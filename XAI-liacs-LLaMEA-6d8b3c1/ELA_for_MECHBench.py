from ELA import ELAproblem
import pflacco.classical_ela_features as ela
import pandas as pd
import numpy as np
import os
import re
from llamea import Solution
import argparse


class ELAForMECHBench(ELAproblem):
    def __init__(self, mechbench_points, mechbench_objective_values, mechbench_ela, feature_descriptions):
        super().__init__()
        self.points = mechbench_points
        self.objective_values = mechbench_objective_values
        self.mechbench_ela = mechbench_ela
        self.feature_descriptions = feature_descriptions

    @staticmethod
    def compute_ela(X, y):
        ela_distr = ela.calculate_ela_distribution(X, y)
        ela_meta = ela.calculate_ela_meta(X, y)
        ela_disp = ela.calculate_dispersion(X, y)
        ela_ic = ela.calculate_information_content(X, y)
        ela_nbc = ela.calculate_nbc(X, y)
        ela_pca = ela.calculate_pca(X, y)

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

        ela_values = {
            'disp.ratio_mean_02': ela_1,
            'ela_distr.skewness': ela_2,
            'ela_meta.lin_simple.adj_r2': ela_3,
            'ela_meta.lin_simple.intercept': ela_4,
            'ela_meta.lin_simple.coef.max': ela_5,
            'ela_meta.quad_simple.adj_r2': ela_6,
            'ic.eps_ratio':  ela_7,
            'ic.eps_s': ela_8,
            'nbc.nb_fitness.cor': ela_9,
            'pca.expl_var_PC1.cov_init': ela_10
        }

        return ela_values

    def evaluate_for_MECHBench(self, solution, logger=None):
        code = solution.code
        proxy_name = solution.name

        exec(code, globals())

        algorithm = None
        # Final validation
        feature_results = {}
        results = []

        # proxy = globals()[proxy_name](DIM)
        proxy_class = globals()[proxy_name]
        proxy_instance = proxy_class(dim=5)
        problem = proxy_instance.f
        all_features = []
        objective_values = {}
        ela_per_seed = {}

        for seed, X in self.points.items():
            y = X.apply(problem, axis=1)  # Per seed, get y by evaluating the proxy on X

            # Pre-processing and normalization
            y[y == 0] = 0.1 ** 100  # since y=0 breaks log
            if y.max() == y.min():
                for i in range(len(y)):
                    y[i] = 0
                y_scaled = y
            else:
                y_scaled = (y - y.min()) / (y.max() - y.min())

            objective_values[seed] = y_scaled
            ela_proxy = self.compute_ela(X, y_scaled)

            # Get the ELA features from the sample points and proxy objective values in format {name1: value1, name2: value2, ...}
            ela_per_seed[seed] = ela_proxy

        ela_proxy_df = pd.DataFrame(ela_per_seed)
        ela_proxy_df = ela_proxy_df.T
        # print(f"Proxy ELA df: \n{ela_proxy_df.to_string()}")

        ela_full_df = pd.concat([self.mechbench_ela, ela_proxy_df], axis=0)
        # print(f"Full df: \n{ela_full_df.to_string()}")

        z_score_df = (ela_full_df - ela_full_df.mean()) / ela_full_df.std()
        # print(f"Full z-standardized df: \n{z_score_df.to_string()}")

        z_mechbench = z_score_df.iloc[:11]
        z_proxy = z_score_df.iloc[11:]

        z_mean_mechbench = z_mechbench.mean()
        z_mean_proxy = z_proxy.mean()

        distance_series = (z_mean_mechbench - z_mean_proxy).abs()
        distance_series.name = "feature_distance"

        solution.add_metadata("MECHBench_mean_z", z_mean_mechbench.to_numpy())
        solution.add_metadata("proxy_mean_z", z_mean_proxy.to_numpy())
        solution.add_metadata("proxy_mean_z", distance_series.to_numpy())

        feedback = f"The optimization landscape {proxy_name} scored on:"
        distances_dic = distance_series.to_dict()

        for feature, distance in distances_dic.items():
            solution.add_metadata(f"distance_{feature}", distance)
            feedback += f"{feature} {distance:.3f}, "

        final_score = distance_series.mean()
        solution.set_scores(
            final_score,
            f"{feedback} (lower is better, 0.0 is the best).",
        )

        return solution


