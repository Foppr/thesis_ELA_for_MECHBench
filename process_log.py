import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class LLaMEAAnalyzer:
    def __init__(self, missing_niche_radius=True):
        self.missing_niche_radius = missing_niche_radius
        self.features = [
            'disp.ratio_mean_02',
            'ela_distr.skewness',
            'ela_meta.lin_simple.adj_r2',
            'ela_meta.lin_simple.intercept',
            'ela_meta.lin_simple.coef.max',
            'ela_meta.quad_simple.adj_r2',
            'ic.eps_ratio',
            'ic.eps_s',
            'nbc.nb_fitness.cor',
            'ela_level.mmce_qda_25',
            'ela_level.lda_qda_25'
        ]
        # Storage for processed dataframes per experiment
        self.experiments_data = {}

    def load_log(self, exp_name):
        """
        Loads the JSONL log file, cleans out invalid entries,
        optionally computes niche radius, and stores raw data into a DataFrame.
        """
        raw_log = []
        with open(f"{exp_name}/log.jsonl", 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    individual = json.loads(line)
                    # Safely filter out infinite fitness upfront
                    if individual.get('fitness') != float('inf') and individual.get('fitness') != np.inf:
                        raw_log.append(individual)

        if self.missing_niche_radius:
            raw_log = self._compute_niche_radius(raw_log)

        # Process into standard and feature dataframes
        self.experiments_data[exp_name] = self._process_to_dataframe(raw_log)
        print(f"Successfully loaded and processed: {exp_name}")
        return raw_log

    def _compute_niche_radius(self, log):
        """Computes the niche radius per generation without modifying lists during iteration."""
        if not log:
            return log

        unique_gens = sorted(list(set(ind['generation'] for ind in log)))

        for gen in unique_gens:
            individuals_genX = [ind for ind in log if ind['generation'] == gen]
            dists = []

            for i in range(len(individuals_genX)):
                for j in range(i + 1, len(individuals_genX)):
                    ind1 = individuals_genX[i]
                    ind2 = individuals_genX[j]
                    try:
                        proxy_ela1 = ind1['metadata']['Proxy ELA values']
                        proxy_ela2 = ind2['metadata']['Proxy ELA values']
                        dist = np.sum(np.abs(np.asarray(proxy_ela1) - np.asarray(proxy_ela2)))
                        dists.append(dist)
                    except KeyError:
                        pass

            niche_radius = float(np.mean(dists)) if dists else 0.0
            for ind in individuals_genX:
                if 'metadata' in ind:
                    ind['metadata']['niche_radius'] = niche_radius
        return log

    def _process_to_dataframe(self, log):
        """Flattens list data into a neat Pandas DataFrame containing total fitness and feature errors."""
        flat_records = []
        for ind in log:
            record = {
                'generation': ind['generation'],
                'fitness': ind['fitness']
            }
            # try:
            proxy = ind['metadata']['Proxy ELA values']
            original = ind['metadata']['Original ELA values']
            for idx, feat_name in enumerate(self.features):
                # Store absolute error for each unique feature
                record[feat_name] = abs(proxy[idx][0] - original[idx][0])
            # except (KeyError, TypeError, IndexError):
            #     pass
            flat_records.append(record)

        return pd.DataFrame(flat_records)

    def compare_experiments(self, exp_names):
        """
        Computes global axis boundaries across a pool of experiments.
        Returns: max_gen, ub_total, ub_features
        """
        max_gens = []
        ubs_total = []
        ubs_features = []

        for name in exp_names:
            df = self.experiments_data[name]

            # Total fitness statistics calculation
            agg_total = df.groupby('generation')['fitness'].agg(['min', 'mean']).reset_index()
            max_gens.append(agg_total['generation'].max())
            ubs_total.append(max(agg_total['mean'].max(), agg_total['min'].max()))

            # Feature statistics calculation across all 11 features
            for feat in self.features:
                if feat in df.columns:
                    agg_feat = df.groupby('generation')[feat].agg(['min', 'mean'])
                    ubs_features.append(max(agg_feat['mean'].max(), agg_feat['min'].max()))

        return min(max_gens), max(ubs_total), max(ubs_features)

    def plot_total_fitness(self, exp_name, global_stats, save_suffix):
        """Plots the global best and average raw fitness across generations."""
        df = self.experiments_data[exp_name]
        max_gen, ub_total, _ = global_stats  # Extract total upper bound

        df_filtered = df[df['generation'] <= max_gen]
        agg_df = df_filtered.groupby('generation')['fitness'].agg(['min', 'mean']).reset_index()
        agg_df = agg_df.sort_values('generation')

        generations = agg_df['generation']
        avg_distances = agg_df['mean']
        best_distances = agg_df['min']

        min_val = best_distances.min()
        best_gen = agg_df.loc[agg_df['min'] == min_val, 'generation'].iloc[0]

        plt.figure(figsize=(10, 6))
        plt.style.use('seaborn-v0_8-whitegrid')

        plt.plot(generations, best_distances, label='Best Raw Distance (Min)', color='#1f77b4', linewidth=2.5,
                 marker='o', markersize=4)
        plt.plot(generations, avg_distances, label='Avg Raw Distance', color='#ff7f0e', linewidth=2, linestyle='--')
        plt.scatter(best_gen, min_val, color='#2ca02c', s=100, zorder=5, label='Global Best')

        plt.text(best_gen, min_val - (ub_total * 0.02), f'{min_val:.3f}', color='#006400', fontweight='bold',
                 ha='center', va='top', fontsize=14)
        plt.ylim(0, ub_total)

        plt.title(f'LLaMEA Evolutionary Progress (Problem {save_suffix})', fontsize=14, fontweight='bold', pad=15)
        plt.xlabel('Generation', fontsize=12, labelpad=10)
        plt.ylabel('Raw Distance (Fitness)', fontsize=12, labelpad=10)
        plt.xticks(generations)
        plt.legend(fontsize=11, loc='upper right', frameon=True, facecolor='white', edgecolor='none')
        plt.tight_layout()

        filename = f'llamea_graphs/{save_suffix}.png'
        plt.savefig(filename, dpi=300)
        print(f"Total fitness graph saved as '{filename}'")
        plt.close()

    def plot_feature_fitness(self, exp_name, feature_name, global_stats, save_suffix):
        """Plots both the mean and best (minimum) absolute error for a specific ELA feature."""
        if feature_name not in self.features:
            raise ValueError(f"Feature '{feature_name}' not found in the defined features list.")

        df = self.experiments_data[exp_name]
        max_gen, _, ub_features = global_stats  # Extract uniform features upper bound

        df_filtered = df[df['generation'] <= max_gen]
        agg_df = df_filtered.groupby('generation')[feature_name].agg(['min', 'mean']).reset_index()
        agg_df = agg_df.sort_values('generation')

        generations = agg_df['generation']
        avg_errors = agg_df['mean']
        best_errors = agg_df['min']

        # Identify the local minimum for this specific feature
        min_val = best_errors.min()
        best_gen = agg_df.loc[agg_df['min'] == min_val, 'generation'].iloc[0]

        plt.figure(figsize=(10, 6))
        plt.style.use('seaborn-v0_8-whitegrid')

        # Plot best and average lines for visual symmetry with the total progress graph
        plt.plot(generations, best_errors, label='Best Feature Error (Min)', color='#1f77b4', linewidth=2.5, marker='o',
                 markersize=4)
        plt.plot(generations, avg_errors, label='Avg Feature Error', color='#ff7f0e', linewidth=2, linestyle='--')

        # Highlight the best-performing individual dot for this feature
        plt.scatter(best_gen, min_val, color='#2ca02c', s=100, zorder=5, label='Global Best Error')
        plt.text(best_gen, min_val - (ub_features * 0.02), f'{min_val:.3f}', color='#006400', fontweight='bold',
                 ha='center', va='top', fontsize=14)

        # Enforce global unified scaling across all feature plots
        plt.ylim(0, ub_features)

        plt.title(f'ELA Feature Progress: {feature_name}\n(Problem {save_suffix})', fontsize=13, fontweight='bold',
                  pad=12)
        plt.xlabel('Generation', fontsize=12, labelpad=10)
        plt.ylabel('Absolute Error (|Proxy - Original|)', fontsize=11, labelpad=10)
        plt.xticks(generations)
        plt.legend(fontsize=11, loc='upper right', frameon=True, facecolor='white', edgecolor='none')
        plt.tight_layout()

        filename = f'llamea_graphs/{feature_name}_{save_suffix}.png'
        plt.savefig(filename, dpi=300)
        print(f"Feature graph saved as '{filename}'")
        plt.close()

    def generate_plots(self, exp_name, global_stats, save_suffix, plot_type='total', feature_name=None):
        """
        Unified router interface to generate plots.
        plot_type options: 'total', 'feature', 'all_features'
        """
        if plot_type == 'total':
            self.plot_total_fitness(exp_name, global_stats, save_suffix)
        elif plot_type == 'feature':
            if not feature_name:
                raise ValueError("A specific 'feature_name' must be provided if plot_type='feature'.")
            self.plot_feature_fitness(exp_name, feature_name, global_stats, save_suffix)
        elif plot_type == 'all_features':
            for feat in self.features:
                self.plot_feature_fitness(exp_name, feat, global_stats, save_suffix)
        else:
            raise ValueError("Invalid plot_type. Use 'total', 'feature', or 'all_features'.")

    def save_feature_difficulty_ranking(self, exp_mapping, output_filename='llamea_tables/feature_difficulty_ranking.csv'):
        """
        Aggregates the best (minimum) fitness achieved for each feature across mapping profiles.
        Sorts features from worst (highest remaining absolute error) to best (lowest error).
        """
        feature_data = {}

        # Pull min value for each feature across the specified experiments
        for alias, exp_name in exp_mapping.items():
            if exp_name not in self.experiments_data:
                print(f"Warning: Data for {exp_name} not found. Skipping {alias}.")
                continue

            df = self.experiments_data[exp_name]
            feature_data[alias] = {}

            for feat in self.features:
                if feat in df.columns:
                    # Capture the overall absolute best achieved distance for this feature
                    feature_data[alias][feat] = df[feat].min()
                else:
                    feature_data[alias][feat] = np.nan

        # Construct DataFrame
        df_ranking = pd.DataFrame(feature_data)

        # Sorting by the row-wise mean descending handles worst (highest error) -> best (lowest error)
        df_ranking['overall_mean_error'] = df_ranking.mean(axis=1)
        df_ranking = df_ranking.sort_values(by='overall_mean_error', ascending=False)

        # Clean up sorting column to preserve structural layout requested
        df_ranking = df_ranking.drop(columns=['overall_mean_error'])
        df_ranking.index.name = 'Feature'
        df_ranking = df_ranking.round(3)

        df_ranking.to_csv(output_filename)
        print(f"\n--- Feature Optimization Difficulty Ranking Saved to '{output_filename}' ---")
        print(df_ranking.to_string())

        # Save Latex file
        df_ranking.index = df_ranking.index.str.replace('_', r'\_')

        latex_code = df_ranking.to_latex(
            float_format="%.3f",  # Enforce uniform 3-decimal precision
            column_format="lrrr",  # Left-align feature names, Right-align numeric columns
            caption="LLaMEA Loop Best Achieved Absolute Feature Error Across Problem Profiles",
            label="tab:feature_difficulty",
            position="th"  # Standard top/here float layout positions
        )

        with open('llamea_tables/feature_difficulty.tex', 'w', encoding='utf-8') as f:
            f.write(latex_code)

        print("LaTeX table code successfully saved to 'feature_difficulty.tex'")
        print("\nGenerated LaTeX Code:\n")
        print(latex_code)

        return df_ranking


# --- Execution Block ---
if __name__ == "__main__":
    same_scales = "new_class"

    name1 = "exp-06-04_002048-LLaMEA-qwen3-coder_30b-ELA_for_MECHBENCH"
    name2 = "exp-06-04_122824-LLaMEA-qwen3-coder_30b-ELA_for_MECHBENCH"
    name3 = "exp-06-05_110213-LLaMEA-qwen3-coder_30b-ELA_for_MECHBENCH"

    # Initialize Class
    analyzer = LLaMEAAnalyzer(missing_niche_radius=True)

    # 1. Load Logs
    analyzer.load_log(name1)
    analyzer.load_log(name2)
    analyzer.load_log(name3)

    # 2. Extract shared bounds configuration (contains: max_gen, ub_total, ub_features)
    problem_stats = analyzer.compare_experiments([name1, name2, name3])

    # 3. Generate graphs using the unified router
    # Generate Total Performance Graphs
    # analyzer.generate_plots(name1, problem_stats, save_suffix=f"p1_budget800_niche2{same_scales}", plot_type='total')
    # analyzer.generate_plots(name2, problem_stats, save_suffix=f"p2_budget800_niche2{same_scales}", plot_type='total')
    # analyzer.generate_plots(name3, problem_stats, save_suffix=f"p3_budget800_niche2{same_scales}", plot_type='total')

    # analyzer.generate_plots(name1, problem_stats, save_suffix=f"p1_budget800", plot_type='all_features')
    # analyzer.generate_plots(name2, problem_stats, save_suffix=f"p2_budget800", plot_type='all_features')
    # analyzer.generate_plots(name3, problem_stats, save_suffix=f"p3_budget800", plot_type='all_features')

    # Define the mapping for your experiments
    experiment_mapping = {
        'p1': name1,
        'p2': name2,
        'p3': name3
    }

    # Generate and save the CSV ranking
    difficulty_df = analyzer.save_feature_difficulty_ranking(experiment_mapping)
