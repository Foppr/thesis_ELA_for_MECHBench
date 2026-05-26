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
    if "Proxy ELA values" not in s1.metadata or "Proxy ELA values" not in s2.metadata:
        return 0.0  # No features to compare

    features1 = s1.metadata["Proxy ELA values"]
    features2 = s2.metadata["Proxy ELA values"]

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
    def __init__(self, mechbench_points, mechbench_objective_values, mechbench_ela, features):
        super().__init__()
        self.points = mechbench_points
        self.objective_values = mechbench_objective_values
        self.mechbench_ela = mechbench_ela
        mechbench_means = self.mechbench_ela.mean()
        self.features = features
        self.feature_descriptions = {
            'disp.ratio_mean_02': f"should approach the value {mechbench_means['disp.ratio_mean_02']: .3f}. Explanation: From pflacco's calculate_dispersion['disp.ratio_mean_02']: The dispersion features compare the dispersion, i.e. the (aggregated) pairwise distances, of all points in the initial design with the dispersion among the best points in the initial design. Per default, this set of “best points” is based on the 2%, 5% and 10% quantile of the objectives. Those dispersions are then compared based on the ratio as well as on the difference. [ratio, diff]_[mean, median]_[02, 05, 10, 25]: ratio and difference of the mean / median distances of the distances of the ‘best’ objectives vs. ‘all’ objectives. Taken from https://pflacco.readthedocs.io/en/latest/dispersion.html.",
            'ela_distr.skewness': f"should approach the value {mechbench_means['ela_distr.skewness']: .3f}. Explanation: From pflacco's calculate_ela_distribution['ela_distr.skewness']: skewness of the objective values.",
            'ela_meta.lin_simple.adj_r2': f"should approach the value {mechbench_means['ela_meta.lin_simple.adj_r2']: .3f}. Explanation: From pflacco's calculate_ela_meta['ela_meta.lin_simple.adj_r2']: 'Meta-Model: Linear and quadratic regression models with or without interactions are fitted to the initial data D. The adjusted coefficient of determination R2 is returned in each case as an indicator for model accuracy. Functions with variable scaling will not allow a good fit of regression models without interaction effects, and simple unimodal functions might be approximated by using a quadratic model. In addition, features are extracted which reflect the size relations of the model coefficients.' (Mersmann et al., 2011) lin_simple.adj_r2: adjusted R^2 (i.e. model fit) of a simple linear model.",
            'ela_meta.lin_simple.intercept': f"should approach the value {mechbench_means['ela_meta.lin_simple.intercept']: .3f}. Explanation: From pflacco's calculate_ela_meta['ela_meta.lin_simple.intercept']: 'Meta-Model: Linear and quadratic regression models with or without interactions are fitted to the initial data D. The adjusted coefficient of determination R2 is returned in each case as an indicator for model accuracy. Functions with variable scaling will not allow a good fit of regression models without interaction effects, and simple unimodal functions might be approximated by using a quadratic model. In addition, features are extracted which reflect the size relations of the model coefficients.' (Mersmann et al., 2011) 'ela_meta.lin_simple.intercept': intercept of a simple linear model.",
            'ela_meta.lin_simple.coef.max': f"should approach the value {mechbench_means['ela_meta.lin_simple.coef.max']: .3f}. Explanation: From pflacco's calculate_ela_meta['ela_meta.lin_simple.coef.max']: 'Meta-Model: Linear and quadratic regression models with or without interactions are fitted to the initial data D. The adjusted coefficient of determination R2 is returned in each case as an indicator for model accuracy. Functions with variable scaling will not allow a good fit of regression models without interaction effects, and simple unimodal functions might be approximated by using a quadratic model. In addition, features are extracted which reflect the size relations of the model coefficients.' (Mersmann et al., 2011) 'ela_meta.lin_simple.coef.max': biggest (non-intercept) absolute coefficient of the simple linear model.",
            'ela_meta.quad_simple.adj_r2': f"should approach the value {mechbench_means['ela_meta.quad_simple.adj_r2']: .3f}. Explanation: From pflacco's calculate_ela_meta['ela_meta.quad_simple.adj_r2']: 'Meta-Model: Linear and quadratic regression models with or without interactions are fitted to the initial data D. The adjusted coefficient of determination R2 is returned in each case as an indicator for model accuracy. Functions with variable scaling will not allow a good fit of regression models without interaction effects, and simple unimodal functions might be approximated by using a quadratic model. In addition, features are extracted which reflect the size relations of the model coefficients.' (Mersmann et al., 2011) 'ela_meta.quad_simple.adj_r2': adjusted R^2 (i.e. model fit) of a simple quadratic model (without interactions), i.e. the ratio of its (absolute) biggest and smallest coefficients.",
            'ic.eps_ratio': f"should approach the value {mechbench_means['ic.eps_ratio']: .3f}. Explanation: From pflacco's calculate_information_content['ic.eps_ratio']: Computes features based on the Information Content of Fitness Sequences (ICoFiS) approach (Munoz et al., 2014). In this approach, the information content of a continuous landscape, i.e. smoothness, ruggedness, or neutrality, are quantified. A neutral landscape has low IC, while a rugged landscape has high IC (Munoz et al., 2014). 'ic.eps_ratio': ratio of partial information sensitivity, cf. equation (8) in Munoz et al. (2014) where the ratio is 0.5.",
            'ic.eps_s': f"should approach the value {mechbench_means['ic.eps_s']: .3f}. Explanation: From pflacco's calculate_information_content['ic.eps_s']: Computes features based on the Information Content of Fitness Sequences (ICoFiS) approach (Munoz et al., 2014). In this approach, the information content of a continuous landscape, i.e. smoothness, ruggedness, or neutrality, are quantified. A neutral landscape has low IC, while a rugged landscape has high IC (Munoz et al., 2014). 'ic.eps_s': settling sensitivity, indicating the epsilon for which the sequence nearly consists of zeros only, cf. equation (6) in Munoz et al. (2014).",
            'nbc.nb_fitness.cor': f"should approach the value {mechbench_means['nbc.nb_fitness.cor']: .3f}. Explanation: From pflacco's calculate_nbc['nbc.nb_fitness.cor']: Nearest Better Clustering features. Computes features based on the comparison of nearest neighbour and nearest better neighbour, i.e., the nearest neighbor with a better performance / objective value value. nb_fitness.cor: correlation between fitness value and count of observations to whom the current observation is the nearest better neighbour (the so-called 'indegree').",
            'pca.expl_var_PC1.cov_init': f"should approach the value {mechbench_means['pca.expl_var_PC1.cov_init']: .3f}. Explanation: From pflacco's calculate_pca['pca.expl_var_PC1.cov_init']: Principal component (analysis) features. expl_var_PC1.cov_init: proportion of variance, which is explained by the first principal component when applying PCA to the covariance matrix of the entire initial design.",
            'ela_level.mmce_qda_25': f"should approach the value {mechbench_means['ela_level.mmce_qda_25']: .3f}. Explanation: From pflacco's calculate_ela_level['ela_level.mmce_qda_25']: 'The initial data set D is split into two classes by a specific objective level which works as a threshold. One possibility is to use the median for this, which will result in equally sized classes. Other choices studied are the upper and lower quartiles of the distribution of y. Linear (LDA), quadratic (QDA) and mixture discriminant analysis (MDA) are used to predict whether the objective values Y fall below or exceed the calculated threshold. Multi-modal functions should result in several unconnected sublevel sets for the quantile of lower values, which can only be modeled by MDA, but not LDA or QDA. The extracted low-level features are based on the distribution of the resulting cross-validated mean misclassification errors of each classifier.' (Mersmann et al., 2011) 'ela_level.mmce_qda_25': mean misclassification error of quadratic discriminant analysis (QDA) in the lower quartile (25).",
            'ela_level.lda_qda_25': f"should approach the value {mechbench_means['ela_level.lda_qda_25']: .3f}. Explanation: From pflacco's calculate_ela_level['ela_level.lda_qda_25']: 'The initial data set D is split into two classes by a specific objective level which works as a threshold. One possibility is to use the median for this, which will result in equally sized classes. Other choices studied are the upper and lower quartiles of the distribution of y. Linear (LDA), quadratic (QDA) and mixture discriminant analysis (MDA) are used to predict whether the objective values Y fall below or exceed the calculated threshold. Multi-modal functions should result in several unconnected sublevel sets for the quantile of lower values, which can only be modeled by MDA, but not LDA or QDA. The extracted low-level features are based on the distribution of the resulting cross-validated mean misclassification errors of each classifier.' (Mersmann et al., 2011) 'ela_level.lda_qda_25': mean misclassification error of linear discriminant analysis (QDA) in the lower quartile (25)."
        }
        self.task_prompt = f"""
        Your task is to design novel mathematical functions (proxy functions) to be used as black-box optimization benchmark landscapes, with specific landscape properties.
        The code you need to write is a class with a function `f` with one parameter `x` which is a realvalued sample (numpy array).
        The proxy function's landscape will be quantified using Exploratory Landscape Analysis (ELA) features, using the pflacco Python library. The proxy's landscape should approach that of the original, expensive BBO problem as much as possible, meaning its ELA feature values should be as close as possible to those of the original problem.
        The optimization function should have the following properties: \n- it will be used as minimization problem (so the global optimum should be the minimum value of the function)."""
        for feature in self.features:
            self.task_prompt += f"ELA feature {feature} {self.feature_descriptions[feature]}"
        self.task_prompt += """
        The class should also have a __init__(dim) function, that received the number of dimensions for the function.
        The function will be evaluated between per dimension lower bound of -5.0 and upper bound of 5.0.
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
            'pca.expl_var_PC1.cov_init': ela_10,
            'ela_level.mmce_qda_25': ela_11,
            'ela_level.lda_qda_25': ela_12
        }

        return ela_values

    def evaluate_for_MECHBench(self, solution, logger=None):
        code = solution.code
        proxy_name = solution.name

        exec(code, globals())

        proxy_class = globals()[proxy_name]
        proxy_instance = proxy_class(dim=5)
        problem = proxy_instance.f
        objective_values = {}
        ela_per_seed = {}

        for seed, X in self.points.items():
            y = X.apply(problem, axis=1)  # Per seed, get y by evaluating the proxy on X
            if not isinstance(y, pd.core.series.Series):
                print(f"y for seed {seed} and problem {solution.name}: {y}")

            # Pre-processing and normalization
            y[y == 0] = 0.1 ** 100  # since y=0 breaks log
            if y.max() == y.min():
                for i in range(len(y)):
                    y[i] = 0
                y_scaled = y
            else:
                # Scale y (X should already be scaled before!)
                y_scaled = (y - y.min()) / (y.max() - y.min())

            objective_values[seed] = y_scaled
            ela_proxy = self.compute_ela(X, y_scaled)

            # Get the ELA features from the sample points and proxy objective values in format {name1: value1, name2: value2, ...}
            ela_per_seed[seed] = ela_proxy

        # ela_per_seed = preprocces_data(ela_per_seed)
        ela_proxy_df = pd.DataFrame(ela_per_seed)
        ela_proxy_df = ela_proxy_df.T
        proxy_ela_means = ela_proxy_df.mean()
        mechbench_ela_means = self.mechbench_ela.mean()
        solution.add_metadata("Proxy ELA values", proxy_ela_means.to_numpy())
        solution.add_metadata("Original ELA values", mechbench_ela_means.to_numpy())

        print(f"MECHBench MEANS: \n{mechbench_ela_means}")
        print(f"PROXY MEANS: \n{proxy_ela_means}")

        feedback = f"The optimization landscape '{proxy_name}' had the following distances to the original ELA values: "
        for i in range(len(proxy_ela_means)):
            pairwise_distance = proxy_ela_means[i] - mechbench_ela_means[i]
            solution.add_metadata(f"Distance to {proxy_ela_means.index[i]}", round(pairwise_distance, 3))
            feedback += f"{proxy_ela_means.index[i]}: {pairwise_distance: .3f} (Original value: {mechbench_ela_means[i]}, proxy value: {proxy_ela_means[i]}) \n"

        # # OLD METHOD:
        # # Use mean distance from all z-standardized feature values as final score
        # ela_full_df = pd.concat([self.mechbench_ela, ela_proxy_df], axis=0)
        #
        # print(f"ELA FULL DF: \n{ela_full_df.to_string()}")
        #
        # z_score_df = (ela_full_df - ela_full_df.mean()) / ela_full_df.std()
        # print(f"FULL Z-STANDARD DF: \n{z_score_df.to_string()}")
        #
        # z_mechbench = z_score_df.iloc[:len(z_score_df)//2]
        # print(f"Z MECHBENCH: \n {z_mechbench.to_string()}")
        # z_proxy = z_score_df.iloc[len(z_score_df)//2:]
        # print(f"Z PROXY: \n {z_proxy.to_string()}")
        #
        # z_mean_mechbench = z_mechbench.mean()
        # print(f"Z MECHBENCH MEAN: \n{z_mean_mechbench}")
        # z_mean_proxy = z_proxy.mean()
        # print(f"Z PROXY MEAN: \n{z_mean_proxy}")

        # NEW METHOD: Calculate Z-scores using MECHBench mean and std
        # mb_mean = self.mechbench_ela.mean()
        # mb_std = np.maximum(self.mechbench_ela.std(), 0.01)
        #
        # mb_std = mb_std.replace(0, 1.0)
        #
        # # Standardize both groups independently using the target's baseline metrics
        # z_mean_mechbench = (self.mechbench_ela.mean() - mb_mean)  # vector of 0s
        # z_mean_proxy = (proxy_ela_means - mb_mean)

        # print(f"Z MEAN MECHBENCH: \n{z_mean_mechbench}")
        # print(f"Z MEAN PROXY: \n{z_mean_proxy}")
        #
        # distance_series = (z_mean_mechbench - z_mean_proxy).abs()
        # print(f"DISTANCE SERIES: \n{distance_series}")
        # distance_series.name = "feature_distance"
        #
        # print(f"MECHBENCH SD: \n{mb_std}")
        #
        # # Standardize both groups independently using the target's baseline metrics
        # z_mean_mechbench = (self.mechbench_ela.mean() - mb_mean) / mb_std  # vector of 0s
        # z_mean_proxy = (proxy_ela_means - mb_mean) / mb_std
        #
        # print(f"Z MEAN MECHBENCH (WITH SD): \n{z_mean_mechbench}")
        # print(f"Z MEAN PROXY (WITH SD): \n{z_mean_proxy}")

        distance_series = (mechbench_ela_means - proxy_ela_means).abs()
        print(f"DISTANCE SERIES WITH SD: \n{distance_series}")
        distance_series.name = "feature_distance"

        # solution.add_metadata("MECHBench_mean_z", z_mean_mechbench.to_numpy())
        # solution.add_metadata("proxy_mean_z", z_mean_proxy.to_numpy())
        # solution.add_metadata("proxy_mean_z", distance_series.to_numpy())

        final_score = distance_series.mean()
        print(f"MEAN DISTANCE: \n{final_score}")
        solution.set_scores(
            final_score,  # Fitness
            feedback=f"{feedback}",
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
        'ela_level.mmce_qda_25',
        'ela_level.lda_qda_25'
    ]

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

    ela_mechbench = pd.read_csv(
        "C:/Users/foppe/Documents/DSAI-3/Thesis/thesis_code/Folder_Points/ELA/problem_2_250D.csv", index_col=0)
    problem = ELAForMECHBench(mechbench_points=points,
                              mechbench_objective_values=objective_values,
                              mechbench_ela=ela_mechbench,
                              features=features)

    mutation_prompts = []
    for feature in problem.features:
        mutation_prompts.append(
            f"Create a new landscape class based on the selected code and improve the {feature} score, meaning: ELA feature {feature} {problem.feature_descriptions[feature]}.")
    mutation_prompts.append(
        "Create a new landscape class that is completely different from the selected solution but still adheres to the properties outlined in the task description.")

    ai_model = "qwen3-coder:30b"
    llm = Ollama_LLM(ai_model)

    role_prompt = "You are a highly skilled computer scientist in the field optimization and benchmarking."

    for experiment_i in [1]:
        es = LLaMEA(
            f=problem.evaluate_for_MECHBench,
            minimization=True,  # IMPORTANT: Distance should be minimized (0 is best)
            role_prompt=role_prompt,
            n_parents=16,
            n_offspring=8,
            llm=llm,
            task_prompt=problem.task_prompt,
            example_prompt=problem.example_prompt,
            output_format_prompt=problem.format_prompt,
            mutation_prompts=mutation_prompts,
            experiment_name=experiment_name,
            elitism=False,
            HPO=False,
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
        'ela_level.mmce_qda_25',
        'ela_level.lda_qda_25'
    ]

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

    efm = ELAForMECHBench(points, objective_values, ela_df, features)
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
