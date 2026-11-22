import sys

from ELA import ELAproblem
import pflacco.classical_ela_features as ela
import pandas as pd
import numpy as np
import os
import re
from llamea import Solution
import argparse
from llamea.llm import Ollama_LLM
from llamea.llamea import LLaMEA
import joblib


def ela_distance(s1, s2):
    """
    Calculate the ELA distance between two solutions based on their metadata.
    """
    if "Proxy min-max ELA values" not in s1.metadata or "Proxy min-max ELA values" not in s2.metadata:
        return 0.0

    features1 = s1.metadata["Proxy min-max ELA values"]
    features2 = s2.metadata["Proxy min-max ELA values"]

    # Turn into arrays
    features1 = np.array(list(features1.values()))
    features2 = np.array(list(features2.values()))

    # Replace NaN values with zeros
    features1 = np.nan_to_num(features1, nan=0.0)
    features2 = np.nan_to_num(features2, nan=0.0)

    try:
        scaler = joblib.load(f"ela_scaler.joblib")
        features1 = scaler.transform(features1)
        features2 = scaler.transform(features2)
    except:
        pass

    # Calculate the Manhattan distance between the two feature vectors
    if len(features1) != len(features2):
        # fallback to Euclidean distance if lengths differ
        return np.linalg.norm(features1 - features2)
    return np.sum(np.abs(features1 - features2))


class ELAForBBOB(ELAproblem):
    def __init__(self, fid, size, features, dim, seed):
        """
        :param: problem_type (int): problem ID (1, 2, 3)
        :param: size (int): size of the problem (30, 60, 125, 250, 500) * D
        :param: features (list): list of features
        """
        super().__init__()

        self.dim = dim
        self.seed = seed
        self.X = pd.read_csv(f'../Folder_point_new/BBOB/{self.seed}/250d{self.dim}_seed{seed}.csv')

        self.min_max_ela_df = pd.read_csv(f'../Folder_point_new/BBOB/bbob_f{fid}_iid1_dim{dim}_minmax.csv', index_col=0)

        # New updated ela stats per size:
        self.ela_stats = pd.read_csv(f"ela_feature_stats.csv")

        self.features = features

        self.mutation_prompts = [
            "Create a new landscape class by mutating the selected code. Keep the same interface, but modify the mathematical structure of f(x). Try to improve the fitness score based on the feedback.",
            "Create a new landscape class by making a small mutation to the selected code, such as changing coefficients, frequencies, nonlinear terms, interactions, or shifts.",
            "Create a new landscape class by making a larger mutation to the selected code while preserving the same interface.",
            "Create a new landscape class that is substantially different from the selected solution but still follows the task description."
        ]
        self.task_prompt = """
        Your task is to design a novel mathematical function to be used as a black-box optimization benchmark landscape.

        Write a Python class with:
        - an __init__(dim) function receiving the number of dimensions;
        - a function f(x), where x is a real-valued NumPy array.

        The function will be used as a minimization problem.
        The function will be evaluated on the domain [-5.0, 5.0]^dim.

        Return only the complete Python class.
        """

    @staticmethod
    def compute_ela(X, y):
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

    def evaluate_for_BBOB(self, solution, logger=None):
        code = solution.code
        proxy_name = solution.name

        exec(code, globals())

        proxy_class = globals()[proxy_name]
        proxy_instance = proxy_class(dim=self.dim)
        problem = proxy_instance.f
        objective_values = {}
        ela_per_seed = {}

        y = self.X.apply(problem, axis=1)  # Per seed, get y by evaluating the proxy on X

        y[y == 0] = 0.1 ** 100  # since y=0 breaks log
        if y.max() == y.min():
            for i in range(len(y)):
                y[i] = 0
            y_scaled = y
        else:
            # Scale y
            y_scaled = (y - y.min()) / (y.max() - y.min())

        ela_proxy = self.compute_ela(self.X, y_scaled)
        ela_proxy = pd.Series(ela_proxy)
        ela_proxy = ela_proxy.reset_index()
        ela_proxy.columns = ['feature', 'value']
        ela_proxy.index.name = 'feature'
        ela_proxy.name = 'value'
        ela_proxy.set_index('feature', inplace=True)

        proxy_ela_dic = ela_proxy.round(4).to_dict()['value']
        solution.add_metadata("Proxy ELA values (no min-max)", proxy_ela_dic)
        # print(f"PROXY ELA: \n{ela_proxy.to_string()}")

        # Min-max normalization on proxy ELA values:
        stats_filtered = self.ela_stats[
            (self.ela_stats['dimension'] == self.dim) & (self.ela_stats['dataset'] == 'BBOB_SM_all')]

        # Explicitly join using left_index=True because 'feature' was set as the index
        merged_df = pd.merge(ela_proxy, stats_filtered[['feature', 'min', 'max']],
                             left_index=True, right_on='feature', how='left')

        denominator = merged_df['max'] - merged_df['min']
        denominator = denominator.replace(0, np.nan)
        merged_df['normalized_value'] = (merged_df['value'] - merged_df['min']) / denominator
        merged_df['normalized_value'] = merged_df['normalized_value'].fillna(0.0)
        ela_proxy_minmax = merged_df[['feature', 'normalized_value']].rename(columns={'normalized_value': 'value'})

        # Re-index ela_proxy_minmax
        ela_proxy_minmax.set_index('feature', inplace=True)

        original_ela_minmax_dic = self.min_max_ela_df.round(4).to_dict()['value']
        proxy_ela_minmax_dic = ela_proxy_minmax.round(4).to_dict()['value']
        solution.add_metadata("Original min-max ELA values", original_ela_minmax_dic)
        solution.add_metadata("Proxy min-max ELA values", proxy_ela_minmax_dic)
        # print(f"ORIGINAL ELA MIN-MAX: \n{self.min_max_ela_df.to_string()}")
        # print(f"PROXY ELA MIN-MAX: \n{ela_proxy_minmax.to_string()}")

        distances_minmax = {}
        abs_distances_minmax = {}
        for i in range(len(ela_proxy)):
            # Grab the feature name from the index
            feature_name = ela_proxy.index[i]

            # Grab the actual scalar float values from column 0 ('value')
            proxy_val_minmax = ela_proxy_minmax.iloc[i, 0]
            print(f"proxy_val_minmax for {feature_name}: {proxy_val_minmax}\n")
            original_val_minmax = self.min_max_ela_df.iloc[i, 0]
            print(f"original_val_minmax for {feature_name}: {original_val_minmax}\n")

            pairwise_distance_minmax = proxy_val_minmax - original_val_minmax
            print(f"pairwise_distance_minmax for {feature_name}: {pairwise_distance_minmax}\n\n")

            # solution.add_metadata(f"Distance to {feature_name}", round(pairwise_distance, 3))
            distances_minmax[feature_name] = pairwise_distance_minmax
            abs_distances_minmax[feature_name] = abs(pairwise_distance_minmax)
            # feedback += f"{feature_name}: {pairwise_distance: .3f} (Original value: {original_val: .3f}, proxy value: {proxy_val: .3f}) \n"

        print(f"\nabs_distances_minmax: {abs_distances_minmax}\n")
        solution.add_metadata('Min-max distances', distances_minmax)
        solution.add_metadata('Absolute min-max distances', abs_distances_minmax)

        distance_series_minmax = (ela_proxy_minmax - self.min_max_ela_df)
        print(f"DISTANCE SERIES MIN-MAX: \n{distance_series_minmax}")

        # final_score = distance_series_minmax['value'].abs().mean()
        final_score = distance_series_minmax['value'].abs().sum()  # Manhattan distance
        solution.add_metadata("Raw manhattan distance (min-max normalized)", final_score)

        feedback = f"The landscape '{proxy_name}' had manhattan distance (fitness) {final_score:.3f}. Lower is better.\n"
        feature_distances = distance_series_minmax.to_dict()['value']
        for feature_name, distance in feature_distances.items():
            feedback += f"{feature_name}: error {distance:.3f}\n"

        print(f"MANHATTAN DISTANCE (min-max): \n{final_score}")
        solution.set_scores(
            final_score,  # Fitness
            feedback=f"{feedback}",
        )

        return solution


