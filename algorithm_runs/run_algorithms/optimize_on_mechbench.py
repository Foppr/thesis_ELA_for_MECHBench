import ioh
import warnings
import argparse
import numpy as np
import sys
import os
import signal
import subprocess

sys.path.append('..')
from tqdm import tqdm
from main_analysis import instantiate_optimizer
from MECHBench.smechbench_experiment_utils import get_objective_function

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
_original_os_remove = os.remove


def _safe_os_remove(path, *args, **kwargs):
    try:
        _original_os_remove(path, *args, **kwargs)
    except FileNotFoundError:
        pass


os.remove = _safe_os_remove


def wrap_with_timeout(func, timeout_seconds=1200):
    """
    Closes around the raw target function to enforce execution limits (timeouts)
    AND gracefully handles unphysical geometric simulation crashes (Error 1).
    """
    history_y = []

    def timeout_handler(signum, frame):
        raise TimeoutError("OpenRadioss explicit simulation exceeded maximum runtime limit.")

    def _clean_node_processes():
        """Helper to ensure no rogue MPI processes are left eating CPU."""
        try:
            subprocess.run(["pkill", "-f", "engine_linux64"], capture_output=True)
            subprocess.run(["pkill", "-f", "mpirun"], capture_output=True)
        except Exception as e:
            sys.stderr.write(f"[CLEANUP WARNING] Failed to broadcast process kill signals: {e}\n")

    def wrapped_objective(x, *args, **kwargs):
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(timeout_seconds)

        try:
            val = func(x, *args, **kwargs)
            history_y.append(float(val))

        except TimeoutError:
            # Handle Error 3: Timeouts
            sys.stderr.write(f"\n[TIMEOUT] Evaluation stalled at {timeout_seconds}s. Cleansing cluster node.\n")
            _clean_node_processes()
            val = _compute_penalty()

        except Exception as e:
            # --- FIX FOR ERROR 1: Catch Engine Crashes / Segfault exceptions ---
            sys.stderr.write(
                f"\n[ENGINE CRASH] OpenRadioss failed mathematically on input geometry. Applying penalty.\n")
            _clean_node_processes()
            val = _compute_penalty()

        finally:
            signal.alarm(0)  # Clear the alarm countdown safely

        return val

    def _compute_penalty():
        """Helper to generate a bad minimization score dynamically."""
        if history_y:
            worst_observed = max(history_y)
            std_observed = np.std(history_y) if len(history_y) > 1 else 1.0
            return worst_observed + (2.0 * std_observed) + 1.0
        return 100.0  # Fallback penalty if evaluation #1 fails completely

    return wrapped_objective


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--problem', type=int)
    parser.add_argument('--optimizer', type=str)
    parser.add_argument('--deck_id', type=int)
    parser.add_argument('--seed', type=int)
    parser.add_argument('--timeout', type=int, default=1500)
    args = parser.parse_args()

    problem = args.problem
    optimizer_name = args.optimizer
    seed = args.seed
    print(f"---------------------------------")
    print(f"RUNNING SEED {seed} OPTIMIZER {optimizer_name} ON PROBLEM {problem}")

    if problem == 1 or problem == 2:
        dim = 5
    else:
        dim = 15

    f_no_deck_id = get_objective_function(problem)
    deck_id = args.deck_id

    f_raw = lambda x: f_no_deck_id(np.clip(x, -5, 5), deck_id=deck_id)
    f = wrap_with_timeout(f_raw, timeout_seconds=args.timeout)

    def dummy_optimum(instance, n_variables):
        return ioh.RealSolution(x=[0] * dim, y=-1e10)

    f_wrapped = ioh.wrap_problem(
        f,
        name=f"mechbench_p{problem}",
        optimization_type=ioh.OptimizationType.MIN,
        lb=-5,
        ub=5,
        dimension=dim,
        calculate_objective=dummy_optimum
    )

    logger = ioh.logger.Analyzer(
        root=f'analysis/logger_data/mechbench/seed{seed}/p{problem}',
        folder_name=f"{optimizer_name}",
        algorithm_name=f"{optimizer_name}_mechbench",
        store_positions=True,
        triggers=[ioh.logger.trigger.ALWAYS]
    )

    f_wrapped.attach_logger(logger)

    optimizer = instantiate_optimizer(f_wrapped, dim, optimizer_name, seed)
    optimizer.run()
    logger.close()


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    main()