class SinusoidalHomogeneousLandscape:
    def __init__(self, dim=5):
        self.dim = dim
        # Precompute frequency factors for different dimensions
        self.frequencies = np.arange(1, dim + 1) * 0.5

    def f(self, x):
        # Normalize input to [-pi, pi] for sinusoidal functions
        x_normalized = x * (np.pi / 5.0)

        # Base quadratic term for conditioning
        quadratic = np.sum(x ** 2)

        # Sinusoidal components with different frequencies
        sinusoidal = np.sum(np.sin(self.frequencies * x_normalized) *
                            np.cos(self.frequencies * x_normalized) *
                            np.exp(-0.1 * np.abs(x)))

        # Add a small constant to ensure global minimum is at origin
        # and create a smooth landscape with homogeneous basin sizes
        result = quadratic + 0.5 * sinusoidal + 0.1 * np.sum(np.sin(x_normalized) ** 2)

        return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run ELA problem with LLaMEA.")
    parser.add_argument(
        "--share",
        action="store_true",
        help="Enable the sharing feature."
    )
    args = parser.parse_args()

    niching = None
    experiment_name = "ELA_for_MECHBENCH"
    if args.share:
        niching = "sharing"

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
            'pca.expl_var_PC1.cov_init',
        ]

    ela_1 = f"From pflacco's calculate_dispersion['disp.ratio_mean_02']: The dispersion features compare the dispersion, i.e. the (aggregated) pairwise distances, of all points in the initial design with the dispersion among the best points in the initial design. Per default, this set of “best points” is based on the 2%, 5% and 10% quantile of the objectives. Those dispersions are then compared based on the ratio as well as on the difference. [ratio, diff]_[mean, median]_[02, 05, 10, 25]: ratio and difference of the mean / median distances of the distances of the ‘best’ objectives vs. ‘all’ objectives"
    ela_2 = f"From pflacco's calculate_ela_distribution['ela_distr.skewness']: "
    ela_3 = f""
    ela_4 = f""
    ela_5 = f""
    ela_6 = f""
    ela_7 = f""
    ela_8 = f""
    ela_9 = f""
    ela_10 = f""

    feature_descriptions = {
            'disp.ratio_mean_02': ela_1,
            'ela_distr.skewness': ela_2,
            'ela_meta.lin_simple.adj_r2': ela_3,
            'ela_meta.lin_simple.intercept': ela_4,
            'ela_meta.lin_simple.coef.max': ela_5,
            'ela_meta.quad_simple.adj_r2': ela_6,
            'ic.eps_ratio':  ela_7,
            'ic.eps_s': ela_8,
            'nbc.nb_fitness.cor': ela_9,
            'pca.expl_var_PC1.cov_init': ela_10
        }

    problem = ELAproblem(name=f"ELA", features=features, dims=[5], eval_timeout=1200)

    mutation_prompts = []
    for feature in problem.features:
        mutation_prompts.append(
            f"Create a new landscape class based on the selected code and improve the {feature} score, meaning: {problem.feature_descriptions[feature]}.")
    mutation_prompts.append(
        "Create a new landscape class that is completely different from the selected solution but still adheres to the properties outlined in the task description.")

    ai_model = "qwen3-coder:30b"
    llm = Ollama_LLM(ai_model)

    for experiment_i in [1]:
        es = LLaMEA(
            problem.evaluate_function,
            n_parents=8,
            n_offspring=16,
            llm=llm,
            task_prompt=problem.task_prompt,
            example_prompt=problem.example_prompt,
            output_format_prompt=problem.format_prompt,
            mutation_prompts=mutation_prompts,
            experiment_name=experiment_name,
            elitism=False,
            HPO=False,
            budget=budget,
            max_workers=4,
            parallel_backend="loky",
            niching=niching,
            distance_metric=ela_distance,
            niche_radius=0.5,
            adaptive_niche_radius=True,
            eval_timeout=3600,
        )
        print(es.run())


    def test1():
        # Import the sample points
        points = {}
        path = "C:/Users/foppe/Documents/DSAI-3/Thesis/thesis_code/Folder_Points/samples/D250_5D"  # We only have objective values for 5D
        for csv in os.listdir(path):
            seed = csv[-6:-4]
            X = pd.read_csv(f'{path}/{csv}')

            # The whole row is one string, so convert to an array, skipping the id column
            strings = [value[0].split(' ')[1:] for value in X.values]  # [['-4.14', '2.49', ..., '1.35'], ..., [...]]
            X = pd.DataFrame([[float(value) for value in values] for values in strings], dtype=np.float64)
            X_scaled = (X - X.min()) / (X.max() - X.min())
            points[f'seed_{seed}'] = X_scaled

        # Import the objective values
        objective_values = {}
        path = "C:/Users/foppe/Documents/DSAI-3/Thesis/thesis_code/Folder_Points/data_problem_2_5D_1"
        for csv in os.listdir(path):
            seed = csv[-11:-4]
            y = pd.read_csv(f'{path}/{csv}')
            y = y['penalized_mass']  # objective values has to be a Series, not pd df
            y_scaled = (y - y.min()) / (y.max() - y.min())
            objective_values[f'{seed}'] = y_scaled

        ela_per_seed = {}
        for seed, X in points.items():
            ela_dic = ELAForMECHBench.compute_ela(X, objective_values[seed])
            ela_per_seed[seed] = ela_dic

        ela_df = pd.DataFrame(ela_per_seed)
        ela_df = ela_df.T
        ela_df.to_csv("C:/Users/foppe/Documents/DSAI-3/Thesis/thesis_code/Folder_Points/ELA_scaled/problem_2_250D.csv")

        def extract_algorithm_code(message):
            """
            Extracts algorithm code from a given message string using regular expressions.

            Args:
                message (str): The message string containing the algorithm code.

            Returns:
                str: Extracted algorithm code.

            Raises:
                NoCodeException: If no code block is found within the message.
            """
            code_pattern = r"```(?:python|diff)?\n(.*?)\n```"
            match = re.search(code_pattern, message, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(1)


        message = "# Description: This benchmark function combines multiple sinusoidal components with varying frequencies and amplitudes to create a landscape with homogeneous basin sizes and smooth search space. The function features multiple local minima that are evenly distributed in terms of basin size, while maintaining a homogeneous structure throughout the search space. The sinusoidal components create a complex but predictable landscape that challenges optimization algorithms to escape local optima while maintaining consistent search behavior across dimensions.\n\n# Code: \n```python\nimport numpy as np\n\nclass SinusoidalHomogeneousLandscape:\n    \n    def __init__(self, dim=5):\n        self.dim = dim\n        # Precompute frequency factors for different dimensions\n        self.frequencies = np.arange(1, dim + 1) * 0.5\n        \n    def f(self, x):\n        # Normalize input to [-pi, pi] for sinusoidal functions\n        x_normalized = x * (np.pi / 5.0)\n        \n        # Base quadratic term for conditioning\n        quadratic = np.sum(x**2)\n        \n        # Sinusoidal components with different frequencies\n        sinusoidal = np.sum(np.sin(self.frequencies * x_normalized) * \n                           np.cos(self.frequencies * x_normalized) * \n                           np.exp(-0.1 * np.abs(x)))\n        \n        # Add a small constant to ensure global minimum is at origin\n        # and create a smooth landscape with homogeneous basin sizes\n        result = quadratic + 0.5 * sinusoidal + 0.1 * np.sum(np.sin(x_normalized)**2)\n        \n        return result\n```"
        code = extract_algorithm_code(message)

        new_individual = Solution(
            name="SinusoidalHomogeneousLandscape",
            description="This benchmark function combines multiple sinusoidal components with varying frequencies and amplitudes to create a landscape with homogeneous basin sizes and smooth search space. The function features multiple local minima that are evenly distributed in terms of basin size, while maintaining a homogeneous structure throughout the search space. The sinusoidal components create a complex but predictable landscape that challenges optimization algorithms to escape local optima while maintaining consistent search behavior across dimensions.",
            code=code
        )

        efm = ELAForMECHBench(points, objective_values, ela_df)
        distance_series_ = efm.evaluate_for_MECHBench(new_individual)

    def test2():
        ela_mechbench_mean_z = {
            'disp.ratio_mean_02': 0.947832,
            'ela_distr.skewness': 0.973135,
            'ela_meta.lin_simple.adj_r2': -0.976826,
            'ela_meta.lin_simple.intercept': 0.969779,
            'ela_meta.lin_simple.coef.max': -0.959217,
            'ela_meta.quad_simple.adj_r2': -0.976516,
            'ic.eps_ratio': -0.874767,
            'ic.eps_s': 0.970102,
            'nbc.nb_fitness.cor': 0.059940,
            'pca.expl_var_PC1.cov_init': -0.910719
        }

        ela_proxy_mean_z = {
            'disp.ratio_mean_02': -0.947832,
            'ela_distr.skewness': -0.973135,
            'ela_meta.lin_simple.adj_r2': 0.976826,
            'ela_meta.lin_simple.intercept': -0.969779,
            'ela_meta.lin_simple.coef.max': 0.959217,
            'ela_meta.quad_simple.adj_r2': 0.976516,
            'ic.eps_ratio': 0.874767,
            'ic.eps_s': -0.970102,
            'nbc.nb_fitness.cor': -0.059940,
            'pca.expl_var_PC1.cov_init': 0.910719
        }

        df_MECHBench = pd.DataFrame.from_dict(ela_mechbench_mean_z)
        df_proxy = pd.DataFrame.from_dict(ela_proxy_mean_z)

        for e in df_MECHBench:
            print(e)

