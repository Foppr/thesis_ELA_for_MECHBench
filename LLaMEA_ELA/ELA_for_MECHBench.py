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


class ELAForMECHBench(ELAproblem):
    def __init__(self, problem_type, size, features):
        """
        :param: problem_type (int): problem ID (1, 2, 3)
        :param: size (int): size of the problem (30, 60, 125, 250, 500) * D
        :param: features (list): list of features
        """
        super().__init__()
        data_path = "../Folder_Points/500D"
        if problem_type == 1:
            abs_path = os.path.abspath(data_path + "/data_p1")
            dim = 5
            self.dim_stats = dim
        elif problem_type == 2:
            abs_path = os.path.abspath(data_path + "/data_p2")
            dim = 5
            self.dim_stats = dim
        elif problem_type == 3:
            abs_path = os.path.abspath(data_path + "/data_p3")
            dim = 15
            self.dim_stats = 20  # For p3, use dim=20 from the stats, because dim=15 is absent
        else:
            print('Please enter a valid problem type (1, 2 or 3)')
            sys.exit(1)

        self.dim = dim

        points_df = pd.read_csv(f"{abs_path}/points/{size}d{dim}_p{problem_type}_seed1312.csv", index_col='id')
        min_max_points_df = pd.read_csv(f"{abs_path}/points_min_max/min_max_{size}d{dim}_p{problem_type}_seed1312.csv", index_col='id')
        self.X = points_df.iloc[:, :dim]  # x0-x4 for p1-2, x0-x14 for p3
        self.X_scaled = min_max_points_df.iloc[:, :dim]
        self.original_ela_df = pd.read_csv(f"{abs_path}/ELA/ela_{size}d{dim}_p{problem_type}_seed1312.csv", index_col='feature')
        self.min_max_ela_df = pd.read_csv(f"{abs_path}/ELA_min_max/minmax_ela_{size}d{dim}_p{problem_type}_seed1312.csv", index_col='feature')

        # New updated ela stats per size:
        self.ela_stats = pd.read_csv(f"../Folder_Points/500D/by_size/{size}d/{size}d_updated_ELA_stats.csv")

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

    def evaluate_for_MECHBench(self, solution, logger=None):
        code = solution.code
        proxy_name = solution.name

        exec(code, globals())

        proxy_class = globals()[proxy_name]
        proxy_instance = proxy_class(dim=self.dim)
        problem = proxy_instance.f
        objective_values = {}
        ela_per_seed = {}

        y = self.X.apply(problem, axis=1)  # Per seed, get y by evaluating the proxy on X
        # if not isinstance(y, pd.core.series.Series):
        #     print(f"y for seed {seed} and problem {solution.name}: {y}")

        # Pre-processing and normalization
        y[y == 0] = 0.1 ** 100  # since y=0 breaks log
        if y.max() == y.min():
            for i in range(len(y)):
                y[i] = 0
            y_scaled = y
        else:
            # Scale y
            y_scaled = (y - y.min()) / (y.max() - y.min())

        ela_proxy = self.compute_ela(self.X_scaled, y_scaled)
        ela_proxy = pd.Series(ela_proxy)
        ela_proxy = ela_proxy.reset_index()
        ela_proxy.columns = ['feature', 'value']
        ela_proxy.index.name = 'feature'
        ela_proxy.name = 'value'
        ela_proxy.set_index('feature', inplace=True)

        original_ela_dic = self.original_ela_df.round(4).to_dict()['value']
        proxy_ela_dic = ela_proxy.round(4).to_dict()['value']
        solution.add_metadata("Original ELA values (no min-max)", original_ela_dic)
        solution.add_metadata("Proxy ELA values (no min-max)", proxy_ela_dic)
        print(f"ORIGINAL ELA: \n{self.original_ela_df.to_string()}")
        print(f"PROXY ELA: \n{ela_proxy.to_string()}")

        # Min-max normalization on proxy ELA values:
        stats_filtered = self.ela_stats[
            (self.ela_stats['dimension'] == self.dim_stats) & (self.ela_stats['dataset'] == 'BBOB_SM_all')]

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
        print(f"ORIGINAL ELA MIN-MAX: \n{self.min_max_ela_df.to_string()}")
        print(f"PROXY ELA MIN-MAX: \n{ela_proxy_minmax.to_string()}")

        distances = {}
        abs_distances = {}
        distances_minmax = {}
        abs_distances_minmax = {}
        for i in range(len(ela_proxy)):
            # Grab the feature name from the index
            feature_name = ela_proxy.index[i]

            # Grab the actual scalar float values from column 0 ('value')
            proxy_val = ela_proxy.iloc[i, 0]
            original_val = self.original_ela_df.iloc[i, 0]
            proxy_val_minmax = ela_proxy_minmax.iloc[i, 0]
            print(f"proxy_val_minmax for {feature_name}: {proxy_val_minmax}\n")
            original_val_minmax = self.min_max_ela_df.iloc[i, 0]
            print(f"original_val_minmax for {feature_name}: {original_val_minmax}\n")

            pairwise_distance = proxy_val - original_val
            pairwise_distance_minmax = proxy_val_minmax - original_val_minmax
            print(f"pairwise_distance_minmax for {feature_name}: {pairwise_distance_minmax}\n\n")

            # solution.add_metadata(f"Distance to {feature_name}", round(pairwise_distance, 3))
            distances[feature_name] = pairwise_distance
            abs_distances[feature_name] = abs(pairwise_distance)
            distances_minmax[feature_name] = pairwise_distance_minmax
            abs_distances_minmax[feature_name] = abs(pairwise_distance_minmax)
            # feedback += f"{feature_name}: {pairwise_distance: .3f} (Original value: {original_val: .3f}, proxy value: {proxy_val: .3f}) \n"

        print(f"\nabs_distances_minmax: {abs_distances_minmax}\n")
        solution.add_metadata('Distances', distances)
        solution.add_metadata('Absolute distances', abs_distances)
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
    problem_type = int(os.environ.get("PROBLEM_TYPE", 1))
    ES_config = (os.environ.get("ES_CONFIG", "1E1"))
    print(ES_config)
    n_parents = int(ES_config[0])
    elitism = bool(1 if ES_config[1] == "E" else 0)
    n_offspring = int(ES_config[2])
    problem = ELAForMECHBench(problem_type=problem_type,
                              size=500,  # <-- Optional edit: dataset size (30, 60, 125, 250 or 500)
                              features=features)

    print(f"--- Launching Experiment ---")
    print(f"Problem {problem_type} ({ES_config})")
    print(f"------------------------------------------")

    ai_model = "qwen3-coder:30b"
    llm = Ollama_LLM(ai_model)

    # LLaMEA setup
    role_prompt = "You are a highly skilled computer scientist in the field optimization and benchmarking."

    for experiment_i in range(5):  # 5 runs
    # for experiment_i in range(1):  # 1 run
        experiment_name = f"p{problem_type}_({ES_config})_run{experiment_i}"
        print(f'Running experiment number {experiment_i}')
        es = LLaMEA(
            f=problem.evaluate_for_MECHBench,
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