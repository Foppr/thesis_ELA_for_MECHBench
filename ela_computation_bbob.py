"""Generate BBOB samples with SciPy, evaluate with IOHexperimenter, export ELA.

Run:     python ela_computation_bbob.py
Small:   python ela_computation_bbob.py --fids 1 8 --iids 1 --dimensions 5

One CSV row represents one (fid, iid, dim, seed_number, normalization).
Both raw and min-max-normalized objective values are used by default, as in
ela_computation_raw.py. Input coordinates are never normalized. All seven
feature groups from that script (including PCA) are retained. Sampling uses
SciPy rather than pflacco; feature extraction still requires pflacco.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import ioh
import numpy as np
import pandas as pd
from scipy.stats import qmc
from sklearn.preprocessing import MinMaxScaler
import pflacco.classical_ela_features as ela

# Edit these defaults here or override them on the command line.
FUNCTION_IDS = list(range(1, 25))
DIMENSIONS = [5, 10, 20]
SEEDS = list(range(1312, 1327))  # Random seeds for reproducibility.

# # Small:
# FUNCTION_IDS = list(range(1, 6))
# DIMENSIONS = [5]
# SEEDS = [1312]  # Random seeds for reproducibility.

INSTANCE_IDS = list(range(1, 6))
SAMPLE_MULTIPLIER = 250  # Number of sample points = multiplier * dimension.

def generate_sample(dimension: int, n_samples: int, seed: int,
                    method: str = 'lhs') -> np.ndarray:
    """Generate a reproducible design on the BBOB study domain [-5, 5]^d.

    The same design is reused across functions and instances for a fixed
    (dimension, sample size, seed). A seed identifies a sampling repetition;
    it is independent of the BBOB instance ID.
    """
    if dimension < 2 or n_samples < 2 or seed < 0:
        raise ValueError('Require dimension >= 2, n_samples >= 2, seed >= 0.')
    if method == 'lhs':
        unit_sample = qmc.LatinHypercube(d=dimension, seed=seed).random(n_samples)
    elif method == 'sobol':
        unit_sample = qmc.Sobol(d=dimension, seed=seed).random(n_samples)
    elif method == 'random':
        unit_sample = np.random.default_rng(seed).random((n_samples, dimension))
    else:
        raise ValueError(f'Unknown sampling method: {method}')
    return qmc.scale(unit_sample, [-5.0] * dimension, [5.0] * dimension)


def evaluate_bbob(X: np.ndarray, fid: int, iid: int) -> np.ndarray:
    """Evaluate every sample point on the requested noiseless BBOB instance."""
    problem = ioh.get_problem(
        fid=fid, instance=iid, dimension=X.shape[1],
        problem_class=ioh.ProblemClass.BBOB,
    )
    # Explicit pointwise evaluation also works on IOH versions without batching.
    y = np.asarray([problem(x.tolist()) for x in X], dtype=float)
    if not np.isfinite(y).all():
        raise ValueError(f'Non-finite objective values for fid={fid}, iid={iid}.')
    return y


def compute_ela(X, y, normalize=True):
        if normalize:
            y[y == 0] = 0.1 ** 100  # since y=0 breaks log
            if y.max() == y.min():
                for i in range(len(y)):
                    y[i] = 0
                y = y
            else:
                # Scale y
                y = (y - y.min()) / (y.max() - y.min())

        ela_distr = ela.calculate_ela_distribution(X, y)
        ela_meta = ela.calculate_ela_meta(X, y)
        ela_disp = ela.calculate_dispersion(X, y)
        ela_ic = ela.calculate_information_content(X, y)
        ela_nbc = ela.calculate_nbc(X, y)
        ela_pca = ela.calculate_pca(X, y)
        ela_level = ela.calculate_ela_level(X, y)

        ela_1 = ela_disp['disp.ratio_mean_02']  # 1) disp.ratio_mean_02
        ela_2 = ela_distr['ela_distr.skewness']  # 2) ela_distr.skewness
        ela_3 = ela_meta['ela_meta.lin_simple.adj_r2']  # 3) ela_meta.lin_simple.adj_r2
        ela_4 = ela_meta['ela_meta.lin_simple.intercept']  # 4) ela_meta.lin_simple.intercept
        ela_5 = ela_meta['ela_meta.lin_simple.coef.max']  # 5) ela_meta.lin_simple.coef.max
        ela_6 = ela_meta['ela_meta.quad_simple.adj_r2']  # 6) ela_meta.quad_simple.adj_r2
        ela_7 = ela_ic['ic.eps_ratio']  # 7) ic.eps_ratio
        ela_8 = ela_ic['ic.eps_s']  # 8) ic.eps_s
        ela_9 = ela_nbc['nbc.nb_fitness.cor']  # 9) nbc.nb_fitness.cor
        ela_10 = ela_pca['pca.expl_var_PC1.cov_init']  # 10) Pca.expl_var_PC1.cov_init
        ela_11 = ela_level['ela_level.mmce_qda_25']  # 11
        ela_12 = ela_level['ela_level.lda_qda_25']  # 12

        ela_values = {
            'disp.ratio_mean_02': ela_1,
            'ela_distr.skewness': ela_2,
            'ela_meta.lin_simple.adj_r2': ela_3,
            'ela_meta.lin_simple.intercept': ela_4,
            'ela_meta.lin_simple.coef.max': ela_5,
            'ela_meta.quad_simple.adj_r2': ela_6,
            'ic.eps_ratio': ela_7,
            'ic.eps_s': ela_8,
            'nbc.nb_fitness.cor': ela_9,
            # 'pca.expl_var_PC1.cov_init': ela_10,
            'ela_level.mmce_qda_25': ela_11,
            'ela_level.lda_qda_25': ela_12
        }

        return ela_values


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--fids', nargs='+', type=int, default=FUNCTION_IDS)
    parser.add_argument('--iids', nargs='+', type=int, default=INSTANCE_IDS)
    parser.add_argument('--dimensions', nargs='+', type=int, default=DIMENSIONS)
    parser.add_argument('--seeds', nargs='+', type=int, default=SEEDS)
    parser.add_argument('--multiplier', type=int, default=SAMPLE_MULTIPLIER)
    parser.add_argument('--n-samples', type=int, default=None,
                        help='Fixed sample count, overriding multiplier * dimension.')
    parser.add_argument('--sampling', choices=['lhs', 'sobol', 'random'], default='sobol')
    parser.add_argument('--normalization', choices=['both', 'raw', 'minmax'], default='minmax')
    # parser.add_argument('--output', type=Path, default=OUTPUT_CSV)
    args = parser.parse_args()
    if any(fid < 1 or fid > 24 for fid in args.fids):
        parser.error('BBOB function IDs must be between 1 and 24.')
    if any(iid < 1 for iid in args.iids):
        parser.error('Instance IDs must be positive.')
    if any(dim < 2 for dim in args.dimensions):
        parser.error('Dimensions must be >= 2.')
    if any(seed < 0 for seed in args.seeds):
        parser.error('Seeds must be nonnegative.')
    if args.multiplier < 1 or (args.n_samples is not None and args.n_samples < 2):
        parser.error('Use multiplier >= 1 and n-samples >= 2.')
    for field in ('fids', 'iids', 'dimensions', 'seeds'):
        setattr(args, field, list(dict.fromkeys(getattr(args, field))))
    return args


def main() -> None:
    args = parse_args()
    modes = ['raw', 'minmax'] if args.normalization == 'both' else [args.normalization]
    rows = []
    # args.output.parent.mkdir(parents=True, exist_ok=True)
    # Checkpoint after each (dimension, seed) to retain completed batches.
    for dim in args.dimensions:
        OUTPUT_CSV = Path(__file__).resolve().parent / 'output_ela' / f'ela_features_bbob_dim{dim}.csv'
        n_samples = args.n_samples if args.n_samples is not None else args.multiplier * dim
        for repetition, seed in enumerate(args.seeds):
            X = generate_sample(dim, n_samples, seed, args.sampling)
            for fid in args.fids:
                for iid in args.iids:
                    y = evaluate_bbob(X, fid, iid)
                    for mode in modes:
                        metadata = dict(fid=fid, iid=iid, dim=dim, rep=repetition + 1,
                                        seed_number=seed, n_samples=n_samples,
                                        sampling=args.sampling, normalization=mode,
                                        )
                        try:
                            features = compute_ela(X, y, normalize=mode == 'minmax')
                        except Exception as exc:
                            raise RuntimeError(f'ELA computation failed for {metadata}') from exc
                        rows.append({**features, **metadata})
                    print(f'Computed fid={fid}, iid={iid}, dim={dim}, seed={seed}, n={n_samples}',
                          flush=True)
            pd.DataFrame(rows).to_csv(OUTPUT_CSV, index=False)
            print(f'Saved {len(rows)} rows to {OUTPUT_CSV}', flush=True)


if __name__ == '__main__':
    main()
