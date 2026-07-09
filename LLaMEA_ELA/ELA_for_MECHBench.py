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
        # self.feature_descriptions = {
        #     'disp.ratio_mean_02': f"should approach the value {self.original_ela_df.loc['disp.ratio_mean_02', 'value']: .3f}. Explanation: From pflacco's calculate_dispersion['disp.ratio_mean_02']: The dispersion features compare the dispersion, i.e. the (aggregated) pairwise distances, of all points in the initial design with the dispersion among the best points in the initial design. Per default, this set of “best points” is based on the 2%, 5% and 10% quantile of the objectives. Those dispersions are then compared based on the ratio as well as on the difference. [ratio, diff]_[mean, median]_[02, 05, 10, 25]: ratio and difference of the mean / median distances of the distances of the ‘best’ objectives vs. ‘all’ objectives. Taken from https://pflacco.readthedocs.io/en/latest/dispersion.html.",
        #     'ela_distr.skewness': f"should approach the value {self.original_ela_df.loc['ela_distr.skewness', 'value']: .3f}. Explanation: From pflacco's calculate_ela_distribution['ela_distr.skewness']: skewness of the objective values.",
        #     'ela_meta.lin_simple.adj_r2': f"should approach the value {self.original_ela_df.loc['ela_meta.lin_simple.adj_r2', 'value']: .3f}. Explanation: From pflacco's calculate_ela_meta['ela_meta.lin_simple.adj_r2']: 'Meta-Model: Linear and quadratic regression models with or without interactions are fitted to the initial data D. The adjusted coefficient of determination R2 is returned in each case as an indicator for model accuracy. Functions with variable scaling will not allow a good fit of regression models without interaction effects, and simple unimodal functions might be approximated by using a quadratic model. In addition, features are extracted which reflect the size relations of the model coefficients.' (Mersmann et al., 2011) lin_simple.adj_r2: adjusted R^2 (i.e. model fit) of a simple linear model.",
        #     'ela_meta.lin_simple.intercept': f"should approach the value {self.original_ela_df.loc['ela_meta.lin_simple.intercept', 'value']: .3f}. Explanation: From pflacco's calculate_ela_meta['ela_meta.lin_simple.intercept']: 'Meta-Model: Linear and quadratic regression models with or without interactions are fitted to the initial data D. The adjusted coefficient of determination R2 is returned in each case as an indicator for model accuracy. Functions with variable scaling will not allow a good fit of regression models without interaction effects, and simple unimodal functions might be approximated by using a quadratic model. In addition, features are extracted which reflect the size relations of the model coefficients.' (Mersmann et al., 2011) 'ela_meta.lin_simple.intercept': intercept of a simple linear model.",
        #     'ela_meta.lin_simple.coef.max': f"should approach the value {self.original_ela_df.loc['ela_meta.lin_simple.coef.max', 'value']: .3f}. Explanation: From pflacco's calculate_ela_meta['ela_meta.lin_simple.coef.max']: 'Meta-Model: Linear and quadratic regression models with or without interactions are fitted to the initial data D. The adjusted coefficient of determination R2 is returned in each case as an indicator for model accuracy. Functions with variable scaling will not allow a good fit of regression models without interaction effects, and simple unimodal functions might be approximated by using a quadratic model. In addition, features are extracted which reflect the size relations of the model coefficients.' (Mersmann et al., 2011) 'ela_meta.lin_simple.coef.max': biggest (non-intercept) absolute coefficient of the simple linear model.",
        #     'ela_meta.quad_simple.adj_r2': f"should approach the value {self.original_ela_df.loc['ela_meta.quad_simple.adj_r2', 'value']: .3f}. Explanation: From pflacco's calculate_ela_meta['ela_meta.quad_simple.adj_r2']: 'Meta-Model: Linear and quadratic regression models with or without interactions are fitted to the initial data D. The adjusted coefficient of determination R2 is returned in each case as an indicator for model accuracy. Functions with variable scaling will not allow a good fit of regression models without interaction effects, and simple unimodal functions might be approximated by using a quadratic model. In addition, features are extracted which reflect the size relations of the model coefficients.' (Mersmann et al., 2011) 'ela_meta.quad_simple.adj_r2': adjusted R^2 (i.e. model fit) of a simple quadratic model (without interactions), i.e. the ratio of its (absolute) biggest and smallest coefficients.",
        #     'ic.eps_ratio': f"should approach the value {self.original_ela_df.loc['ic.eps_ratio', 'value']: .3f}. Explanation: From pflacco's calculate_information_content['ic.eps_ratio']: Computes features based on the Information Content of Fitness Sequences (ICoFiS) approach (Munoz et al., 2014). In this approach, the information content of a continuous landscape, i.e. smoothness, ruggedness, or neutrality, are quantified. A neutral landscape has low IC, while a rugged landscape has high IC (Munoz et al., 2014). 'ic.eps_ratio': ratio of partial information sensitivity, cf. equation (8) in Munoz et al. (2014) where the ratio is 0.5.",
        #     'ic.eps_s': f"should approach the value {self.original_ela_df.loc['ic.eps_s', 'value']: .3f}. Explanation: From pflacco's calculate_information_content['ic.eps_s']: Computes features based on the Information Content of Fitness Sequences (ICoFiS) approach (Munoz et al., 2014). In this approach, the information content of a continuous landscape, i.e. smoothness, ruggedness, or neutrality, are quantified. A neutral landscape has low IC, while a rugged landscape has high IC (Munoz et al., 2014). 'ic.eps_s': settling sensitivity, indicating the epsilon for which the sequence nearly consists of zeros only, cf. equation (6) in Munoz et al. (2014).",
        #     'nbc.nb_fitness.cor': f"should approach the value {self.original_ela_df.loc['nbc.nb_fitness.cor', 'value']: .3f}. Explanation: From pflacco's calculate_nbc['nbc.nb_fitness.cor']: Nearest Better Clustering features. Computes features based on the comparison of nearest neighbour and nearest better neighbour, i.e., the nearest neighbor with a better performance / objective value value. nb_fitness.cor: correlation between fitness value and count of observations to whom the current observation is the nearest better neighbour (the so-called 'indegree').",
        #     'ela_level.mmce_qda_25': f"should approach the value {self.original_ela_df.loc['ela_level.mmce_qda_25', 'value']: .3f}. Explanation: From pflacco's calculate_ela_level['ela_level.mmce_qda_25']: 'The initial data set D is split into two classes by a specific objective level which works as a threshold. One possibility is to use the median for this, which will result in equally sized classes. Other choices studied are the upper and lower quartiles of the distribution of y. Linear (LDA), quadratic (QDA) and mixture discriminant analysis (MDA) are used to predict whether the objective values Y fall below or exceed the calculated threshold. Multi-modal functions should result in several unconnected sublevel sets for the quantile of lower values, which can only be modeled by MDA, but not LDA or QDA. The extracted low-level features are based on the distribution of the resulting cross-validated mean misclassification errors of each classifier.' (Mersmann et al., 2011) 'ela_level.mmce_qda_25': mean misclassification error of quadratic discriminant analysis (QDA) in the lower quartile (25).",
        #     'ela_level.lda_qda_25': f"should approach the value {self.original_ela_df.loc['ela_level.lda_qda_25', 'value']: .3f}. Explanation: From pflacco's calculate_ela_level['ela_level.lda_qda_25']: 'The initial data set D is split into two classes by a specific objective level which works as a threshold. One possibility is to use the median for this, which will result in equally sized classes. Other choices studied are the upper and lower quartiles of the distribution of y. Linear (LDA), quadratic (QDA) and mixture discriminant analysis (MDA) are used to predict whether the objective values Y fall below or exceed the calculated threshold. Multi-modal functions should result in several unconnected sublevel sets for the quantile of lower values, which can only be modeled by MDA, but not LDA or QDA. The extracted low-level features are based on the distribution of the resulting cross-validated mean misclassification errors of each classifier.' (Mersmann et al., 2011) 'ela_level.lda_qda_25': mean misclassification error of linear discriminant analysis (QDA) in the lower quartile (25)."
        # }

        # self.mutations = {}
        # # NEW: Instead of random mutation, mutate only to update the worst-performing feature.
        # for feature in self.features:
        #     self.mutations[feature] = f"""
        #     Create a new landscape class based on the selected code and improve the {feature} score, meaning: ELA feature {feature} {self.feature_descriptions[feature]}.
        #     """

        # OLD: Random mutations
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

        # for feature in self.features:
        #     self.task_prompt += f"ELA feature {feature} {self.feature_descriptions[feature]}"
        # self.task_prompt += """
        # The class should also have a __init__(dim) function, that received the number of dimensions for the function.
        # The function will be evaluated between per dimension lower bound of -5.0 and upper bound of 5.0.
        # """

        self.example_proxy1 = f"""
        The previous loop resulted in the following code as the best proxy function, with fitness (i.e. distance to original ELA vector) of 0.234:
        
import numpy as np\n\nclass landscape:\n    \n    def __init__(self, dim=5):\n        self.dim = dim\n\n    def f(self, x):\n        # Normalize input to [-1, 1] for easier handling\n        x_norm = x / 5.0\n        \n        # Global quadratic basin - creates the smooth global structure\n        quadratic_term = np.sum(x_norm**2)\n        \n        # Radial basis function components to create multiple well-separated local minima\n        rb_term = 0.0\n        centers = np.linspace(-0.8, 0.8, 12)  # More centers for better clustering structure\n        for i in range(len(centers)):\n            for j in range(self.dim):\n                rb_term += 0.3 * np.exp(-15 * (x_norm[j] - centers[i%len(centers)])**2)\n        \n        # Harmonic perturbations to control skewness and dispersion\n        harmonic_term = 0.0\n        for i in range(self.dim):\n            harmonic_term += 0.6 * np.sin(3 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i])\n            harmonic_term += 0.4 * np.sin(5 * np.pi * x_norm[i]) * np.sin(3 * np.pi * x_norm[i])\n            harmonic_term += 0.3 * np.sin(7 * np.pi * x_norm[i]) * np.cos(4 * np.pi * x_norm[i])\n        \n        # Additional harmonic terms to control linear model coefficients and quadratic fit\n        additional_harmonic = 0.0\n        for i in range(self.dim):\n            additional_harmonic += 0.2 * np.sin(2 * np.pi * x_norm[i]) * np.cos(1.5 * np.pi * x_norm[i])\n            additional_harmonic += 0.15 * np.sin(4 * np.pi * x_norm[i]) * np.sin(2.5 * np.pi * x_norm[i])\n        \n        # Enhanced quadratic structure to improve quad_simple.adj_r2\n        # Add terms that specifically improve the ratio of max to min coefficients in quadratic models\n        quadratic_improvement = 0.0\n        for i in range(self.dim):\n            quadratic_improvement += 0.3 * x_norm[i]**2\n            quadratic_improvement += 0.08 * x_norm[i]**4  # Higher order term to influence quadratic fit\n            quadratic_improvement += 0.03 * x_norm[i]**6\n        \n        # Cross-dimensional interaction terms to improve model fit characteristics\n        cross_term = 0.0\n        for i in range(self.dim):\n            for j in range(i+1, min(i+4, self.dim)):  # More cross-terms for better interaction\n                cross_term += 0.15 * x_norm[i] * x_norm[j] * np.sin(np.pi * (x_norm[i] + x_norm[j]))\n        \n        # Skewness control term - increased cubic and higher order terms to achieve target skewness\n        skew_term = 0.0\n        for i in range(self.dim):\n            skew_term += 0.15 * x_norm[i]**3  # Increased cubic term for skewness\n            skew_term += 0.05 * x_norm[i]**5  # Fifth order term for additional skewness\n            skew_term += 0.02 * x_norm[i]**7  # Seventh order term for more pronounced skewness\n        \n        # Ruggedness enhancement to increase information content\n        ruggedness_term = 0.0\n        for i in range(self.dim):\n            ruggedness_term += 0.4 * np.sin(12 * np.pi * x_norm[i]) * np.cos(10 * np.pi * x_norm[i])\n            ruggedness_term += 0.25 * np.sin(18 * np.pi * x_norm[i]) * np.sin(15 * np.pi * x_norm[i])\n        \n        # Additional terms to specifically improve nearest better clustering properties\n        clustering_term = 0.0\n        # Add structure that creates more uniform distribution of better neighbors\n        for i in range(self.dim):\n            clustering_term += 0.1 * np.sin(6 * np.pi * x_norm[i]) * np.cos(4 * np.pi * x_norm[i])\n            clustering_term += 0.05 * np.sin(8 * np.pi * x_norm[i]) * np.sin(6 * np.pi * x_norm[i])\n            clustering_term += 0.08 * np.cos(5 * np.pi * x_norm[i]) * np.sin(3 * np.pi * x_norm[i])\n        \n        # Combine all terms with appropriate scaling\n        result = 0.7 * quadratic_term + 1.2 * rb_term + 0.6 * harmonic_term + 0.4 * additional_harmonic + 0.3 * cross_term + 0.5 * skew_term + 0.5 * ruggedness_term + 0.3 * quadratic_improvement + 0.2 * clustering_term\n        \n        # Add offset to control intercept\n        result += 0.744\n        \n        return result

The worst-performing feature is ela_meta.lin_simple.coef.max:
Original value: 0.3047 (1.0 after min-max normalization)
Proxy value: 0.0402 (0.1306 after min-max normalization)
Distance: -0.2645 (-0.869 after min-max normalization)

Please adjust the above code to improve the ela_meta.lin_simple.coef.max value (i.e. approach 0.3047 as much as possible), while trying to keep all other features the same.
        """
        self.example_proxy2 = f"""
        The previous loop resulted in the following code as the best proxy function, with fitness (i.e. distance to original ELA vector) of 0.242:
        
import numpy as np\n\nclass landscape:\n    \n    def __init__(self, dim=5):\n        self.dim = dim\n\n    def f(self, x):\n        # Normalize input to [-1, 1] range\n        x_norm = x / 5.0\n        \n        # Central quadratic basin - main attraction\n        quadratic = np.sum(x_norm**2)\n        \n        # Radial distance from center\n        r = np.sqrt(np.sum(x_norm**2))\n        \n        # Create multiple overlapping radial basis functions for high ruggedness\n        radial_basis = 0\n        for i in range(0, self.dim, 2):\n            if i+1 < self.dim:\n                # Multiple overlapping radial components\n                radial_basis += 0.5 * np.exp(-5 * (r - 0.3)**2) * np.sin(10 * np.pi * x_norm[i]) * np.cos(8 * np.pi * x_norm[i+1])\n                radial_basis += 0.3 * np.exp(-3 * (r - 0.7)**2) * np.cos(12 * np.pi * x_norm[i]) * np.sin(10 * np.pi * x_norm[i+1])\n                radial_basis += 0.4 * np.exp(-4 * (r - 0.5)**2) * np.sin(15 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i+1])\n        \n        # Add more complex local structure to increase multimodality and ruggedness\n        local_terms = 0\n        for i in range(self.dim):\n            local_terms += 0.8 * np.sin(15 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i])\n            local_terms += 0.6 * np.sin(20 * np.pi * x_norm[i]) * np.cos(18 * np.pi * x_norm[i])\n            \n        # Add radial sinusoidal modulation with enhanced multi-modality\n        radial_modulation = 0\n        for i in range(self.dim):\n            radial_term = np.sin(8 * np.pi * r) * np.cos(6 * np.pi * r)\n            radial_term *= (1.0 + 0.7 * np.sin(6 * np.pi * x_norm[i]))\n            radial_modulation += radial_term\n            \n        # Add exponentially decaying radial components to control information content\n        exp_decay = 0\n        for i in range(self.dim):\n            # Enhanced exponential decay to increase ruggedness and information content\n            exp_decay += 0.5 * np.exp(-5 * r) * np.sin(10 * np.pi * x_norm[i])\n            \n        # Add cross-dimensional interaction terms for meta-model fit\n        interaction_terms = 0\n        for i in range(self.dim):\n            for j in range(i+1, min(i+3, self.dim)):  # Limited interactions\n                interaction_terms += 0.4 * x_norm[i] * x_norm[j] * (1 + 0.5 * r)\n                \n        # Add noise component to control dispersion and skewness\n        noise = 0.2 * np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm))\n        \n        # Combine all terms with appropriate scaling\n        result = 0.4 * quadratic + 0.6 * radial_modulation + 0.4 * exp_decay + local_terms + radial_basis + interaction_terms + noise\n        \n        # Apply radial scaling to control the landscape properties\n        radial_scaling = 1.0 + 0.4 * np.exp(-r**2)\n        result *= radial_scaling\n        \n        # Add specific terms to enhance disp.ratio_mean_02 (dispersion properties)\n        # Introduce more pronounced ruggedness in the middle range of the landscape\n        ruggedness = 0\n        for i in range(self.dim):\n            ruggedness += 0.5 * np.sin(15 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i])\n            ruggedness += 0.4 * np.sin(20 * np.pi * x_norm[i]) * np.cos(18 * np.pi * x_norm[i])\n            ruggedness += 0.3 * np.sin(25 * np.pi * x_norm[i]) * np.cos(22 * np.pi * x_norm[i])\n            \n        # Combine with radial components to enhance information content\n        result += 0.3 * ruggedness * (1.0 - r**2)\n        \n        # Add stronger linear terms to increase max coefficient\n        linear_terms = 0\n        for i in range(self.dim):\n            linear_terms += 0.5 * x_norm[i]\n            \n        # Add even stronger cross-dimensional linear terms\n        for i in range(self.dim):\n            for j in range(i+1, min(i+2, self.dim)):\n                linear_terms += 0.4 * x_norm[i] * x_norm[j]\n                \n        result += linear_terms\n        \n        # Adjust the global offset to control the linear model intercept\n        result += 0.380\n        \n        # Adjust to ensure the minimum value is at the origin\n        result -= 0.380\n        \n        # Add specific enhancement for information content (ic.eps_ratio)\n        # Add a term that increases the landscape's ruggedness and information content\n        info_content = 0\n        for i in range(self.dim):\n            # Create more pronounced peaks and valleys for higher information content\n            info_content += 0.3 * np.sin(15 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i])\n            info_content += 0.2 * np.sin(20 * np.pi * x_norm[i]) * np.cos(18 * np.pi * x_norm[i])\n            info_content += 0.15 * np.sin(25 * np.pi * x_norm[i]) * np.cos(22 * np.pi * x_norm[i])\n            \n        # Apply information content enhancement\n        result += 0.2 * info_content * np.exp(-0.5 * r**2)\n        \n        # Add additional high-frequency modulation to increase information content\n        high_freq = 0\n        for i in range(self.dim):\n            high_freq += 0.25 * np.sin(25 * np.pi * x_norm[i]) * np.cos(22 * np.pi * x_norm[i])\n            high_freq += 0.2 * np.sin(30 * np.pi * x_norm[i]) * np.cos(27 * np.pi * x_norm[i])\n            \n        result += 0.15 * high_freq * (1.0 - r**2)\n        \n        # Add specific dispersion control terms\n        # Create more evenly distributed objective values to improve disp.ratio_mean_02\n        dispersion_control = 0\n        for i in range(self.dim):\n            # Add terms that create better spread of values\n            dispersion_control += 0.15 * np.sin(8 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[i])\n            dispersion_control += 0.1 * np.sin(12 * np.pi * x_norm[i]) * np.cos(10 * np.pi * x_norm[i])\n            \n        # Add stronger dispersion control component specifically for disp.ratio_mean_02\n        dispersion_component = 0.25 * dispersion_control * (1.0 - r**2)\n        result += dispersion_component\n        \n        # Add radial terms that create more uniform distribution of points\n        radial_distribution = 0\n        for i in range(self.dim):\n            radial_distribution += 0.08 * np.sin(4 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])\n            radial_distribution += 0.05 * np.sin(6 * np.pi * x_norm[i]) * np.cos(5 * np.pi * x_norm[i])\n            \n        result += 0.08 * radial_distribution * (1.0 - r**2)\n        \n        # Add specific enhancement for disp.ratio_mean_02 through strategic fitness value distribution\n        # Create a landscape with controlled fitness value clustering and spread\n        fitness_spread = 0\n        for i in range(self.dim):\n            fitness_spread += 0.3 * np.sin(18 * np.pi * x_norm[i]) * np.cos(15 * np.pi * x_norm[i])\n            fitness_spread += 0.2 * np.sin(22 * np.pi * x_norm[i]) * np.cos(19 * np.pi * x_norm[i])\n            \n        result += 0.25 * fitness_spread * np.exp(-0.3 * r**2)\n        \n        # Add additional ruggedness components specifically for increasing disp.ratio_mean_02\n        # Create more pronounced peaks and valleys that increase information content\n        additional_ruggedness = 0\n        for i in range(self.dim):\n            # Add high-frequency components that contribute to information content\n            additional_ruggedness += 0.2 * np.sin(30 * np.pi * x_norm[i]) * np.cos(25 * np.pi * x_norm[i])\n            additional_ruggedness += 0.15 * np.sin(35 * np.pi * x_norm[i]) * np.cos(30 * np.pi * x_norm[i])\n            additional_ruggedness += 0.1 * np.sin(40 * np.pi * x_norm[i]) * np.cos(35 * np.pi * x_norm[i])\n            \n        result += 0.1 * additional_ruggedness * (1.0 - r**2)\n        \n        # Add a strong radial component that increases information content\n        radial_ic = 0\n        for i in range(0, self.dim, 2):\n            if i+1 < self.dim:\n                radial_ic += 0.25 * np.sin(20 * np.pi * r) * np.cos(15 * np.pi * r) * np.sin(10 * np.pi * x_norm[i]) * np.cos(8 * np.pi * x_norm[i+1])\n                \n        result += 0.2 * radial_ic * (1.0 - r**2)\n        \n        # Add a strong component that increases the information content ratio\n        # This specifically targets the disp.ratio_mean_02 feature\n        disp_ratio_component = 0\n        for i in range(self.dim):\n            # Use higher frequency components to create more information content\n            disp_ratio_component += 0.3 * np.sin(25 * np.pi * x_norm[i]) * np.cos(20 * np.pi * x_norm[i])\n            disp_ratio_component += 0.25 * np.sin(30 * np.pi * x_norm[i]) * np.cos(25 * np.pi * x_norm[i])\n            disp_ratio_component += 0.2 * np.sin(35 * np.pi * x_norm[i]) * np.cos(30 * np.pi * x_norm[i])\n            \n        # Apply this to increase information content while maintaining other properties\n        result += 0.25 * disp_ratio_component * np.exp(-0.2 * r**2)\n        \n        # Add a final component that ensures high information content\n        final_ic_component = 0\n        for i in range(self.dim):\n            # Create a very rugged component that will increase disp.ratio_mean_02\n            final_ic_component += 0.4 * np.sin(40 * np.pi * x_norm[i]) * np.cos(35 * np.pi * x_norm[i])\n            final_ic_component += 0.3 * np.sin(45 * np.pi * x_norm[i]) * np.cos(40 * np.pi * x_norm[i])\n            \n        result += 0.3 * final_ic_component * (1.0 - r**2)\n        \n        # Add specific dispersion enhancement to directly target disp.ratio_mean_02\n        # This is the key addition to improve the dispersion ratio\n        disp_enhancement = 0\n        for i in range(self.dim):\n            # Add components that increase the spread of objective values\n            disp_enhancement += 0.2 * np.sin(18 * np.pi * x_norm[i]) * np.cos(15 * np.pi * x_norm[i])\n            disp_enhancement += 0.15 * np.sin(22 * np.pi * x_norm[i]) * np.cos(19 * np.pi * x_norm[i])\n            disp_enhancement += 0.1 * np.sin(26 * np.pi * x_norm[i]) * np.cos(23 * np.pi * x_norm[i])\n            \n        # Apply dispersion enhancement with radial scaling\n        result += 0.18 * disp_enhancement * (1.0 - r**2)\n        \n        # Add specific NBC enhancement to directly target nbc.nb_fitness.cor\n        # Create a landscape that improves the correlation between fitness values and indegree\n        nbc_enhancement = 0\n        for i in range(self.dim):\n            # Add terms that create better clustering of better fitness values\n            nbc_enhancement += 0.3 * np.sin(12 * np.pi * x_norm[i]) * np.cos(10 * np.pi * x_norm[i])\n            nbc_enhancement += 0.25 * np.sin(16 * np.pi * x_norm[i]) * np.cos(14 * np.pi * x_norm[i])\n            nbc_enhancement += 0.2 * np.sin(20 * np.pi * x_norm[i]) * np.cos(18 * np.pi * x_norm[i])\n            \n        # Apply NBC enhancement with radial scaling\n        result += 0.15 * nbc_enhancement * (1.0 - r**2)\n        \n        # Add additional terms to improve the correlation structure\n        correlation_terms = 0\n        for i in range(self.dim):\n            # Add terms that create better local clustering\n            correlation_terms += 0.1 * np.sin(25 * np.pi * x_norm[i]) * np.cos(22 * np.pi * x_norm[i])\n            correlation_terms += 0.08 * np.sin(30 * np.pi * x_norm[i]) * np.cos(27 * np.pi * x_norm[i])\n            \n        result += 0.1 * correlation_terms * np.exp(-0.3 * r**2)\n        \n        # Add terms that create more distinct fitness value ranges for better NBC properties\n        fitness_ranges = 0\n        for i in range(self.dim):\n            # Create distinct local minima that will improve indegree correlation\n            fitness_ranges += 0.2 * np.sin(10 * np.pi * x_norm[i]) * np.cos(8 * np.pi * x_norm[i])\n            fitness_ranges += 0.15 * np.sin(14 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i])\n            \n        result += 0.12 * fitness_ranges * (1.0 - r**2)\n        \n        # Add enhanced dispersion control specifically for disp.ratio_mean_02\n        # Create a more balanced distribution of objective values\n        enhanced_dispersion = 0\n        for i in range(self.dim):\n            # Add components that create a better spread of values to improve dispersion ratio\n            enhanced_dispersion += 0.3 * np.sin(16 * np.pi * x_norm[i]) * np.cos(13 * np.pi * x_norm[i])\n            enhanced_dispersion += 0.25 * np.sin(20 * np.pi * x_norm[i]) * np.cos(17 * np.pi * x_norm[i])\n            enhanced_dispersion += 0.2 * np.sin(24 * np.pi * x_norm[i]) * np.cos(21 * np.pi * x_norm[i])\n            \n        # Apply enhanced dispersion control\n        result += 0.2 * enhanced_dispersion * (1.0 - r**2)\n        \n        # Add radial components that create better separation between points\n        radial_separation = 0\n        for i in range(0, self.dim, 2):\n            if i+1 < self.dim:\n                radial_separation += 0.15 * np.sin(12 * np.pi * r) * np.cos(10 * np.pi * r) * np.sin(8 * np.pi * x_norm[i]) * np.cos(6 * np.pi * x_norm[i+1])\n                \n        result += 0.1 * radial_separation * (1.0 - r**2)\n        \n        # Add specific terms to increase the ratio between all-point and best-point distances\n        # This is key to achieving the target disp.ratio_mean_02 = 0.611\n        dispersion_ratio_terms = 0\n        for i in range(self.dim):\n            # Add terms that create a more uniform spread of values to increase the dispersion ratio\n            dispersion_ratio_terms += 0.2 * np.sin(22 * np.pi * x_norm[i]) * np.cos(19 * np.pi * x_norm[i])\n            dispersion_ratio_terms += 0.15 * np.sin(26 * np.pi * x_norm[i]) * np.cos(23 * np.pi * x_norm[i])\n            dispersion_ratio_terms += 0.1 * np.sin(30 * np.pi * x_norm[i]) * np.cos(27 * np.pi * x_norm[i])\n            \n        result += 0.18 * dispersion_ratio_terms * np.exp(-0.1 * r**2)\n        \n        # Add a component that specifically increases the overall spread of objective values\n        spread_enhancement = 0\n        for i in range(self.dim):\n            # Add terms that increase the variance of objective values\n            spread_enhancement += 0.25 * np.sin(28 * np.pi * x_norm[i]) * np.cos(25 * np.pi * x_norm[i])\n            spread_enhancement += 0.2 * np.sin(32 * np.pi * x_norm[i]) * np.cos(29 * np.pi * x_norm[i])\n            spread_enhancement += 0.15 * np.sin(36 * np.pi * x_norm[i]) * np.cos(33 * np.pi * x_norm[i])\n            \n        result += 0.22 * spread_enhancement * (1.0 - r**2)\n        \n        return result\n\n    def compute_indegree(self, X):\n        \"\"\"Compute indegree for NBC analysis\"\"\"\n        n = X.shape[0]\n        indegree = np.zeros(n)\n        \n        # For each point, count how many points have better fitness values\n        for i in range(n):\n            fitness_i = self.f(X[i])\n            count = 0\n            for j in range(n):\n                if i != j and self.f(X[j]) < fitness_i:\n                    count += 1\n            indegree[i] = count\n            \n        return indegree

The worst-performing feature is ela_meta.lin_simple.coef.max:
Original value: 0.0953 (0.8984 after min-max normalization)
Proxy value: 0.0027 (0.0213 after min-max normalization)
Distance: -0.0926 (-0.877 after min-max normalization)

Please adjust the above code to improve the ela_meta.lin_simple.coef.max value (i.e. approach 0.0953 as much as possible), while trying to keep all other features the same.
        """
        self.example_proxy3 = f"""
        The previous loop resulted in the following code as the best proxy function, with fitness (i.e. distance to original ELA vector) of 0.177:
        
import numpy as np\n\nclass landscape:\n    \n    def __init__(self, dim=5):\n        self.dim = dim\n\n    def f(self, x):\n        # Normalize input to [-1, 1] range for better control\n        x_norm = x / 5.0\n        \n        # Global quadratic basin - creates the main optimization landscape\n        quadratic = np.sum(x_norm**2)\n        \n        # Add multiple local minima using high-frequency sinusoidal modulation\n        # This creates a complex landscape with many local optima\n        sinusoidal = 0.0\n        for i in range(self.dim):\n            sinusoidal += np.sin(15 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i])\n        \n        # Add more local optima with varying frequencies to increase ruggedness\n        local_terms = 0.0\n        for i in range(self.dim):\n            local_terms += 0.5 * np.sin(20 * np.pi * x_norm[i]) * np.cos(18 * np.pi * x_norm[i])\n        \n        # Add a structured pattern to increase information content\n        structured_pattern = 0.0\n        for i in range(self.dim):\n            structured_pattern += 0.3 * np.sin(25 * np.pi * x_norm[i]) * np.cos(22 * np.pi * x_norm[i])\n        \n        # Add a periodic component to enhance ruggedness and information content\n        periodic_component = 0.0\n        for i in range(self.dim):\n            periodic_component += 0.2 * np.sin(30 * np.pi * x_norm[i]) * np.cos(28 * np.pi * x_norm[i])\n        \n        # Combine all terms with appropriate scaling\n        result = quadratic + 0.5 * sinusoidal + 0.3 * local_terms + 0.2 * structured_pattern + 0.1 * periodic_component\n        \n        # Add a constant offset to ensure global minimum is at the origin\n        result += 0.3 * np.sum(np.abs(x_norm))\n        \n        # Apply a transformation to adjust skewness and model fit characteristics\n        # Introduce skewness through asymmetric modification\n        skewness_factor = 1.0 + 0.2 * np.sin(np.sum(x_norm**3))\n        result = result * skewness_factor\n        \n        # Add a noise component to improve information content properties\n        noise = 0.001 * np.random.randn()\n        result += noise\n        \n        # Apply a transformation to better control the information content properties\n        # This helps in achieving the target ic.eps_s value of 1.000\n        result = result * (1.0 + 0.1 * np.sin(np.sum(x_norm**4)))\n        \n        # Add a specific scaling factor to enhance ruggedness and information content\n        # This is crucial for achieving high ic.eps_s values\n        ruggedness_factor = 1.0 + 0.2 * np.sin(35 * np.pi * np.sum(x_norm**2))\n        result = result * ruggedness_factor\n        \n        # Add additional multimodal structure to improve LDA/QDA classification properties\n        # This specifically targets the lda_qda_25 feature by creating more distinct clusters\n        multimodal_structure = 0.0\n        for i in range(self.dim):\n            # Add a specific pattern that creates more separated regions in the landscape\n            multimodal_structure += 0.4 * np.sin(40 * np.pi * x_norm[i]) * np.cos(38 * np.pi * x_norm[i])\n        \n        # Add the multimodal structure with careful scaling\n        result += 0.15 * multimodal_structure\n        \n        # Apply a transformation to specifically adjust the lda/qda classification properties\n        # This helps in achieving the target lda_qda_25 value of 0.125\n        result = result * (1.0 + 0.05 * np.sin(45 * np.pi * np.sum(x_norm**2)))\n        \n        # Increase the maximum coefficient by adding strong linear components\n        # This specifically targets the ela_meta.lin_simple.coef.max feature\n        linear_component = 0.0\n        for i in range(self.dim):\n            linear_component += 0.8 * x_norm[i]  # Strong linear component to increase max coef\n        \n        result += linear_component\n        \n        # Add a second strong linear component in different direction to further increase max coef\n        # This helps in achieving the target ela_meta.lin_simple.coef.max value of 0.432\n        linear_component2 = 0.0\n        for i in range(self.dim):\n            linear_component2 += 0.6 * x_norm[(i + 1) % self.dim]  # Rotated linear component\n        \n        result += linear_component2\n        \n        # Add a third strong linear component to maximize the coefficient\n        linear_component3 = 0.0\n        for i in range(self.dim):\n            linear_component3 += 0.5 * x_norm[(i + 2) % self.dim]  # Another rotated linear component\n        \n        result += linear_component3\n        \n        # Add a fourth strong linear component to maximize the coefficient\n        linear_component4 = 0.0\n        for i in range(self.dim):\n            linear_component4 += 0.432 * x_norm[(i + 3) % self.dim]  # This will be the maximum coefficient\n        \n        result += linear_component4\n        \n        # Add a fifth strong linear component to maximize the coefficient\n        linear_component5 = 0.0\n        for i in range(self.dim):\n            linear_component5 += 0.432 * x_norm[(i + 4) % self.dim]  # This will be the maximum coefficient\n        \n        result += linear_component5\n        \n        # Add a quadratic term to help with model fit characteristics\n        quadratic_term = 0.2 * np.sum(x_norm**2)\n        result += quadratic_term\n        \n        # Introduce skewness by adding asymmetric terms\n        asymmetric_term = 0.0\n        for i in range(self.dim):\n            asymmetric_term += 0.15 * np.sin(50 * np.pi * x_norm[i]) * np.cos(48 * np.pi * x_norm[i]) * np.abs(x_norm[i])\n        \n        result += asymmetric_term\n        \n        # Add a controlled amount of skewness to reach target value\n        skewness_control = 0.05 * np.sum(np.sin(60 * np.pi * x_norm**3))\n        result += skewness_control\n        \n        # Add specific clustering structure to improve nbc.nb_fitness.cor\n        # Create a pattern that encourages better neighbor relationships\n        clustering_pattern = 0.0\n        for i in range(self.dim):\n            clustering_pattern += 0.2 * np.sin(25 * np.pi * x_norm[i]) * np.cos(23 * np.pi * x_norm[i])\n        \n        result += 0.1 * clustering_pattern\n        \n        # Add a specific term to enhance the correlation between fitness values and indegree\n        # This helps in achieving the target nb_fitness.cor value of 0.416\n        correlation_term = 0.0\n        for i in range(self.dim):\n            correlation_term += 0.1 * np.sin(30 * np.pi * x_norm[i]) * np.cos(28 * np.pi * x_norm[i])\n        \n        result += 0.05 * correlation_term\n        \n        # Add a controlled amount of noise to help with the clustering properties\n        # This helps in achieving better correlation between fitness and indegree\n        noise_term = 0.02 * np.random.randn()\n        result += noise_term\n        \n        # Apply a specific transformation to increase skewness to target value\n        # This is the key modification to improve ela_distr.skewness\n        skewness_adjustment = 0.1 * np.sum(np.sin(70 * np.pi * x_norm**3))\n        result += skewness_adjustment\n        \n        # Add a controlled cubic term to further adjust skewness\n        cubic_term = 0.05 * np.sum(x_norm**3)\n        result += cubic_term\n        \n        # Add dispersion control term to specifically target disp.ratio_mean_02\n        # This is the key modification to improve disp.ratio_mean_02\n        dispersion_control = 0.0\n        for i in range(self.dim):\n            # Create a pattern that increases the ratio between best and all points dispersion\n            dispersion_control += 0.3 * np.sin(55 * np.pi * x_norm[i]) * np.cos(52 * np.pi * x_norm[i])\n        \n        result += 0.2 * dispersion_control\n        \n        # Add additional dispersion control through a multi-scale approach\n        multi_scale_dispersion = 0.0\n        for i in range(self.dim):\n            multi_scale_dispersion += 0.15 * np.sin(48 * np.pi * x_norm[i]) * np.cos(45 * np.pi * x_norm[i])\n        \n        result += 0.1 * multi_scale_dispersion\n        \n        # Add a term that specifically increases the distance between best and all points\n        # This helps in achieving the target disp.ratio_mean_02 value of 0.720\n        distance_ratio_term = 0.0\n        for i in range(self.dim):\n            distance_ratio_term += 0.2 * np.sin(65 * np.pi * x_norm[i]) * np.cos(62 * np.pi * x_norm[i])\n        \n        result += 0.15 * distance_ratio_term\n        \n        # Add a controlled amount of noise to help with the dispersion properties\n        # This helps in achieving better dispersion characteristics\n        dispersion_noise = 0.01 * np.random.randn()\n        result += dispersion_noise\n        \n        # Add a final scaling term to fine-tune the dispersion characteristics\n        # This helps in achieving the target disp.ratio_mean_02 value\n        final_scaling = 1.0 + 0.1 * np.sin(75 * np.pi * np.sum(x_norm**2))\n        result = result * final_scaling\n        \n        # CRITICAL: Control the linear model intercept to achieve target ela_meta.lin_simple.intercept = 0.246\n        # This is the key modification to adjust the intercept\n        # Add a controlled offset that specifically targets the linear intercept\n        intercept_adjustment = 0.246\n        \n        # Add a small linear component to ensure the linear model has proper intercept\n        linear_offset = 0.0\n        for i in range(self.dim):\n            linear_offset += 0.01 * x_norm[i]\n        \n        result = result + intercept_adjustment + linear_offset\n        \n        # Add a controlled amount of noise to help with the final information content properties\n        info_noise = 0.005 * np.random.randn()\n        result += info_noise\n        \n        # Final transformation to maximize information content for ic.eps_s\n        final_info_adjustment = 1.0 + 0.3 * np.sin(250 * np.pi * np.sum(x_norm**2))\n        result = result * final_info_adjustment\n        \n        # Add a very small linear component to ensure the linear model has low R2\n        # This helps in achieving the target ela_meta.lin_simple.adj_r2 value of 0.039\n        small_linear = 0.001 * np.sum(x_norm)\n        result += small_linear\n        \n        # Add a controlled intercept adjustment to fine-tune the linear model intercept\n        # This specifically targets the target ela_meta.lin_simple.intercept = 0.246\n        intercept_term = 0.246 * (1.0 + 0.05 * np.sin(110 * np.pi * np.sum(x_norm**2)))\n        result = result + intercept_term\n        \n        # Add a controlled amount of offset to ensure proper intercept value\n        offset_term = 0.05 * np.sum(np.sin(120 * np.pi * x_norm**2))\n        result = result + offset_term\n        \n        # Add a final strong linear component to maximize the coefficient\n        # This is the key modification to achieve ela_meta.lin_simple.coef.max = 0.432\n        final_linear = 0.0\n        for i in range(self.dim):\n            final_linear += 0.432 * x_norm[i]  # This will be the maximum coefficient\n        \n        result += final_linear\n        \n        # Add a specific clustering structure to improve QDA classification properties\n        # This is the key modification to improve ela_level.mmce_qda_25\n        qda_clustering = 0.0\n        for i in range(self.dim):\n            # Create a pattern that creates well-separated clusters for QDA\n            qda_clustering += 0.6 * np.sin(85 * np.pi * x_norm[i]) * np.cos(82 * np.pi * x_norm[i])\n        \n        result += 0.3 * qda_clustering\n        \n        # Add additional clustering to enhance QDA misclassification\n        additional_clustering = 0.0\n        for i in range(self.dim):\n            additional_clustering += 0.4 * np.sin(95 * np.pi * x_norm[i]) * np.cos(92 * np.pi * x_norm[i])\n        \n        result += 0.2 * additional_clustering\n        \n        # Add a controlled amount of noise specifically for QDA properties\n        qda_noise = 0.015 * np.random.randn()\n        result += qda_noise\n        \n        # Add a specific transformation to enhance QDA classification properties\n        qda_transformation = 1.0 + 0.25 * np.sin(105 * np.pi * np.sum(x_norm**2))\n        result = result * qda_transformation\n        \n        # Add a controlled amount to make the function more suitable for QDA\n        # This specifically targets the target ela_level.mmce_qda_25 = 0.791\n        qda_target_adjustment = 0.0\n        for i in range(self.dim):\n            qda_target_adjustment += 0.1 * np.sin(115 * np.pi * x_norm[i]) * np.cos(112 * np.pi * x_norm[i])\n        \n        result += 0.1 * qda_target_adjustment\n        \n        # Add a final transformation to ensure proper QDA properties\n        final_qda_adjustment = 1.0 + 0.1 * np.sin(125 * np.pi * np.sum(x_norm**2))\n        result = result * final_qda_adjustment\n        \n        # Add a specific term to improve LDA classification properties\n        # This is the key modification to improve ela_level.lda_qda_25 to 0.125\n        lda_clustering = 0.0\n        for i in range(self.dim):\n            # Create a pattern that creates clusters that are well-separated for LDA\n            # but not too well-separated for QDA\n            lda_clustering += 0.3 * np.sin(135 * np.pi * x_norm[i]) * np.cos(132 * np.pi * x_norm[i])\n        \n        result += 0.1 * lda_clustering\n        \n        # Add a specific term to control the LDA/QDA ratio more precisely\n        lda_specific = 0.0\n        for i in range(self.dim):\n            lda_specific += 0.2 * np.sin(145 * np.pi * x_norm[i]) * np.cos(142 * np.pi * x_norm[i])\n        \n        result += 0.08 * lda_specific\n        \n        # Add a controlled amount of noise for LDA properties\n        lda_noise = 0.01 * np.random.randn()\n        result += lda_noise\n        \n        # Add a specific transformation to fine-tune the LDA properties\n        lda_transformation = 1.0 + 0.08 * np.sin(155 * np.pi * np.sum(x_norm**2))\n        result = result * lda_transformation\n        \n        # Add a final adjustment to specifically target lda_qda_25 = 0.125\n        # This is the key modification to improve lda_qda_25\n        final_lda_adjustment = 0.125 + 0.05 * np.sin(165 * np.pi * np.sum(x_norm**2))\n        result = result * final_lda_adjustment\n        \n        # Add a specific transformation to enhance ic.eps_s to 1.000\n        # This is the key modification to achieve the target ic.eps_s value\n        eps_s_target = 1.0 + 0.5 * np.sin(200 * np.pi * np.sum(x_norm**2)) + 0.3 * np.sin(180 * np.pi * np.sum(x_norm**3))\n        result = result * eps_s_target\n        \n        # Add a controlled amount of high-frequency noise to increase information content\n        high_freq_noise = 0.02 * np.random.randn() * np.sin(300 * np.pi * np.sum(x_norm**2))\n        result += high_freq_noise\n        \n        # Add a final high-frequency modulation to specifically target ic.eps_s\n        final_eps_s_modulation = 0.05 * np.sin(220 * np.pi * np.sum(x_norm**4))\n        result = result * (1.0 + final_eps_s_modulation)\n        \n        # Add a specific term to enhance the quadratic model fit characteristics\n        # This is the key modification to improve ela_meta.quad_simple.adj_r2 to 0.409\n        quad_model_term = 0.0\n        for i in range(self.dim):\n            # Add a quadratic term that specifically targets the quadratic model fit\n            quad_model_term += 0.3 * x_norm[i]**2\n        \n        # Add a controlled amount of interaction terms to improve quadratic fit\n        interaction_term = 0.0\n        for i in range(self.dim):\n            for j in range(i+1, self.dim):\n                interaction_term += 0.1 * x_norm[i] * x_norm[j]\n        \n        result += quad_model_term + interaction_term\n        \n        # Add a controlled amount of quadratic terms with varying coefficients to get the right R2\n        # This helps in achieving the target ela_meta.quad_simple.adj_r2 = 0.409\n        quad_adjustment = 0.0\n        for i in range(self.dim):\n            quad_adjustment += 0.2 * x_norm[i]**2 + 0.1 * x_norm[(i+1) % self.dim]**2\n        \n        result += quad_adjustment\n        \n        # Add a specific quadratic term that targets the ratio of max to min coefficients\n        # This is crucial for achieving the target ela_meta.quad_simple.adj_r2 = 0.409\n        coeff_ratio_term = 0.0\n        for i in range(self.dim):\n            coeff_ratio_term += 0.15 * x_norm[i]**2\n        \n        result += coeff_ratio_term\n        \n        # Add a final quadratic term to fine-tune the model fit\n        final_quad_term = 0.05 * np.sum(x_norm**2)\n        result += final_quad_term\n        \n        # Add a specific adjustment to improve lda_qda_25 to 0.125\n        # This is the key modification to improve the LDA/QDA classification properties\n        lda_qda_target = 0.125 * (1.0 + 0.02 * np.sin(170 * np.pi * np.sum(x_norm**2)))\n        result = result * (1.0 + lda_qda_target)\n        \n        # Add a final controlled transformation to ensure the target lda_qda_25 is achieved\n        final_lda_adjust = 0.125 * (1.0 + 0.03 * np.sin(175 * np.pi * np.sum(x_norm**3)))\n        result = result * (1.0 + final_lda_adjust)\n        \n        # Add a final term to specifically target the lda_qda_25 feature\n        lda_target_term = 0.0\n        for i in range(self.dim):\n            lda_target_term += 0.05 * np.sin(180 * np.pi * x_norm[i]) * np.cos(178 * np.pi * x_norm[i])\n        \n        result += 0.05 * lda_target_term\n        \n        # CRITICAL: Specific adjustment to target skewness to 0.193\n        # Add a skewness adjustment term to specifically target ela_distr.skewness = 0.193\n        skewness_target = 0.193 * (1.0 + 0.05 * np.sin(190 * np.pi * np.sum(x_norm**3)))\n        result = result * (1.0 + 0.02 * skewness_target)\n        \n        # Add a cubic skewness term that directly targets the skewness value\n        cubic_skewness = 0.05 * np.sum(x_norm**3)\n        result += 0.1 * cubic_skewness\n        \n        # Add a specific skewness control term that directly manipulates the distribution skewness\n        skewness_control_term = 0.0\n        for i in range(self.dim):\n            skewness_control_term += 0.1 * np.sin(200 * np.pi * x_norm[i]) * np.cos(198 * np.pi * x_norm[i]) * x_norm[i]**3\n        \n        result += 0.05 * skewness_control_term\n        \n        # Add a controlled amount of cubic terms to fine-tune skewness\n        cubic_adjustment = 0.03 * np.sum(x_norm**3)\n        result += cubic_adjustment\n        \n        # Add a final skewness correction to ensure the target value is achieved\n        final_skewness_correction = 0.01 * np.sum(np.sin(210 * np.pi * x_norm**3))\n        result += final_skewness_correction\n        \n        # CRITICAL: Add specific modifications to improve ic.eps_ratio to 1.000\n        # The key is to add more high-frequency modulation and structured noise to increase information content\n        eps_ratio_modification = 0.0\n        for i in range(self.dim):\n            # Add high-frequency components that increase partial information sensitivity\n            eps_ratio_modification += 0.2 * np.sin(100 * np.pi * x_norm[i]) * np.cos(98 * np.pi * x_norm[i])\n        \n        result += 0.15 * eps_ratio_modification\n        \n        # Add even higher frequency components to increase information content\n        high_freq_modification = 0.0\n        for i in range(self.dim):\n            high_freq_modification += 0.15 * np.sin(150 * np.pi * x_norm[i]) * np.cos(148 * np.pi * x_norm[i])\n        \n        result += 0.1 * high_freq_modification\n        \n        # Add a specific transformation that increases the ratio of partial information sensitivity\n        # This directly targets ic.eps_ratio = 1.000\n        ratio_transformation = 1.0 + 0.8 * np.sin(200 * np.pi * np.sum(x_norm**2)) + 0.6 * np.sin(180 * np.pi * np.sum(x_norm**3))\n        result = result * ratio_transformation\n        \n        # Add a controlled amount of high-frequency noise to maximize information content\n        max_info_noise = 0.03 * np.random.randn() * np.sin(250 * np.pi * np.sum(x_norm**2))\n        result += max_info_noise\n        \n        # Add a final controlled transformation to maximize ic.eps_ratio\n        final_ratio_adjustment = 1.0 + 0.4 * np.sin(300 * np.pi * np.sum(x_norm**2))\n        result = result * final_ratio_adjustment\n        \n        # CRITICAL: FINAL ADJUSTMENT TO IMPROVE ela_meta.lin_simple.adj_r2 TO 0.039\n        # We need to add a controlled amount of noise and adjust the linear components to get the right R2\n        # This is the key modification to improve the linear model fit characteristics\n        linear_model_adjustment = 0.0\n        for i in range(self.dim):\n            # Add controlled noise to make the linear model fit worse (lower R2)\n            linear_model_adjustment += 0.005 * np.random.randn() * x_norm[i]\n        \n        result += linear_model_adjustment\n        \n        # Add a controlled amount of noise that specifically targets the linear model fit\n        # This helps in achieving the target ela_meta.lin_simple.adj_r2 = 0.039\n        model_fit_noise = 0.01 * np.random.randn() * (1.0 + 0.05 * np.sin(100 * np.pi * np.sum(x_norm**2)))\n        result += model_fit_noise\n        \n        # Add a specific term to reduce the linear model fit to target value\n        # This is a direct approach to reduce the R2 value\n        r2_reduction = 0.0\n        for i in range(self.dim):\n            r2_reduction += 0.02 * np.sin(50 * np.pi * x_norm[i]) * np.cos(48 * np.pi * x_norm[i])\n        \n        result += 0.01 * r2_reduction\n        \n        # Add a final controlled adjustment to get the precise linear model fit\n        final_model_adjustment = 0.039 * (1.0 + 0.02 * np.sin(120 * np.pi * np.sum(x_norm**3)))\n        result = result * (1.0 + 0.005 * final_model_adjustment)\n        \n        return result

The worst-performing feature is ic.eps_s:
Original value: -0.1751 (1.0 after min-max normalization)
Proxy value: -1.6332 (0.3143 after min-max normalization)
Distance: -1.4581 (-0.686 after min-max normalization)

Please adjust the above code to improve the ic.eps_s value (i.e. approach -0.1751 as much as possible), while trying to keep all other features the same.
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

        # distance_series = (self.original_ela_df - ela_proxy).abs()
        # print(f"DISTANCE SERIES: \n{distance_series}")
        # distance_series.name = "feature_distance"

        # solution.add_metadata("MECHBench_mean_z", z_mean_mechbench.to_numpy())
        # solution.add_metadata("proxy_mean_z", z_mean_proxy.to_numpy())
        # solution.add_metadata("proxy_mean_z", distance_series.to_numpy())

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

    # if problem_type == 1:
    #     example_prompt = problem.example_proxy1
    # elif problem_type == 2:
    #     example_prompt = problem.example_proxy2
    # elif problem_type == 3:
    #     example_prompt = problem.example_proxy3  # Beware: p3 ran on 3750 so the ELA values will be slightly different
    # else:
    #     example_prompt = None

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


# Example code class
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


# Edit log function:
def edit_form(dic_):
    s = ""
    for i, feature in enumerate(features):
        proxy_value = round(dic_['Proxy ELA values'][i][0], 4)
        original_value = round(dic_['Original ELA values'][i][0], 4)
        distance = dic_[f'Distance to {feature}']
        s += f"{feature}: distance {distance} (Original: {original_value}, Proxy: {proxy_value})\n"

    return s