import json
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from sklearn import metrics
from sklearn.decomposition import PCA
import seaborn as sns
from matplotlib.lines import Line2D
from scipy.stats import kendalltau


class LLaMEAAnalyzer:
    def __init__(self, log_dir, save_folder_name, aocc_path):
        self.log_dir = log_dir
        self.save_folder_name = save_folder_name
        if not os.path.exists(save_folder_name):
            os.mkdir(save_folder_name)

        self.aocc_path = aocc_path

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

        self.original_minmaxEla_p1 = {'disp.ratio_mean_02': 0.3180841545512229, 'ela_distr.skewness': 0.1293188522940492, 'ela_meta.lin_simple.adj_r2': 0.2210812231592529, 'ela_meta.lin_simple.intercept': 0.7444454923627558, 'ela_meta.lin_simple.coef.max': 1.0, 'ela_meta.quad_simple.adj_r2': 0.2425517809797153, 'ic.eps_ratio': 1.0, 'ic.eps_s': 1.0, 'nbc.nb_fitness.cor': 0.5102519892845082, 'ela_level.mmce_qda_25': 0.2957746230906558, 'ela_level.lda_qda_25': 0.3331012892967914}
        self.original_minmaxEla_p2 = {'disp.ratio_mean_02': 0.613775757719448, 'ela_distr.skewness': 0.1919105264092217, 'ela_meta.lin_simple.adj_r2': 0.2228005657527632, 'ela_meta.lin_simple.intercept': 0.4325753309513677, 'ela_meta.lin_simple.coef.max': 0.3115486529327629, 'ela_meta.quad_simple.adj_r2': 0.2579866624338019, 'ic.eps_ratio': 0.864406779661017, 'ic.eps_s': 0.7478260869565218, 'nbc.nb_fitness.cor': 0.6089279644868683, 'ela_level.mmce_qda_25': 0.225352085399721, 'ela_level.lda_qda_25': 0.4880185824214766}
        self.original_minmaxEla_p3 = {'disp.ratio_mean_02': 0.8785028761364115, 'ela_distr.skewness': 0.1827705273439356, 'ela_meta.lin_simple.adj_r2': 0.0168121027022387, 'ela_meta.lin_simple.intercept': 0.2178719275405489, 'ela_meta.lin_simple.coef.max': 0.595020107122112, 'ela_meta.quad_simple.adj_r2': 0.4266757168517114, 'ic.eps_ratio': 1.0, 'ic.eps_s': 1.0, 'nbc.nb_fitness.cor': 0.3924693159004784, 'ela_level.mmce_qda_25': 0.7743123688965757, 'ela_level.lda_qda_25': 0.1753467427267984}

        self.standings1 = None
        self.standings2 = None
        self.standings3 = None
        self.standings_total = {}

        self.log = {}
        self.experiments_data = {}

    def run(self,
            progress_plots=True,
            pca_plots=True,
            diversity_plots=True,
            get_proxy_standings=True,
            compute_aocc=True,
            compare_aocc=True,
            kendall_fitness_scatter=True
            ):
        # After LLaMEA loop
        self.load_logs()

        if progress_plots:
            save_folder = 'progression_graphs'
            print("\n--- Getting stats to produce uniform experiment bounds ---")
            max_ind, max_fit = self.compare_experiments_by_individual()
            max_feat_fit = self.compare_features_by_individual(max_ind_bound=max_ind)

            print("\n--- LLaMEA progression plots ---")
            self.plot_individual_progression((max_ind, max_fit), save_folder=save_folder, clean_layout=True)
            self.save_individual_legend(save_folder)

            print("\n--- Per-feature progression plots ---")
            self.plot_feature_progression(global_max_fit=max_feat_fit, max_ind_bound=max_ind, save_folder=save_folder, clean_layout=True)
            self.save_feature_legend(save_folder)

        if pca_plots:
            print(f'\n --- Making PCA plots ---')

            for p in self.log:
                all_problem_data = []
                for config in self.log[p]:
                    if 'total' not in config:
                        for inds in self.log[p][config]:
                            if 'total' in inds:
                                for individual in self.log[p][config][inds]:
                                    proxy_dic = individual['metadata']["Proxy min-max ELA values"]
                                    all_problem_data.append(list(proxy_dic.values()))

                # Shared PCA model per problem
                if all_problem_data:
                    shared_df = pd.DataFrame(all_problem_data, columns=self.features)
                    shared_pca = PCA(n_components=2)
                    shared_pca.fit(shared_df)

                    for config in self.log[p]:
                        if 'total' not in config:
                            for inds in self.log[p][config]:
                                if 'total' in inds:
                                    self.pca(
                                        self.log[p][config][inds],
                                        shared_pca,
                                        save_folder='pca_plots',
                                        name_=f'{p}_{config}'
                                    )

        if diversity_plots:
            self.plot_initial_diversity()

        if get_proxy_standings:
            print(f'\n --- Getting podium, median and worst proxy per problem ---')
            log = self.log

            p1_total = log['p1']['p1_total']
            p2_total = log['p2']['p2_total']
            p3_total = log['p3']['p3_total']

            self.standings1 = self.get_podium_median_worst(p1_total)
            self.standings2 = self.get_podium_median_worst(p2_total)
            self.standings3 = self.get_podium_median_worst(p3_total)
            self.standings1.to_csv(f'{self.save_folder_name}/standings1.csv')
            self.standings2.to_csv(f'{self.save_folder_name}/standings2.csv')
            self.standings3.to_csv(f'{self.save_folder_name}/standings3.csv')
        else:
            self.standings1 = pd.read_csv(f'{self.save_folder_name}/standings1.csv')
            self.standings2 = pd.read_csv(f'{self.save_folder_name}/standings2.csv')
            self.standings3 = pd.read_csv(f'{self.save_folder_name}/standings3.csv')

        self.standings_total['p1'] = self.standings1
        self.standings_total['p2'] = self.standings2
        self.standings_total['p3'] = self.standings3

        # RUN ALGORITHMS

        # After algorithm runs
        if compute_aocc:
            print(f'\n --- Computing AOCC for all proxies ---')
            aocc_savename = 'aocc_results.csv'
            self.compute_AOCC(self.aocc_path, aocc_savename)

        if compare_aocc:
            print(f'\n --- Computing Kendall\'s tau ---')
            kendall_savename = 'kendall_results'
            aocc_savename = 'aocc_results.csv'
            self.compare_AOCCs(aocc_savename, kendall_savename)

        if kendall_fitness_scatter:
            print(f'\n --- Producing Kendall vs. Fitness scatterplot ---')
            scatter_savename = 'kendall_fitness_scatterplot'
            path_kendall_results = 'kendall_results'
            self.scatter_fitness_kendall(path_kendall_results, scatter_savename)

    def load_logs(self):
        for problem_ in os.listdir(self.log_dir):
            problem_log = []  # Contains all individuals of this problem, across all configs and runs
            self.log[problem_] = {}
            self.experiments_data[problem_] = {}
            for config_ in os.listdir(f'{self.log_dir}/{problem_}'):
                config_log = []  # Contains all individuals of this config across all runs
                self.log[problem_][config_] = {}
                self.experiments_data[problem_][config_] = {}
                for run_ in os.listdir(f'{self.log_dir}/{problem_}/{config_}'):
                    run_log = []  # Contains all individuals of this run
                    full_path = f'{self.log_dir}/{problem_}/{config_}/{run_}'
                    with open(f"{full_path}/log.jsonl", 'r', encoding='utf-8') as f:
                        for line in f:
                            if line.strip():
                                individual = json.loads(line)
                                # Skip infinities (individuals with errors)
                                if individual.get('fitness') != float('inf') and individual.get('fitness') != np.inf:
                                    individual['problem'] = problem_
                                    individual['ES_config'] = config_
                                    individual['run'] = run_
                                    run_log.append(individual)
                                    config_log.append(individual)
                                    problem_log.append(individual)

                    self.log[problem_][config_][run_] = run_log
                    self.experiments_data[problem_][config_][run_] = self._process_to_dataframe(run_log)
                    # 3 x 3 x 5 run_logs
                self.log[problem_][config_][f'{config_}_total'] = config_log
                self.experiments_data[problem_][config_][f'{config_}_total'] = self._process_to_dataframe(config_log)
                # 3 x 3 config_logs
            self.log[problem_][f'{problem_}_total'] = problem_log
            self.experiments_data[problem_][f'{problem_}_total'] = self._process_to_dataframe(problem_log)
            # 3 problem_logs

    def _process_to_dataframe(self, log):
        flat_records = []
        for ind in log:
            record = {
                'id': ind['id'],
                'generation': ind['generation'],
                'fitness': ind['fitness'],
                # 'raw_mean_distance': ind['metadata']['Raw mean distance']
            }
            proxy_dic = ind['metadata']["Proxy min-max ELA values"]
            original_dic = ind['metadata']['Original min-max ELA values']
            for idx, feat_name in enumerate(self.features):
                # Store error for each unique feature
                record[feat_name] = abs(proxy_dic[feat_name] - original_dic[feat_name])
            flat_records.append(record)

        return pd.DataFrame(flat_records)

    def pca(self, individuals, pre_fitted_pca, save_folder, name_):
        pca_dic = {}
        proxy_data = pd.DataFrame(columns=self.features)
        generations = []

        for i, individual in enumerate(individuals):
            proxy_dic = individual['metadata']["Proxy min-max ELA values"]
            proxy_data.loc[i] = proxy_dic.values()
            generations.append(individual['generation'])

        generations = pd.Series(generations)

        proxies_reduced = pre_fitted_pca.transform(proxy_data)
        expl_var = pre_fitted_pca.explained_variance_ratio_

        fig, ax = plt.subplots(figsize=(9, 6))

        # Scatterplot
        scatter = ax.scatter(
            proxies_reduced[:, 0],
            proxies_reduced[:, 1],
            c=generations,
            cmap="viridis",
            s=40,
            alpha=0.8,
            edgecolors="none"
        )

        # PC values
        ax.set(
            title=f"PCA by Generations ({name_})",
            xlabel=f"1st Principal Component ({expl_var[0] * 100:.1f}%)",
            ylabel=f"2nd Principal Component ({expl_var[1] * 100:.1f}%)",
        )

        # Axes
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        # Colorbar
        cbar = fig.colorbar(scatter, ax=ax)
        cbar.set_label("Evolutionary Generation", rotation=270, labelpad=15)

        plt.tight_layout()
        filename = f"{self.save_folder_name}/{save_folder}/PCA_results_{name_}.png"
        plt.savefig(filename, dpi=900)
        plt.close()

        return pca_dic

    def plot_initial_diversity(self):
        # Get all initial parents and their min-maxed ELA values:
        all_initial_elas = []
        for problem in self.log:
            for config in self.log[problem]:
                if 'total' not in config:
                    if config == '1+1':
                        n_parents = 1
                    elif config == '2+4':
                        n_parents = 2
                    elif config == '4+8':
                        n_parents = 4
                    for run in self.log[problem][config]:
                        if 'total' not in run:
                            parent_inds = self.log[problem][config][run][:n_parents]
                            parent_elas = [ind['metadata']['Proxy min-max ELA values'] for ind in parent_inds]
                            for parent_ela in parent_elas:
                                all_initial_elas.append(parent_ela)

        # Plot parent feature diversity with a scatterplot
        df_proxies = pd.DataFrame(all_initial_elas)
        df_melted = df_proxies.melt(var_name="Feature", value_name="Value")

        # Map feature names to X-coordinates [0, 1, 2, ...]
        feature_to_x = {feat: i for i, feat in enumerate(self.features)}
        df_melted["X_idx"] = df_melted["Feature"].map(feature_to_x)

        np.random.seed(42)  # for reproducible jitter
        df_melted["X_jittered"] = df_melted["X_idx"] + np.random.uniform(
            -0.18, 0.18, len(df_melted)
        )

        plt.figure(figsize=(15, 8))
        sns.set_style("whitegrid")
        feature_colors = sns.color_palette("tab20", len(self.features))

        # 4. Plot the proxy ELA values
        for i, feat in enumerate(self.features):
            feat_data = df_melted[df_melted["Feature"] == feat]
            plt.scatter(
                feat_data["X_jittered"],
                feat_data["Value"],
                color=feature_colors[i],
                alpha=0.4,
                s=25,
                marker="o",
                edgecolors="none",
                zorder=2,
            )

        target_problems = {
            "Problem 1": (self.original_minmaxEla_p1, "*", 180),
            "Problem 2": (self.original_minmaxEla_p2, "X", 120),
            "Problem 3": (self.original_minmaxEla_p3, "D", 100),
        }

        # 6. Plot original ELA values
        for p_name, (p_dict, marker, size) in target_problems.items():
            for feat, val in p_dict.items():
                if feat in feature_to_x:
                    x_coord = feature_to_x[feat]
                    feat_idx = self.features.index(feat)

                    plt.scatter(
                        x_coord,
                        val,
                        color=feature_colors[feat_idx],
                        marker=marker,
                        s=size,
                        edgecolors="black",
                        linewidths=1.5,
                        zorder=5,  # Keep them on top
                    )

        plt.title(
            "ELA Feature Diversity (Original vs. Proxy)",
            fontsize=14,
            fontweight="bold",
            pad=15,
        )
        plt.ylabel("Min-max Feature Value", fontsize=12)
        plt.xlabel("ELA Features", fontsize=12)

        plt.xticks(
            ticks=range(len(self.features)),
            labels=self.features,
            rotation=35,
            ha="right",
            fontsize=10,
        )
        plt.xlim(-0.5, len(self.features) - 0.5)

        legend_elements = [
            Line2D(
                [0],
                [0],
                marker="o",
                color="w",
                markerfacecolor="gray",
                markersize=6,
                alpha=0.6,
                label="Initial Proxies",
            ),
            Line2D(
                [0],
                [0],
                marker="*",
                color="w",
                markerfacecolor="black",
                markeredgecolor="black",
                markersize=12,
                label="MB1",
            ),
            Line2D(
                [0],
                [0],
                marker="X",
                color="w",
                markerfacecolor="black",
                markeredgecolor="black",
                markersize=10,
                label="MB2",
            ),
            Line2D(
                [0],
                [0],
                marker="D",
                color="w",
                markerfacecolor="black",
                markeredgecolor="black",
                markersize=9,
                label="MB3",
            ),
        ]
        plt.legend(handles=legend_elements, loc="upper right", frameon=True, fontsize=11)

        plt.tight_layout()
        filename = f'{self.save_folder_name}/parent_ela_diversity.png'
        plt.savefig(filename, dpi=900)

        return all_initial_elas

    def get_podium_median_worst(self, individuals):
        """
        Extract the best 3, median 3, and worst 3 proxies
        """
        df_sorted = pd.DataFrame(individuals).sort_values(by='fitness').reset_index(drop=True)

        # Get rid of identical IDs and proxy code
        df_sorted = df_sorted.drop_duplicates(subset='id').drop_duplicates(subset='code')

        podium_proxies = []
        median_proxies = []
        worst_proxies = []

        # Podium
        for id, row in df_sorted.iterrows():
            if self._is_proxy_valid(row['code'], row['name']):
                podium_proxies.append(row)
            if len(podium_proxies) == 3:
                break

        # Worst
        for id, row in df_sorted[::-1].iterrows():  # Reverse traversal
            if self._is_proxy_valid(row['code'], row['name']):
                worst_proxies.append(row)  # Goes 1) worst, 2) second-worst, 3) third-worst
            if len(worst_proxies) == 3:
                break

        mid_start = len(df_sorted) // 2

        # Absolute middle
        idx = mid_start
        med2_row = None
        med2_idx = None
        while idx < len(df_sorted):
            row = df_sorted.iloc[idx]
            if self._is_proxy_valid(row['code'], row['name']):
                med2_row = row
                med2_idx = idx
                break
            idx += 1

        if med2_row is not None:
            # Going backward (better) for med1
            idx = med2_idx - 1
            med1_row = None
            while idx >= 0:
                row = df_sorted.iloc[idx]
                if self._is_proxy_valid(row['code'], row['name']):
                    med1_row = row
                    break
                idx -= 1

            # Going forward (worse) for med2
            idx = med2_idx + 1
            med3_row = None
            while idx < len(df_sorted):
                row = df_sorted.iloc[idx]
                if self._is_proxy_valid(row['code'], row['name']):
                    med3_row = row
                    break
                idx += 1

            if med1_row is not None: median_proxies.append(med1_row)
            median_proxies.append(med2_row)
            if med3_row is not None: median_proxies.append(med3_row)

        df_pod = pd.DataFrame(podium_proxies) if podium_proxies else pd.DataFrame()
        df_med = pd.DataFrame(median_proxies) if median_proxies else pd.DataFrame()
        df_wst = pd.DataFrame(worst_proxies) if worst_proxies else pd.DataFrame()

        if not df_pod.empty: df_pod['standing'] = [f'pod{i + 1}' for i in range(len(df_pod))]
        if not df_med.empty: df_med['standing'] = [f'med{i + 1}' for i in range(len(df_med))]
        if not df_wst.empty: df_wst['standing'] = [f'worst{i + 1}' for i in range(len(df_wst))]

        df_standings = pd.concat([df_pod, df_med, df_wst])

        return df_standings

    def _is_proxy_valid(self, code, name):
        """
        Validates a proxy by testing negative and positive inputs
        """
        try:
            # Create an isolated environment to execute the proxy string
            local_env = {}
            exec(code, globals(), local_env)
            if name not in local_env:
                return False

            proxy_class = local_env[name]
            proxy_instance = proxy_class(dim=5)
            problem = proxy_instance.f

            test_points = np.random.uniform(-5.0, 5.0, (100, 5))

            for pt in test_points:
                val = problem(pt)
                if np.isnan(val) or np.isinf(val):
                    return False
            return True
        except Exception:
            return False

    # region PROGRESSION PLOTS
    def save_individual_legend(self, save_folder):
        """
        Generates a separate, standalone horizontal (3x1 layout) legend
        figure for the individual progression graphs.
        """
        import matplotlib.lines as mlines

        # Wide but short canvas sizing
        fig, ax = plt.subplots(figsize=(12, 1))
        ax.axis('off')

        # Explicitly reconstruct handles matching the plot design aesthetics
        h_raw = mlines.Line2D([], [], color='#ff7f0e', alpha=0.7, linewidth=1.5, label='Mean Individual Fitness')
        h_best = mlines.Line2D([], [], color='#1f77b4', linewidth=2.5, label='Mean Best-so-Far Fitness')
        h_gb = mlines.Line2D([], [], color='#2ca02c', marker='o', linestyle='None', markersize=12, label='Global Best')

        # Create single row layout via ncol=3
        ax.legend(handles=[h_raw, h_best, h_gb], loc='center', ncol=3,
                  fontsize=18, frameon=True, facecolor='white', edgecolor='none')

        plt.tight_layout()
        filename = f'{self.save_folder_name}/{save_folder}/legend_progression.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Generated separate progression legend: {filename}")

    def save_feature_legend(self, save_folder):
        """
        Generates a separate, standalone wide matrix legend figure
        (2 rows x 6 columns layout) for the 11 ELA features.
        """
        import matplotlib.lines as mlines

        # Wide canvas designed to stretch cleanly under a 3x3 layout block
        fig, ax = plt.subplots(figsize=(18, 1.5))
        ax.axis('off')

        color_palette = plt.cm.tab20(np.linspace(0, 1, len(self.features)))
        handles = []

        for idx, feat in enumerate(self.features):
            h = mlines.Line2D([], [], color=color_palette[idx], linewidth=3.0, label=feat)
            handles.append(h)

        # ncol=6 forces 11 items cleanly into 2 horizontal rows (6 top, 5 bottom)
        ax.legend(handles=handles, loc='center', ncol=6,
                  fontsize=14, frameon=True, facecolor='white', edgecolor='none')

        plt.tight_layout()
        filename = f'{self.save_folder_name}/{save_folder}/legend_features.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Generated separate feature legend: {filename}")

    def plot_individual_progression(self, global_stats, save_folder, clean_layout=False):
        """
        Generates 9 graphs tracking raw fitness vs. best-so-far convergence.
        """
        full_path = f'{self.save_folder_name}/{save_folder}'
        if not os.path.exists(full_path):
            os.mkdir(full_path)
        max_ind_bound, max_fit_bound = global_stats

        for problem_ in self.log.keys():
            if 'total' in problem_:
                continue
            for config_ in self.log[problem_].keys():
                if 'total' in config_:
                    continue

                runs_dict = self.log[problem_][config_]
                run_keys = [k for k in runs_dict.keys() if 'total' not in k]
                if not run_keys:
                    continue

                min_len = min(len(runs_dict[rk]) for rk in run_keys)

                raw_matrix = []
                best_matrix = []

                for rk in run_keys:
                    run_log = runs_dict[rk][:min_len]
                    fitness_seq = [ind['fitness'] for ind in run_log]

                    best_seq = []
                    current_best = float('inf')
                    for fit in fitness_seq:
                        if fit < current_best:
                            current_best = fit
                        best_seq.append(current_best)

                    raw_matrix.append(fitness_seq)
                    best_matrix.append(best_seq)

                raw_matrix = np.array(raw_matrix)
                best_matrix = np.array(best_matrix)

                mean_raw = np.mean(raw_matrix, axis=0)
                mean_best = np.mean(best_matrix, axis=0)

                best_fitness = mean_best[:max_ind_bound].min()
                best_ind = mean_best[:max_ind_bound].argmin()

                se_raw = np.std(raw_matrix, axis=0) / np.sqrt(len(run_keys))
                se_best = np.std(best_matrix, axis=0) / np.sqrt(len(run_keys))

                individuals_xaxis = np.arange(1, min_len + 1)

                plt.figure(figsize=(10, 6))
                plt.style.use('seaborn-v0_8-whitegrid')
                fig, ax = plt.subplots(figsize=(10, 6))

                ax.plot(individuals_xaxis, mean_raw, color='#ff7f0e', alpha=0.7, linewidth=1.5)
                ax.fill_between(individuals_xaxis, mean_raw - se_raw, mean_raw + se_raw, color='#ff7f0e', alpha=0.15)

                ax.plot(individuals_xaxis, mean_best, color='#1f77b4', linewidth=2.5)
                ax.fill_between(individuals_xaxis, mean_best - se_best, mean_best + se_best, color='#1f77b4', alpha=0.2)

                ax.scatter(best_ind, best_fitness, color='#2ca02c', s=100, zorder=5)

                ax.text(best_ind, best_fitness - (max_fit_bound * 0.02), f'{best_fitness:.3f}', color='#006400',
                        fontweight='bold',
                        ha='center', va='top', fontsize=28)

                ax.set_xlim(1, max_ind_bound)
                ax.set_ylim(0, max_fit_bound * 1.05)

                ax.set_title(f'{problem_} ({config_})', fontsize=26, fontweight='bold',
                             pad=12)

                if clean_layout and config_ != "1+1":
                    ax.set_ylabel('')
                    ax.yaxis.set_tick_params(labelleft=True, labelsize=20)
                else:
                    ax.set_ylabel('Fitness', fontsize=22, labelpad=8, fontweight='bold')
                    ax.yaxis.set_tick_params(labelleft=True, labelsize=20)

                if clean_layout and problem_ != "p3":
                    ax.set_xlabel('')
                    ax.xaxis.set_tick_params(labelbottom=True, labelsize=20)
                else:
                    ax.set_xlabel('Individual', fontsize=22, labelpad=8, fontweight='bold')
                    ax.xaxis.set_tick_params(labelbottom=True, labelsize=20)

                plt.tight_layout()
                suffix = "_clean" if clean_layout else ""
                filename = f'{full_path}/progression_{problem_}_{config_}{suffix}.png'
                plt.savefig(filename, dpi=300, bbox_inches='tight')
                plt.close()
                print(f"Generated progression graph: {filename}")

    def plot_feature_progression(self, global_max_fit, max_ind_bound, save_folder, clean_layout=False):
        """
        Generates 9 graphs tracking the mean best-so-far convergence curve for features.
        """
        full_path = f'{self.save_folder_name}/{save_folder}'
        if not os.path.exists(full_path):
            os.mkdir(full_path)

        for problem_ in self.log.keys():
            if 'total' in problem_:
                continue
            for config_ in self.log[problem_].keys():
                if 'total' in config_:
                    continue

                runs_dict = self.log[problem_][config_]
                run_keys = [k for k in runs_dict.keys() if 'total' not in k]
                if not run_keys:
                    continue

                min_len = min(len(runs_dict[rk]) for rk in run_keys)
                length = min(min_len, max_ind_bound)
                individuals_xaxis = np.arange(1, length + 1)

                plt.figure(figsize=(10, 10))
                plt.style.use('seaborn-v0_8-whitegrid')
                fig, ax = plt.subplots(figsize=(10, 10))

                color_palette = plt.cm.tab20(np.linspace(0, 1, len(self.features)))

                for idx, feat in enumerate(self.features):
                    config_feat_matrix = []
                    for rk in run_keys:
                        run_log = runs_dict[rk][:length]
                        feat_seq = [ind["metadata"]["Absolute min-max distances"][feat] for ind in run_log]

                        best_seq = []
                        current_best = float('inf')
                        for val in feat_seq:
                            if val < current_best:
                                current_best = val
                            best_seq.append(current_best)
                        config_feat_matrix.append(best_seq)

                    mean_best_feat = np.mean(config_feat_matrix, axis=0)
                    ax.plot(individuals_xaxis, mean_best_feat, color=color_palette[idx], linewidth=2.5, alpha=0.9)

                ax.set_xlim(1, max_ind_bound)
                ax.set_ylim(0, global_max_fit * 1.05)

                ax.set_title(f'{problem_} ({config_})', fontsize=26, fontweight='bold',
                             pad=12)

                if clean_layout and config_ != "1+1":
                    ax.set_ylabel('')
                    ax.yaxis.set_tick_params(labelleft=True, labelsize=20)
                else:
                    ax.set_ylabel('Fitness', fontsize=22, labelpad=8, fontweight='bold')
                    ax.yaxis.set_tick_params(labelleft=True, labelsize=20)

                if clean_layout and problem_ != "p3":
                    ax.set_xlabel('')
                    ax.xaxis.set_tick_params(labelbottom=True, labelsize=20)
                else:
                    ax.set_xlabel('Individual', fontsize=22, labelpad=8, fontweight='bold')
                    ax.xaxis.set_tick_params(labelbottom=True, labelsize=20)

                plt.tight_layout()
                suffix = "_clean" if clean_layout else ""
                filename = f'{full_path}/features_{problem_}_{config_}{suffix}.png'
                plt.savefig(filename, dpi=300, bbox_inches='tight')
                plt.close()
                print(f"Generated feature progression graph: {filename}")

    def compare_experiments_by_individual(self):
        """
        Computes uniform axis limits across all 3x3 configurations based
        on individual indexes and the maximum mean fitness observed.
        """
        max_individuals = 99999
        global_max_mean_fitness = 0.0

        for problem_ in self.log.keys():
            if 'total' in problem_:
                continue
            for config_ in self.log[problem_].keys():
                if 'total' in config_:
                    continue

                runs_dict = self.log[problem_][config_]
                run_keys = [k for k in runs_dict.keys() if 'total' not in k]
                if not run_keys:
                    continue

                # Align to the shortest run in this configuration block
                min_len = min(len(runs_dict[rk]) for rk in run_keys)
                # max_individuals = max(max_individuals, min_len)
                max_individuals = min(max_individuals, min_len)

                # Track fitness values to determine maximum y-bound
                config_fitness_matrix = []
                for rk in run_keys:
                    config_fitness_matrix.append([ind['fitness'] for ind in runs_dict[rk][:min_len]])

                if config_fitness_matrix:
                    mean_profile = np.mean(config_fitness_matrix, axis=0)
                    global_max_mean_fitness = max(global_max_mean_fitness, np.max(mean_profile))

        return max_individuals, global_max_mean_fitness

    def compare_features_by_individual(self, max_ind_bound):
        """
        Computes the global maximum fitness across all 11 features, problems,
        and configurations to establish a uniform Y-axis bound.
        """
        global_max_feature_fitness = 0.0

        for problem_ in self.log.keys():
            if 'total' in problem_:
                continue
            for config_ in self.log[problem_].keys():
                if 'total' in config_:
                    continue

                runs_dict = self.log[problem_][config_]
                run_keys = [k for k in runs_dict.keys() if 'total' not in k]
                if not run_keys:
                    continue

                min_len = min(len(runs_dict[rk]) for rk in run_keys)
                length = min(min_len, max_ind_bound)

                # Track best-so-far profiles per feature to find the highest mean point
                for feat in self.features:
                    config_feat_matrix = []
                    for rk in run_keys:
                        run_log = runs_dict[rk][:length]
                        # Extract the explicit absolute min-maxed distance metric
                        feat_seq = [ind["metadata"]["Absolute min-max distances"][feat] for ind in run_log]

                        best_seq = []
                        current_best = float('inf')
                        for val in feat_seq:
                            if val < current_best:
                                current_best = val
                            best_seq.append(current_best)
                        config_feat_matrix.append(best_seq)

                    if config_feat_matrix:
                        mean_profile = np.mean(config_feat_matrix, axis=0)
                        global_max_feature_fitness = max(global_max_feature_fitness, np.max(mean_profile))

        return global_max_feature_fitness

    # endregion PROGRESSION PLOTS

    def save_feature_difficulty_ranking(self, exp_mapping, output_filename='llamea_tables/feature_difficulty_ranking.csv'):
        """
        Export table with best fitness per feature
        """
        feature_data = {}

        for alias, exp_name in exp_mapping.items():
            if exp_name not in self.experiments_data:
                # print(f"Warning: Data for {exp_name} not found. Skipping {alias}.")
                continue

            df = self.experiments_data[exp_name]
            feature_data[alias] = {}

            for feat in self.features:
                if feat in df.columns:
                    feature_data[alias][feat] = df[feat].min()
                else:
                    feature_data[alias][feat] = np.nan

        df_ranking = pd.DataFrame(feature_data)

        df_ranking['overall_mean_error'] = df_ranking.mean(axis=1)
        df_ranking = df_ranking.sort_values(by='overall_mean_error', ascending=False)

        df_ranking = df_ranking.drop(columns=['overall_mean_error'])
        df_ranking.index.name = 'Feature'
        df_ranking = df_ranking.round(3)

        df_ranking.to_csv(output_filename)
        # print(f"\n--- Feature Optimization Difficulty Ranking Saved to '{output_filename}' ---")
        # print(df_ranking.to_string())

        # Save Latex file
        df_ranking.index = df_ranking.index.str.replace('_', r'\_')

        latex_code = df_ranking.to_latex(
            float_format="%.3f",
            column_format="lrrr",
            caption="LLaMEA Loop Best Achieved Absolute Feature Error Across Problem Profiles",
            label="tab:feature_difficulty",
            position="th"
        )

        with open('llamea_tables/feature_difficulty.tex', 'w', encoding='utf-8') as f:
            f.write(latex_code)

        # print("LaTeX table code successfully saved to 'feature_difficulty.tex'")
        # print("\nGenerated LaTeX Code:\n")
        print(latex_code)

        return df_ranking

    def compute_AOCC(self, path_convergence_data, save_path):
        analysis_path = path_convergence_data

        aocc_records = []

        for seed in os.listdir(analysis_path):
            for p in os.listdir(f'{analysis_path}/{seed}'):
                print(f'\n\n### SEED {seed} PROBLEM {p} ###\n\n')
                if p == 'p1' or p == 'p2':
                    max_evals = 150
                else:
                    continue  # missing for now
                    # max_evals = 450

                for standing in os.listdir(f'{analysis_path}/{seed}/{p}'):
                    for algo in os.listdir(f'{analysis_path}/{seed}/{p}/{standing}'):
                        for f in os.listdir(f'{analysis_path}/{seed}/{p}/{standing}/{algo}'):
                            if f[:3] == 'IOH':
                                continue
                            for dat in os.listdir(f'{analysis_path}/{seed}/{p}/{standing}/{algo}/{f}'):
                                dat_path = f'{analysis_path}/{seed}/{p}/{standing}/{algo}/{f}/{dat}'

                                df = pd.read_csv(dat_path, sep=" ")
                                df = df[:max_evals]

                                evaluations = df["evaluations"].to_numpy()
                                raw_y = df["raw_y"].to_numpy()

                                best_so_far = []
                                bsf = 99999999
                                for y_ in raw_y:
                                    if y_ < bsf:
                                        best_so_far.append(y_)
                                        bsf = y_
                                    else:
                                        best_so_far.append(bsf)

                                best_so_far = pd.DataFrame(best_so_far).to_numpy().flatten()

                                bsf_range = best_so_far.max() - best_so_far.min()
                                if bsf_range == 0:
                                    norm_bsf = np.zeros_like(best_so_far)
                                else:
                                    norm_bsf = (best_so_far - best_so_far.min()) / bsf_range

                                norm_evals = (evaluations - evaluations.min()) / (
                                        evaluations.max() - evaluations.min()
                                )

                                auc = np.trapz(norm_bsf, norm_evals)
                                aocc = 1 - auc

                                aocc_records.append({
                                    'problem': p,
                                    'standing': standing,
                                    'algo': algo,
                                    'seed': seed,
                                    'aocc': aocc
                                })

        df_long = pd.DataFrame(aocc_records)

        df_wide = df_long.pivot(
            index=['problem', 'standing', 'algo'],
            columns='seed',
            values='aocc'
        ).reset_index()

        seed_cols = [c for c in df_wide.columns if c not in ['problem', 'standing', 'algo']]
        df_wide['mean'] = df_wide[seed_cols].mean(axis=1)
        filename = f'{self.save_folder_name}/{save_path}'
        df_wide.to_csv(filename)

        return df_wide

    def compare_AOCCs(self, path_aocc_results, save_path):
        full_path = f'{self.save_folder_name}/{path_aocc_results}'
        aocc_results = pd.read_csv(full_path)
        for p in [1, 2]:
            optimizers = {'botorch': {}, 'cmaes': {}, 'de': {}, 'one_plus_one': {}, 'turbo1': {}, 'baxus': {}}
            aocc_p = aocc_results.loc[(aocc_results['problem'] == f'p{p}')]
            for standing in [f'MB{p}', 'pod1', 'pod2', 'pod3', 'med1', 'med2', 'med3', 'worst1', 'worst2', 'worst3']:
                aocc_p_standing = aocc_p.loc[(aocc_p['standing'] == standing)].sort_values(by='mean')[::-1].reset_index()
                # From best to worst
                for i, algo in aocc_p_standing[['algo']].iterrows():
                    rank = i + 1
                    algo = algo.values[0]
                    optimizers[algo][standing] = rank

            # Compute Kendall's tau
            taus = {}
            df_ranking = pd.DataFrame(optimizers).T
            df_MB = df_ranking.iloc[:, 0]
            df_proxies = df_ranking.iloc[:, 1:]
            for standing in df_proxies:
                standings_p = self.standings_total[f'p{p}']
                fitness = standings_p.loc[standings_p['standing'] == standing]['fitness'].values[0]
                taus[f'MB{p}_{standing}'] = {}
                ranking = df_proxies[standing].to_numpy()
                tau, p_value = kendalltau(ranking, df_MB.to_numpy())
                taus[f'MB{p}_{standing}']['tau'] = tau
                taus[f'MB{p}_{standing}']['p'] = p_value
                taus[f'MB{p}_{standing}']['fitness'] = fitness

            df_taus = pd.DataFrame(taus).T
            filename = f'{self.save_folder_name}/{save_path}_p{p}.csv'
            df_taus.to_csv(filename)

    def scatter_fitness_kendall(self, path_kendall_results, save_path):
        for p in [1, 2]:
            filename = f'{self.save_folder_name}/{path_kendall_results}'
            df_taus = pd.read_csv(f'{filename}_p{p}.csv', index_col=0)
            tau = df_taus['tau'].to_numpy()
            fitness = df_taus['fitness'].to_numpy()
            standings = df_taus.index.to_numpy()
            ranks = pd.Series([i for i, s in enumerate(standings)])
            norm_ranks = (ranks - ranks.min()) / (ranks.max() - ranks.min())

            fig, ax = plt.subplots(figsize=(9, 6))
            cmap = plt.get_cmap("viridis")

            jitter_amplitude_x = 0.015
            jitter_amplitude_y = (fitness.max() - fitness.min()) * 0.015

            rng = np.random.default_rng(seed=42)

            for i in range(len(tau)):
                # Generate a tiny offset for overlapping proxies
                jx = rng.uniform(-jitter_amplitude_x, jitter_amplitude_x)
                jy = rng.uniform(-jitter_amplitude_y, jitter_amplitude_y)
                plot_x = tau[i] + jx
                plot_y = fitness[i] + jy

                ax.scatter(
                    plot_x,
                    plot_y,
                    color=cmap(norm_ranks[i]),
                    s=350,
                    alpha=0.8,
                    edgecolors="black",
                    linewidths=0.5
                )

                ax.text(
                    plot_x,
                    plot_y,
                    str(ranks[i]+1),
                    color="white",
                    fontsize=9,
                    fontweight="bold",
                    va="center",
                    ha="center"
                )

            # Trend line
            m, b = np.polyfit(tau, fitness, 1)
            x_line = np.linspace(tau.min(), tau.max(), 100)
            y_line = m * x_line + b
            ax.line = ax.plot(
                x_line,
                y_line,
                color="red",
                linestyle="--",
                linewidth=2,
                alpha=0.7,
                label=f"Trend (slope: {m:.2f})"
            )

            # PC values
            ax.set(
                title=f"Kendall's tau vs. fitness (p{p})",
                xlabel=f"Kendall's tau",
                ylabel=f"Fitness",
            )

            plt.tight_layout()
            plt.savefig(f"{self.save_folder_name}/{save_path}_p{p}.png", dpi=900)
            plt.close()


