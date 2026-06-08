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
    def __init__(self, problem_type, size, features):
        super().__init__()
        data_path = "../Folder_Points/500D"
        if problem_type == 1:
            abs_path = os.path.abspath(data_path + "/data_p1")
            dim = 5
        elif problem_type == 2:
            abs_path = os.path.abspath(data_path + "/data_p2")
            dim = 5
        elif problem_type == 3:
            abs_path = os.path.abspath(data_path + "/data_p3")
            dim = 15
        else:
            print('Please enter a valid problem type (1, 2 or 3)')
            sys.exit(1)

        points_df = pd.read_csv(f"{abs_path}/points/{size}d{dim}_p{problem_type}_seed1312.csv", index_col='id')
        self.X = points_df.iloc[:, :dim]  # x0-x4 for p1-2, x0-x14 for p3
        self.original_ela_df = pd.read_csv(f"{abs_path}/ELA/{size}d{dim}_p{problem_type}_seed1312_ela.csv", index_col='feature')

        # Min-max normalization on ELA values:
        self.ela_stats = pd.read_csv("../ela_feature_stats.csv")
        stats_filtered = self.ela_stats[(self.ela_stats['dimension'] == 5) & (self.ela_stats['dataset'] == 'BBOB_SM_all')]
        merged_df = pd.merge(self.original_ela_df, stats_filtered[['feature', 'min', 'max']], on='feature', how='left')

        # If value > max or value < min, make them the new max/min
        merged_df['min'] = np.minimum(merged_df['min'], merged_df['value'])
        merged_df['max'] = np.maximum(merged_df['max'], merged_df['value'])

        denominator = merged_df['max'] - merged_df['min']
        denominator = denominator.replace(0, np.nan)
        merged_df['normalized_value'] = (merged_df['value'] - merged_df['min']) / denominator
        merged_df['normalized_value'] = merged_df['normalized_value'].fillna(0.0)
        self.original_ela_df = merged_df[['feature', 'normalized_value']].rename(columns={'normalized_value': 'value'})

        self.original_ela_df.set_index('feature', inplace=True)

        self.features = features
        self.feature_descriptions = {
            'disp.ratio_mean_02': f"should approach the value {self.original_ela_df.loc['disp.ratio_mean_02', 'value']: .3f}. Explanation: From pflacco's calculate_dispersion['disp.ratio_mean_02']: The dispersion features compare the dispersion, i.e. the (aggregated) pairwise distances, of all points in the initial design with the dispersion among the best points in the initial design. Per default, this set of “best points” is based on the 2%, 5% and 10% quantile of the objectives. Those dispersions are then compared based on the ratio as well as on the difference. [ratio, diff]_[mean, median]_[02, 05, 10, 25]: ratio and difference of the mean / median distances of the distances of the ‘best’ objectives vs. ‘all’ objectives. Taken from https://pflacco.readthedocs.io/en/latest/dispersion.html.",
            'ela_distr.skewness': f"should approach the value {self.original_ela_df.loc['ela_distr.skewness', 'value']: .3f}. Explanation: From pflacco's calculate_ela_distribution['ela_distr.skewness']: skewness of the objective values.",
            'ela_meta.lin_simple.adj_r2': f"should approach the value {self.original_ela_df.loc['ela_meta.lin_simple.adj_r2', 'value']: .3f}. Explanation: From pflacco's calculate_ela_meta['ela_meta.lin_simple.adj_r2']: 'Meta-Model: Linear and quadratic regression models with or without interactions are fitted to the initial data D. The adjusted coefficient of determination R2 is returned in each case as an indicator for model accuracy. Functions with variable scaling will not allow a good fit of regression models without interaction effects, and simple unimodal functions might be approximated by using a quadratic model. In addition, features are extracted which reflect the size relations of the model coefficients.' (Mersmann et al., 2011) lin_simple.adj_r2: adjusted R^2 (i.e. model fit) of a simple linear model.",
            'ela_meta.lin_simple.intercept': f"should approach the value {self.original_ela_df.loc['ela_meta.lin_simple.intercept', 'value']: .3f}. Explanation: From pflacco's calculate_ela_meta['ela_meta.lin_simple.intercept']: 'Meta-Model: Linear and quadratic regression models with or without interactions are fitted to the initial data D. The adjusted coefficient of determination R2 is returned in each case as an indicator for model accuracy. Functions with variable scaling will not allow a good fit of regression models without interaction effects, and simple unimodal functions might be approximated by using a quadratic model. In addition, features are extracted which reflect the size relations of the model coefficients.' (Mersmann et al., 2011) 'ela_meta.lin_simple.intercept': intercept of a simple linear model.",
            'ela_meta.lin_simple.coef.max': f"should approach the value {self.original_ela_df.loc['ela_meta.lin_simple.coef.max', 'value']: .3f}. Explanation: From pflacco's calculate_ela_meta['ela_meta.lin_simple.coef.max']: 'Meta-Model: Linear and quadratic regression models with or without interactions are fitted to the initial data D. The adjusted coefficient of determination R2 is returned in each case as an indicator for model accuracy. Functions with variable scaling will not allow a good fit of regression models without interaction effects, and simple unimodal functions might be approximated by using a quadratic model. In addition, features are extracted which reflect the size relations of the model coefficients.' (Mersmann et al., 2011) 'ela_meta.lin_simple.coef.max': biggest (non-intercept) absolute coefficient of the simple linear model.",
            'ela_meta.quad_simple.adj_r2': f"should approach the value {self.original_ela_df.loc['ela_meta.quad_simple.adj_r2', 'value']: .3f}. Explanation: From pflacco's calculate_ela_meta['ela_meta.quad_simple.adj_r2']: 'Meta-Model: Linear and quadratic regression models with or without interactions are fitted to the initial data D. The adjusted coefficient of determination R2 is returned in each case as an indicator for model accuracy. Functions with variable scaling will not allow a good fit of regression models without interaction effects, and simple unimodal functions might be approximated by using a quadratic model. In addition, features are extracted which reflect the size relations of the model coefficients.' (Mersmann et al., 2011) 'ela_meta.quad_simple.adj_r2': adjusted R^2 (i.e. model fit) of a simple quadratic model (without interactions), i.e. the ratio of its (absolute) biggest and smallest coefficients.",
            'ic.eps_ratio': f"should approach the value {self.original_ela_df.loc['ic.eps_ratio', 'value']: .3f}. Explanation: From pflacco's calculate_information_content['ic.eps_ratio']: Computes features based on the Information Content of Fitness Sequences (ICoFiS) approach (Munoz et al., 2014). In this approach, the information content of a continuous landscape, i.e. smoothness, ruggedness, or neutrality, are quantified. A neutral landscape has low IC, while a rugged landscape has high IC (Munoz et al., 2014). 'ic.eps_ratio': ratio of partial information sensitivity, cf. equation (8) in Munoz et al. (2014) where the ratio is 0.5.",
            'ic.eps_s': f"should approach the value {self.original_ela_df.loc['ic.eps_s', 'value']: .3f}. Explanation: From pflacco's calculate_information_content['ic.eps_s']: Computes features based on the Information Content of Fitness Sequences (ICoFiS) approach (Munoz et al., 2014). In this approach, the information content of a continuous landscape, i.e. smoothness, ruggedness, or neutrality, are quantified. A neutral landscape has low IC, while a rugged landscape has high IC (Munoz et al., 2014). 'ic.eps_s': settling sensitivity, indicating the epsilon for which the sequence nearly consists of zeros only, cf. equation (6) in Munoz et al. (2014).",
            'nbc.nb_fitness.cor': f"should approach the value {self.original_ela_df.loc['nbc.nb_fitness.cor', 'value']: .3f}. Explanation: From pflacco's calculate_nbc['nbc.nb_fitness.cor']: Nearest Better Clustering features. Computes features based on the comparison of nearest neighbour and nearest better neighbour, i.e., the nearest neighbor with a better performance / objective value value. nb_fitness.cor: correlation between fitness value and count of observations to whom the current observation is the nearest better neighbour (the so-called 'indegree').",
            # 'pca.expl_var_PC1.cov_init': f"should approach the value {self.original_ela_df.loc['pca.expl_var_PC1.cov_init', 'value']: .3f}. Explanation: From pflacco's calculate_pca['pca.expl_var_PC1.cov_init']: Principal component (analysis) features. expl_var_PC1.cov_init: proportion of variance, which is explained by the first principal component when applying PCA to the covariance matrix of the entire initial design.",
            'ela_level.mmce_qda_25': f"should approach the value {self.original_ela_df.loc['ela_level.mmce_qda_25', 'value']: .3f}. Explanation: From pflacco's calculate_ela_level['ela_level.mmce_qda_25']: 'The initial data set D is split into two classes by a specific objective level which works as a threshold. One possibility is to use the median for this, which will result in equally sized classes. Other choices studied are the upper and lower quartiles of the distribution of y. Linear (LDA), quadratic (QDA) and mixture discriminant analysis (MDA) are used to predict whether the objective values Y fall below or exceed the calculated threshold. Multi-modal functions should result in several unconnected sublevel sets for the quantile of lower values, which can only be modeled by MDA, but not LDA or QDA. The extracted low-level features are based on the distribution of the resulting cross-validated mean misclassification errors of each classifier.' (Mersmann et al., 2011) 'ela_level.mmce_qda_25': mean misclassification error of quadratic discriminant analysis (QDA) in the lower quartile (25).",
            'ela_level.lda_qda_25': f"should approach the value {self.original_ela_df.loc['ela_level.lda_qda_25', 'value']: .3f}. Explanation: From pflacco's calculate_ela_level['ela_level.lda_qda_25']: 'The initial data set D is split into two classes by a specific objective level which works as a threshold. One possibility is to use the median for this, which will result in equally sized classes. Other choices studied are the upper and lower quartiles of the distribution of y. Linear (LDA), quadratic (QDA) and mixture discriminant analysis (MDA) are used to predict whether the objective values Y fall below or exceed the calculated threshold. Multi-modal functions should result in several unconnected sublevel sets for the quantile of lower values, which can only be modeled by MDA, but not LDA or QDA. The extracted low-level features are based on the distribution of the resulting cross-validated mean misclassification errors of each classifier.' (Mersmann et al., 2011) 'ela_level.lda_qda_25': mean misclassification error of linear discriminant analysis (QDA) in the lower quartile (25)."
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
        proxy_instance = proxy_class(dim=5)
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
            # Scale y (X should already be scaled before!)
            y_scaled = (y - y.min()) / (y.max() - y.min())

        ela_proxy = self.compute_ela(self.X, y_scaled)
        ela_proxy = pd.Series(ela_proxy)
        ela_proxy = ela_proxy.reset_index()
        ela_proxy.columns = ['feature', 'value']

        # Min-max normalization on ELA values:
        stats_filtered = self.ela_stats[(self.ela_stats['dimension'] == 5) & (self.ela_stats['dataset'] == 'BBOB_SM_all')]
        merged_df = pd.merge(ela_proxy, stats_filtered[['feature', 'min', 'max']], on='feature', how='left')
        denominator = merged_df['max'] - merged_df['min']
        denominator = denominator.replace(0, np.nan)
        merged_df['normalized_value'] = (merged_df['value'] - merged_df['min']) / denominator
        merged_df['normalized_value'] = merged_df['normalized_value'].fillna(0.0)
        ela_proxy = merged_df[['feature', 'normalized_value']].rename(columns={'normalized_value': 'value'})

        # ela_per_seed = preprocces_data(ela_per_seed)
        ela_proxy.index.name = 'feature'
        ela_proxy.name = 'value'
        ela_proxy.set_index('feature', inplace=True)

        solution.add_metadata("Proxy ELA values", ela_proxy.to_numpy())
        solution.add_metadata("Original ELA values", self.original_ela_df.to_numpy())

        print(f"ORIGINAL ELA: \n{self.original_ela_df.to_string()}")
        print(f"PROXY ELA: \n{ela_proxy.to_string()}")

        feedback = f"The optimization landscape '{proxy_name}' had the following distances to the original ELA values: "
        for i in range(len(ela_proxy)):
            # Grab the feature name from the index
            feature_name = ela_proxy.index[i]

            # Grab the actual scalar float values from column 0 ('value')
            proxy_val = ela_proxy.iloc[i, 0]
            original_val = self.original_ela_df.iloc[i, 0]

            # This is now a simple float subtraction!
            pairwise_distance = proxy_val - original_val

            solution.add_metadata(f"Distance to {feature_name}", round(pairwise_distance, 3))
            feedback += f"{feature_name}: {pairwise_distance: .3f} (Original value: {original_val: .3f}, proxy value: {proxy_val: .3f}) \n"
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

        distance_series = (self.original_ela_df - ela_proxy).abs()
        print(f"DISTANCE SERIES: \n{distance_series}")
        distance_series.name = "feature_distance"

        # solution.add_metadata("MECHBench_mean_z", z_mean_mechbench.to_numpy())
        # solution.add_metadata("proxy_mean_z", z_mean_proxy.to_numpy())
        # solution.add_metadata("proxy_mean_z", distance_series.to_numpy())

        final_score = distance_series['value'].mean()
        solution.add_metadata("Raw mean distance", final_score)

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
        # 'pca.expl_var_PC1.cov_init',
        'ela_level.mmce_qda_25',
        'ela_level.lda_qda_25'
    ]

    problem = ELAForMECHBench(problem_type=2,  # <-- EDIT: problem type (1, 2 or 3)
                              size=500,  # <-- EDIT: dataset size (30, 60, 125, 250 or 500)
                              features=features)

    mutation_prompts = []
    for feature in features:
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
            max_workers=4,
            budget=400,
            parallel_backend="loky",
            niching="sharing",
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