if __name__ == '__main__':
    # Environment and mutations setup
    features = [
        'disp.ratio_mean_02',
        'ela_distr.skewness',
        'ela_meta.lin_simple.adj_r2',
        'ela_meta.lin_simple.intercept',
        'ela_meta.lin_simple.coef.max',
        'ela_meta.quad_simple.adj_r2',
        'ic.eps_ratio',
        'ic.eps_s',
        'nbc.nb_fitness.cor',
        # 'pca.expl_var_PC1.cov_init',
        'ela_level.mmce_qda_25',
        'ela_level.lda_qda_25'
    ]

    # Read variables dynamically from slurm:
    dim = int(os.environ.get("dim", 5))
    seed = int(os.environ.get("seed", 1312))
    fid = int(os.environ.get("fid", 1))
    ES_config = (os.environ.get("ES_CONFIG", "1E1"))
    print(ES_config)
    n_parents = int(ES_config[0])
    elitism = bool(1 if ES_config[1] == "E" else 0)
    n_offspring = int(ES_config[2])
    problem = ELAForBBOB(fid=fid,
                              size=500,  # <-- Optional edit: dataset size (30, 60, 125, 250 or 500)
                              features=features,
                         dim=dim,
                         seed=seed)

    print(f"--- Launching Experiment ---")
    print(f"f{fid} ({ES_config})")
    print(f"------------------------------------------")

    ai_model = "qwen3-coder:30b"
    llm = Ollama_LLM(ai_model)

    # LLaMEA setup
    role_prompt = "You are a highly skilled computer scientist in the field optimization and benchmarking."
    seeds = [1312, 1313, 1314, 1315, 1316]  # First 5/15 seeds for the loop

    # for seed in seeds:  # 5 runs
    experiment_name = f"f{fid}_({ES_config})_seed{seed}"
    print(f'Running experiment with seed {seed}')
    es = LLaMEA(
        f=problem.evaluate_for_BBOB,
        minimization=True,  # IMPORTANT: Distance should be minimized (0 is best)
        n_parents=n_parents,
        n_offspring=n_offspring,
        llm=llm,
        role_prompt=role_prompt,
        task_prompt=problem.task_prompt,
        mutation_prompts=problem.mutation_prompts,
        experiment_name=experiment_name,
        elitism=elitism,  # False=,   True=+
        HPO=False,
        max_workers=4,
        budget=100,
        parallel_backend="loky",
        niching="sharing",
        distance_metric=ela_distance,
        niche_radius=2.0,
        adaptive_niche_radius=True,
        eval_timeout=3600,
        dim=dim,
        fid=fid,
        config=ES_config,
        seed=seed
    )
    print(es.run())


# Edit log function:
def edit_form(dic_):
    s = ""
    for i, feature in enumerate(features):
        proxy_value = round(dic_['Proxy ELA values'][i][0], 4)
        original_value = round(dic_['Original ELA values'][i][0], 4)
        distance = dic_[f'Distance to {feature}']
        s += f"{feature}: distance {distance} (Original: {original_value}, Proxy: {proxy_value})\n"

    return s