if __name__ == "__main__":
    log_dir = "../ELA_for_MECHBench/LLaMEA_ELA/exps_0704"
    save_folder_name = 'results'
    aocc_path = '../ELA_for_MECHBench/LLaMEA_ELA/proxies'
    analyzer = LLaMEAAnalyzer(
        log_dir=log_dir,
        save_folder_name=save_folder_name,
        aocc_path=aocc_path
    )

    analyzer.load_logs()
    log = analyzer.log
    df = analyzer.experiments_data

    analyzer.run(
        progress_plots=False,
        pca_plots=True,
        diversity_plots=False,
        get_proxy_standings=False,
        compute_aocc=False,
        compare_aocc=False,
        kendall_fitness_scatter=False
    )

    sys.exit(0)

    # analyzer.run(
    #     progress_plots=False,
    #     get_proxy_standings=True,
    #     compute_aocc=False,
    #     compare_aocc=True
    # )

    analyzer.load_logs()
    for p in analyzer.log:
        for config in analyzer.log[p]:
            if 'total' not in config:
                for inds in analyzer.log[p][config]:
                    if 'total' in inds:
                        analyzer.pca(analyzer.log[p][config][inds], name_=f'{p}_{config}')

    sys.exit(0)

    base_dir = "../ELA_for_MECHBench/LLaMEA_ELA/exps_0704"
    analyzer = LLaMEAAnalyzer(save_folder_name='')
    analyzer.load_logs(base_dir)

    aocc_path = '../ELA_for_MECHBench/LLaMEA_ELA/proxies'
    # aoccs = analyzer.compute_AOCC(aocc_path)
    # analyzer.compare_AOCCs('aocc_results_2.csv')

    log = analyzer.log
    exp_data = analyzer.experiments_data

    p1_total = log['p1']['p1_total']
    p2_total = log['p2']['p2_total']
    p3_total = log['p3']['p3_total']

    pod1, med1, wrs1 = analyzer.get_podium_median_worst(p1_total)
    print(pod1['id'])
    pod2, med2, wrs2 = analyzer.get_podium_median_worst(p2_total)
    print(pod2['id'])
    pod3, med3, wrs3 = analyzer.get_podium_median_worst(p3_total)
    print(pod3['id'])

    sys.exit(0)

    initial_elas = analyzer.plot_initial_diversity()

    print("\n--- Computing Uniform Bounds Across All Experiments ---")
    max_ind, max_fit = analyzer.compare_experiments_by_individual()
    print(f'MAX INDIVIDUAL BOUND {max_ind}')
    max_feat_fit = analyzer.compare_features_by_individual(max_ind_bound=max_ind)

    # 1. Process Core Progression Figures & Legend
    print("\n--- Generating Consolidated Progression Plots & Legend ---")
    analyzer.plot_individual_progression((max_ind, max_fit), clean_layout=True)
    analyzer.save_individual_legend()

    # 2. Process Feature Progression Figures & Legend
    print("\n--- Generating Per-Feature Convergence Plots & Legend ---")
    analyzer.plot_feature_progression(global_max_fit=max_feat_fit, max_ind_bound=max_ind, clean_layout=True)
    analyzer.save_feature_legend()

    print("\nProcessing completely successful!")
    sys.exit(0)

    def threshold_experiment(individuals):
        filter_thresholds = [0.0, 0.1, 0.3, 0.5, 0.7, 0.9]

        for thr in filter_thresholds:
            podium, median, worst, filtered_df = analyzer.get_podium_median_worst(individuals, filter_threshold=thr)
            print(f'--- THRESHOLD {thr} * SD ---\n')
            print(f'Podium fitnesses:\n {podium["fitness"]} \nSD {float(podium["fitness"].std().round(3))}')
            print(f'Median fitnesses:\n {median["fitness"]} \nSD {float(median["fitness"].std().round(3))}')
            print(f'Worst fitnesses:\n {worst["fitness"]} \nSD {float(worst["fitness"].std().round(3))}')
            print(f'Len Filtered df: {len(filtered_df)} (how many total proxies there were to choose from)')
            print(f'\n\n')

    for problem in ['p1', 'p2', 'p3']:
        problem_total = log[problem][f'{problem}_total']
        print(f'\n +++ CHECKING {problem} TOTAL (len {len(problem_total)}) +++ \n ')
        threshold_experiment(problem_total)
        for config_name, config_log in log[problem].items():
            if 'total' not in config_name:
                config_total = config_log[f'{config_name}_total']
                print(f'\n +++ CHECKING {config_name} TOTAL (len {len(config_total)}) +++ \n ')
                threshold_experiment(config_total)

    sys.exit(0)

    # region 0630
    base_dir = "../exps_06_30"
    analyzer = LLaMEAAnalyzer(save_folder_name='llamea_graphs/exps_06_30_new')
    os.makedirs(analyzer.save_folder_name, exist_ok=True)

    analyzer.load_logs(base_dir)

    print("\n--- Computing Uniform Bounds Across All Experiments ---")
    max_ind, max_fit = analyzer.compare_experiments_by_individual()
    print(f'MAX INDIVIDUAL BOUND {max_ind}')
    max_feat_fit = analyzer.compare_features_by_individual(max_ind_bound=max_ind)

    # 1. Process Core Progression Figures & Legend
    print("\n--- Generating Consolidated Progression Plots & Legend ---")
    analyzer.plot_individual_progression((max_ind, max_fit), clean_layout=True)
    analyzer.save_individual_legend()

    # 2. Process Feature Progression Figures & Legend
    print("\n--- Generating Per-Feature Convergence Plots & Legend ---")
    analyzer.plot_feature_progression(global_max_fit=max_feat_fit, max_ind_bound=max_ind, clean_layout=True)
    analyzer.save_feature_legend()

    print("\nProcessing completely successful!")
    sys.exit(0)

    # endregion 0630

    # region 0701
    base_dir = "../exps_0701"
    analyzer = LLaMEAAnalyzer(save_folder_name='llamea_graphs/exps_07_01')
    os.makedirs(analyzer.save_folder_name, exist_ok=True)

    analyzer.load_logs(base_dir)

    print("\n--- Computing Uniform Bounds Across All Experiments ---")
    _, max_fit = analyzer.compare_experiments_by_individual()
    max_ind = 129  # Variance exception anchor
    max_feat_fit = analyzer.compare_features_by_individual(max_ind_bound=max_ind)

    # 1. Process Core Progression Figures & Legend
    print("\n--- Generating Consolidated Progression Plots & Legend ---")
    analyzer.plot_individual_progression((max_ind, max_fit), clean_layout=True)
    analyzer.save_individual_legend()

    # 2. Process Feature Progression Figures & Legend
    print("\n--- Generating Per-Feature Convergence Plots & Legend ---")
    analyzer.plot_feature_progression(global_max_fit=max_feat_fit, max_ind_bound=max_ind, clean_layout=True)
    analyzer.save_feature_legend()

    print("\nProcessing completely successful!")
    sys.exit(0)

    # endregion 0701

    print("\n--- Computing Global Stats Across Experiments ---")
    problem_stats = analyzer.compare_experiments(exp_names)

    print("\n--- Generating Plots ---")
    for name in exp_names:
        folder_name = os.path.basename(name)
        clean_suffix = f"{folder_name}"

        # Generate the total fitness and feature plots
        analyzer.generate_plots(name, problem_stats, save_suffix=clean_suffix, plot_type='total')
        analyzer.generate_plots(name, problem_stats, save_suffix=clean_suffix, plot_type='all_features')