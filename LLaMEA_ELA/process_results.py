import json
import os
import numpy as np
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import sys
from sklearn import metrics
from sklearn.decomposition import PCA
import seaborn as sns
from matplotlib.lines import Line2D
from scipy.stats import kendalltau
import pflacco.classical_ela_features as ela


class LLaMEAAnalyzer:
    def __init__(self, log_dir,
                 save_folder_name,
                 aocc_path,
                 updated_stats_path='../Folder_Points/500D/by_size/500D/500d_updated_ELA_stats.csv',
                 original_stats_path='ela_feature_stats.csv'
                 ):
        self.log_dir = log_dir
        print(self.log_dir)
        self.save_folder_name = save_folder_name
        if not os.path.exists(save_folder_name):
            os.mkdir(save_folder_name)

        self.aocc_path = aocc_path
        self.updated_stats_path = updated_stats_path
        self.original_stats_path = original_stats_path

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

        # self.MB1_ela_500d = pd.read_csv('../Folder_Points/500D/data_p1/ELA/ela_500d5_p1_seed1312.csv')
        # self.MB2_ela_500d = pd.read_csv('../Folder_Points/500D/data_p2/ELA/ela_500d5_p2_seed1312.csv')
        # self.MB3_ela_500d = pd.read_csv('../Folder_Points/500D/data_p3/ELA/ela_500d15_p3_seed1312.csv')

        self.original_minmaxEla_p1 = {'disp.ratio_mean_02': 0.3180841545512229, 'ela_distr.skewness': 0.1293188522940492, 'ela_meta.lin_simple.adj_r2': 0.2210812231592529, 'ela_meta.lin_simple.intercept': 0.7444454923627558, 'ela_meta.lin_simple.coef.max': 1.0, 'ela_meta.quad_simple.adj_r2': 0.2425517809797153, 'ic.eps_ratio': 1.0, 'ic.eps_s': 1.0, 'nbc.nb_fitness.cor': 0.5102519892845082, 'ela_level.mmce_qda_25': 0.2957746230906558, 'ela_level.lda_qda_25': 0.3331012892967914}
        self.original_minmaxEla_p2 = {'disp.ratio_mean_02': 0.613775757719448, 'ela_distr.skewness': 0.1919105264092217, 'ela_meta.lin_simple.adj_r2': 0.2228005657527632, 'ela_meta.lin_simple.intercept': 0.4325753309513677, 'ela_meta.lin_simple.coef.max': 0.3115486529327629, 'ela_meta.quad_simple.adj_r2': 0.2579866624338019, 'ic.eps_ratio': 0.864406779661017, 'ic.eps_s': 0.7478260869565218, 'nbc.nb_fitness.cor': 0.6089279644868683, 'ela_level.mmce_qda_25': 0.225352085399721, 'ela_level.lda_qda_25': 0.4880185824214766}
        self.original_minmaxEla_p3 = {'disp.ratio_mean_02': 0.8785028761364115, 'ela_distr.skewness': 0.1827705273439356, 'ela_meta.lin_simple.adj_r2': 0.0168121027022387, 'ela_meta.lin_simple.intercept': 0.2178719275405489, 'ela_meta.lin_simple.coef.max': 0.595020107122112, 'ela_meta.quad_simple.adj_r2': 0.4266757168517114, 'ic.eps_ratio': 1.0, 'ic.eps_s': 1.0, 'nbc.nb_fitness.cor': 0.3924693159004784, 'ela_level.mmce_qda_25': 0.7743123688965757, 'ela_level.lda_qda_25': 0.1753467427267984}

        self.standings_total = {}

        self.log = {}
        self.experiments_data = {}

        self.min_tau = 0
        self.max_tau = 0
        self.min_fit = 0
        self.max_fit = 0

        self.standings1 = pd.read_csv(f'{self.save_folder_name}/standings1.csv')
        self.standings2 = pd.read_csv(f'{self.save_folder_name}/standings2.csv')
        self.standings3 = pd.read_csv(f'{self.save_folder_name}/standings3.csv')

        self.standings_total['p1'] = self.standings1
        self.standings_total['p2'] = self.standings2
        self.standings_total['p3'] = self.standings3

        self.standings_ELA_values = {
            'p1': {
                'pod1': {
                    'disp.ratio_mean_02': 0.5447, 'ela_distr.skewness': 0.1172, 'ela_meta.lin_simple.adj_r2': 0.2974,
                    'ela_meta.lin_simple.intercept': 0.7985, 'ela_meta.lin_simple.coef.max': 1.0064,
                    'ela_meta.quad_simple.adj_r2': 0.2831, 'ic.eps_ratio': 1.0282, 'ic.eps_s': 0.7826,
                    'nbc.nb_fitness.cor': 0.3845, 'ela_level.mmce_qda_25': 0.5493, 'ela_level.lda_qda_25': 0.1464
                },
                'pod2': {
                    'disp.ratio_mean_02': 0.5539, 'ela_distr.skewness': 0.1172, 'ela_meta.lin_simple.adj_r2': 0.2978,
                    'ela_meta.lin_simple.intercept': 0.7999, 'ela_meta.lin_simple.coef.max': 1.0002,
                    'ela_meta.quad_simple.adj_r2': 0.2834, 'ic.eps_ratio': 1.0282, 'ic.eps_s': 0.7739,
                    'nbc.nb_fitness.cor': 0.3811, 'ela_level.mmce_qda_25': 0.5408, 'ela_level.lda_qda_25': 0.1464
                },
                'pod3': {
                    'disp.ratio_mean_02': 0.5598, 'ela_distr.skewness': 0.117, 'ela_meta.lin_simple.adj_r2': 0.2986,
                    'ela_meta.lin_simple.intercept': 0.8058, 'ela_meta.lin_simple.coef.max': 0.9788,
                    'ela_meta.quad_simple.adj_r2': 0.2841, 'ic.eps_ratio': 1.0339, 'ic.eps_s': 0.7739,
                    'nbc.nb_fitness.cor': 0.379, 'ela_level.mmce_qda_25': 0.5394, 'ela_level.lda_qda_25': 0.1484
                },
                'med1': {
                    'disp.ratio_mean_02': 0.4905, 'ela_distr.skewness': 0.2042, 'ela_meta.lin_simple.adj_r2': 0.0259,
                    'ela_meta.lin_simple.intercept': 0.1923, 'ela_meta.lin_simple.coef.max': 0.0105,
                    'ela_meta.quad_simple.adj_r2': 0.2018, 'ic.eps_ratio': 0.9209, 'ic.eps_s': 0.6957,
                    'nbc.nb_fitness.cor': 0.5843, 'ela_level.mmce_qda_25': 0.4775, 'ela_level.lda_qda_25': 0.2232
                },
                'med2': {
                    'disp.ratio_mean_02': 0.339, 'ela_distr.skewness': 0.1205, 'ela_meta.lin_simple.adj_r2': 0.0325,
                    'ela_meta.lin_simple.intercept': 0.6691, 'ela_meta.lin_simple.coef.max': 0.093,
                    'ela_meta.quad_simple.adj_r2': 0.4356, 'ic.eps_ratio': 1.0904, 'ic.eps_s': 0.8957,
                    'nbc.nb_fitness.cor': 0.0556, 'ela_level.mmce_qda_25': 0.8169, 'ela_level.lda_qda_25': 0.1194
                },
                'med3': {
                    'disp.ratio_mean_02': 0.7059, 'ela_distr.skewness': 0.1174, 'ela_meta.lin_simple.adj_r2': 0.094,
                    'ela_meta.lin_simple.intercept': 0.5307, 'ela_meta.lin_simple.coef.max': 0.396,
                    'ela_meta.quad_simple.adj_r2': 0.0822, 'ic.eps_ratio': 1.0621, 'ic.eps_s': 0.8348,
                    'nbc.nb_fitness.cor': 0.1426, 'ela_level.mmce_qda_25': 0.7676, 'ela_level.lda_qda_25': 0.1262
                },
                'worst1': {
                    'disp.ratio_mean_02': 0.7326, 'ela_distr.skewness': -2.0357, 'ela_meta.lin_simple.adj_r2': 0.028,
                    'ela_meta.lin_simple.intercept': 1.1077, 'ela_meta.lin_simple.coef.max': 0.0049,
                    'ela_meta.quad_simple.adj_r2': 0.0069, 'ic.eps_ratio': 0.2486, 'ic.eps_s': -0.0174,
                    'nbc.nb_fitness.cor': 0.8332, 'ela_level.mmce_qda_25': 0.8085, 'ela_level.lda_qda_25': 0.1202
                },
                'worst2': {
                    'disp.ratio_mean_02': 0.1521, 'ela_distr.skewness': 2.0331, 'ela_meta.lin_simple.adj_r2': 0.0286,
                    'ela_meta.lin_simple.intercept': -0.0043, 'ela_meta.lin_simple.coef.max': 0.0068,
                    'ela_meta.quad_simple.adj_r2': 0.0078, 'ic.eps_ratio': 0.0678, 'ic.eps_s': 0.0522,
                    'nbc.nb_fitness.cor': 1.0982, 'ela_level.mmce_qda_25': 0.6197, 'ela_level.lda_qda_25': 0.1717
                },
                'worst3': {
                    'disp.ratio_mean_02': 0.5516, 'ela_distr.skewness': -0.0072, 'ela_meta.lin_simple.adj_r2': 0.4446,
                    'ela_meta.lin_simple.intercept': 0.7292, 'ela_meta.lin_simple.coef.max': 1.2348,
                    'ela_meta.quad_simple.adj_r2': 0.672, 'ic.eps_ratio': 0.8079, 'ic.eps_s': 0.9043,
                    'nbc.nb_fitness.cor': 0.5462, 'ela_level.mmce_qda_25': -0.0535, 'ela_level.lda_qda_25': 8.9405
                }
            },
            'p2': {
                'pod1': {
                    'disp.ratio_mean_02': 0.5813, 'ela_distr.skewness': 0.1255, 'ela_meta.lin_simple.adj_r2': 0.2426,
                    'ela_meta.lin_simple.intercept': 0.4609, 'ela_meta.lin_simple.coef.max': 0.3901,
                    'ela_meta.quad_simple.adj_r2': 0.2371, 'ic.eps_ratio': 0.9153, 'ic.eps_s': 0.6783,
                    'nbc.nb_fitness.cor': 0.4554, 'ela_level.mmce_qda_25': 0.3549, 'ela_level.lda_qda_25': 0.2179
                },
                'pod2': {
                    'disp.ratio_mean_02': 0.6136, 'ela_distr.skewness': 0.1108, 'ela_meta.lin_simple.adj_r2': 0.2464,
                    'ela_meta.lin_simple.intercept': 0.4974, 'ela_meta.lin_simple.coef.max': 0.3916,
                    'ela_meta.quad_simple.adj_r2': 0.2284, 'ic.eps_ratio': 0.9209, 'ic.eps_s': 0.687,
                    'nbc.nb_fitness.cor': 0.4449, 'ela_level.mmce_qda_25': 0.3493, 'ela_level.lda_qda_25': 0.2193
                },
                'pod3': {
                    'disp.ratio_mean_02': 0.6118, 'ela_distr.skewness': 0.1112, 'ela_meta.lin_simple.adj_r2': 0.2455,
                    'ela_meta.lin_simple.intercept': 0.4954, 'ela_meta.lin_simple.coef.max': 0.3909,
                    'ela_meta.quad_simple.adj_r2': 0.2275, 'ic.eps_ratio': 0.9153, 'ic.eps_s': 0.687,
                    'nbc.nb_fitness.cor': 0.4414, 'ela_level.mmce_qda_25': 0.3535, 'ela_level.lda_qda_25': 0.2183
                },
                'med1': {
                    'disp.ratio_mean_02': 0.525, 'ela_distr.skewness': 0.1294, 'ela_meta.lin_simple.adj_r2': 0.0262,
                    'ela_meta.lin_simple.intercept': 0.5545, 'ela_meta.lin_simple.coef.max': 0.0223,
                    'ela_meta.quad_simple.adj_r2': 0.0048, 'ic.eps_ratio': 0.7571, 'ic.eps_s': 0.9304,
                    'nbc.nb_fitness.cor': 0.3323, 'ela_level.mmce_qda_25': 0.9282, 'ela_level.lda_qda_25': 0.1246
                },
                'med2': {
                    'disp.ratio_mean_02': 0.5566, 'ela_distr.skewness': 0.1067, 'ela_meta.lin_simple.adj_r2': 0.0276,
                    'ela_meta.lin_simple.intercept': 0.6409, 'ela_meta.lin_simple.coef.max': 0.0235,
                    'ela_meta.quad_simple.adj_r2': 0.0056, 'ic.eps_ratio': 0.8531, 'ic.eps_s': 0.8435,
                    'nbc.nb_fitness.cor': 0.2576, 'ela_level.mmce_qda_25': 0.9577, 'ela_level.lda_qda_25': 0.1199
                },
                'med3': {
                    'disp.ratio_mean_02': 0.913, 'ela_distr.skewness': 0.1963, 'ela_meta.lin_simple.adj_r2': 0.0259,
                    'ela_meta.lin_simple.intercept': 0.3646, 'ela_meta.lin_simple.coef.max': 0.0095,
                    'ela_meta.quad_simple.adj_r2': 0.0503, 'ic.eps_ratio': 0.9718, 'ic.eps_s': 0.8435,
                    'nbc.nb_fitness.cor': 0.2135, 'ela_level.mmce_qda_25': 0.8254, 'ela_level.lda_qda_25': 0.1179
                },
                'worst1': {
                    'disp.ratio_mean_02': 0.557, 'ela_distr.skewness': 0.1495, 'ela_meta.lin_simple.adj_r2': 0.9391,
                    'ela_meta.lin_simple.intercept': -0.1987, 'ela_meta.lin_simple.coef.max': 3.2852,
                    'ela_meta.quad_simple.adj_r2': 1.0, 'ic.eps_ratio': 0.9831, 'ic.eps_s': 0.7565,
                    'nbc.nb_fitness.cor': 0.748, 'ela_level.mmce_qda_25': 0.0746, 'ela_level.lda_qda_25': 0.2817
                },
                'worst2': {
                    'disp.ratio_mean_02': 0.557, 'ela_distr.skewness': 0.1495, 'ela_meta.lin_simple.adj_r2': 0.9391,
                    'ela_meta.lin_simple.intercept': -0.1987, 'ela_meta.lin_simple.coef.max': 3.2852,
                    'ela_meta.quad_simple.adj_r2': 1.0, 'ic.eps_ratio': 0.9831, 'ic.eps_s': 0.7565,
                    'nbc.nb_fitness.cor': 0.748, 'ela_level.mmce_qda_25': 0.0746, 'ela_level.lda_qda_25': 0.2817
                },
                'worst3': {
                    'disp.ratio_mean_02': 0.557, 'ela_distr.skewness': 0.1495, 'ela_meta.lin_simple.adj_r2': 0.9389,
                    'ela_meta.lin_simple.intercept': -0.199, 'ela_meta.lin_simple.coef.max': 3.2852,
                    'ela_meta.quad_simple.adj_r2': 1.0, 'ic.eps_ratio': 0.9831, 'ic.eps_s': 0.7565,
                    'nbc.nb_fitness.cor': 0.7481, 'ela_level.mmce_qda_25': 0.0746, 'ela_level.lda_qda_25': 0.2817
                }
            },
            'p3': {
                'pod1': {
                    'disp.ratio_mean_02': 0.9266, 'ela_distr.skewness': 0.1566, 'ela_meta.lin_simple.adj_r2': 0.1118,
                    'ela_meta.lin_simple.intercept': 0.1934, 'ela_meta.lin_simple.coef.max': 0.5889,
                    'ela_meta.quad_simple.adj_r2': 0.256, 'ic.eps_ratio': 1.0368, 'ic.eps_s': 0.9917,
                    'nbc.nb_fitness.cor': 0.1944, 'ela_level.mmce_qda_25': 0.7792, 'ela_level.lda_qda_25': 0.1679
                },
                'pod2': {
                    'disp.ratio_mean_02': 0.9628, 'ela_distr.skewness': 0.1564, 'ela_meta.lin_simple.adj_r2': 0.0953,
                    'ela_meta.lin_simple.intercept': 0.2209, 'ela_meta.lin_simple.coef.max': 0.5579,
                    'ela_meta.quad_simple.adj_r2': 0.2386, 'ic.eps_ratio': 1.0368, 'ic.eps_s': 1.0,
                    'nbc.nb_fitness.cor': 0.1943, 'ela_level.mmce_qda_25': 0.7827, 'ela_level.lda_qda_25': 0.1687
                },
                'pod3': {
                    'disp.ratio_mean_02': 0.9628, 'ela_distr.skewness': 0.1565, 'ela_meta.lin_simple.adj_r2': 0.0946,
                    'ela_meta.lin_simple.intercept': 0.2221, 'ela_meta.lin_simple.coef.max': 0.5538,
                    'ela_meta.quad_simple.adj_r2': 0.2426, 'ic.eps_ratio': 1.0368, 'ic.eps_s': 0.9917,
                    'nbc.nb_fitness.cor': 0.1932, 'ela_level.mmce_qda_25': 0.7827, 'ela_level.lda_qda_25': 0.1689
                },
                'med1': {
                    'disp.ratio_mean_02': 0.7889, 'ela_distr.skewness': 0.1569, 'ela_meta.lin_simple.adj_r2': 0.009,
                    'ela_meta.lin_simple.intercept': 0.6076, 'ela_meta.lin_simple.coef.max': 0.1745,
                    'ela_meta.quad_simple.adj_r2': 0.025, 'ic.eps_ratio': 1.0491, 'ic.eps_s': 1.0248,
                    'nbc.nb_fitness.cor': 0.1625, 'ela_level.mmce_qda_25': 0.8121, 'ela_level.lda_qda_25': 0.1644
                },
                'med2': {
                    'disp.ratio_mean_02': 0.6756, 'ela_distr.skewness': 0.1555, 'ela_meta.lin_simple.adj_r2': 0.0298,
                    'ela_meta.lin_simple.intercept': 0.6383, 'ela_meta.lin_simple.coef.max': 0.3224,
                    'ela_meta.quad_simple.adj_r2': 0.0309, 'ic.eps_ratio': 1.0245, 'ic.eps_s': 0.9835,
                    'nbc.nb_fitness.cor': 0.1204, 'ela_level.mmce_qda_25': 0.8116, 'ela_level.lda_qda_25': 0.1645
                },
                'med3': {
                    'disp.ratio_mean_02': 0.9679, 'ela_distr.skewness': 0.1568, 'ela_meta.lin_simple.adj_r2': 0.0204,
                    'ela_meta.lin_simple.intercept': 0.5179, 'ela_meta.lin_simple.coef.max': 0.184,
                    'ela_meta.quad_simple.adj_r2': 0.0211, 'ic.eps_ratio': 0.8528, 'ic.eps_s': 0.8843,
                    'nbc.nb_fitness.cor': 0.2451, 'ela_level.mmce_qda_25': 0.8116, 'ela_level.lda_qda_25': 0.1645
                },
                'worst1': {
                    'disp.ratio_mean_02': 0.0038, 'ela_distr.skewness': 0.9384, 'ela_meta.lin_simple.adj_r2': 0.0022,
                    'ela_meta.lin_simple.intercept': 0.0075, 'ela_meta.lin_simple.coef.max': 0.0119,
                    'ela_meta.quad_simple.adj_r2': 0.0201, 'ic.eps_ratio': 0.4908, 'ic.eps_s': 0.4298,
                    'nbc.nb_fitness.cor': 0.9105, 'ela_level.mmce_qda_25': 0.7596, 'ela_level.lda_qda_25': 0.1799
                },
                'worst2': {
                    'disp.ratio_mean_02': -0.1097, 'ela_distr.skewness': 0.1639, 'ela_meta.lin_simple.adj_r2': 0.2703,
                    'ela_meta.lin_simple.intercept': 0.5183, 'ela_meta.lin_simple.coef.max': 3.3632,
                    'ela_meta.quad_simple.adj_r2': 0.8505, 'ic.eps_ratio': 1.0061, 'ic.eps_s': 0.9669,
                    'nbc.nb_fitness.cor': 0.1574, 'ela_level.mmce_qda_25': 0.5882, 'ela_level.lda_qda_25': 0.2796
                },
                'worst3': {
                    'disp.ratio_mean_02': 0.5471, 'ela_distr.skewness': 0.1449, 'ela_meta.lin_simple.adj_r2': 0.77,
                    'ela_meta.lin_simple.intercept': 0.1634, 'ela_meta.lin_simple.coef.max': 4.6152,
                    'ela_meta.quad_simple.adj_r2': 0.9616, 'ic.eps_ratio': 0.9939, 'ic.eps_s': 0.9587,
                    'nbc.nb_fitness.cor': 0.3481, 'ela_level.mmce_qda_25': 0.2056, 'ela_level.lda_qda_25': 0.1935
                }
            }
        }

        def define_PCA_space():
            all_problem_data = []
            print(self.log)
            for p in self.log:
                for config in self.log[p]:
                    if 'total' not in config:
                        for inds in self.log[p][config]:
                            if 'total' in inds:
                                for individual in self.log[p][config][inds]:
                                    proxy_dic = individual['metadata']["Proxy min-max ELA values"]
                                    all_problem_data.append(list(proxy_dic.values()))

            # Shared, global PCA model
            if all_problem_data:
                shared_df = pd.DataFrame(all_problem_data, columns=self.features)
                shared_pca = PCA(n_components=2)

                # Find global PCA bounds
                all_reduced = shared_pca.fit_transform(shared_df)
                mb_data = [
                    list(self.original_minmaxEla_p1.values()),
                    list(self.original_minmaxEla_p2.values()),
                    list(self.original_minmaxEla_p3.values())
                ]
                mb_df = pd.DataFrame(mb_data, columns=self.features)
                all_mb_reduced = shared_pca.transform(mb_df)

                pc1_min = min(all_reduced[:, 0].min(), all_mb_reduced[:, 0].min())
                pc1_max = max(all_reduced[:, 0].max(), all_mb_reduced[:, 0].max())
                pc2_min = min(all_reduced[:, 1].min(), all_mb_reduced[:, 1].min())
                pc2_max = max(all_reduced[:, 1].max(), all_mb_reduced[:, 1].max())

                # Padding
                pc1_padding = (pc1_max - pc1_min) * 0.05
                pc2_padding = (pc2_max - pc2_min) * 0.05

                global_xlim = (pc1_min - pc1_padding, pc1_max + pc1_padding)
                global_ylim = (pc2_min - pc2_padding, pc2_max + pc2_padding)

            return shared_pca, global_xlim, global_ylim

        self.load_logs()

        self.pca, self.pca_x_lim, self.pca_y_lim = define_PCA_space()


    def run(self,
            progress_plots=True,
            pca_plots=True,
            diversity_plots=True,
            get_proxy_standings=True,
            compute_aocc=True,
            plot_aocc=True,
            compare_aocc=True,
            kendall_fitness_scatter=True,
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

            all_problem_data = []
            for p in self.log:
                for config in self.log[p]:
                    if 'total' not in config:
                        for inds in self.log[p][config]:
                            if 'total' in inds:
                                for individual in self.log[p][config][inds]:
                                    proxy_dic = individual['metadata']["Proxy min-max ELA values"]
                                    all_problem_data.append(list(proxy_dic.values()))

            # Shared, global PCA model
            if all_problem_data:
                shared_df = pd.DataFrame(all_problem_data, columns=self.features)
                shared_pca = PCA(n_components=2)

                # Find global PCA bounds
                all_reduced = shared_pca.fit_transform(shared_df)
                mb_data = [
                    list(self.original_minmaxEla_p1.values()),
                    list(self.original_minmaxEla_p2.values()),
                    list(self.original_minmaxEla_p3.values())
                ]
                mb_df = pd.DataFrame(mb_data, columns=self.features)
                all_mb_reduced = shared_pca.transform(mb_df)

                pc1_min = min(all_reduced[:, 0].min(), all_mb_reduced[:, 0].min())
                pc1_max = max(all_reduced[:, 0].max(), all_mb_reduced[:, 0].max())
                pc2_min = min(all_reduced[:, 1].min(), all_mb_reduced[:, 1].min())
                pc2_max = max(all_reduced[:, 1].max(), all_mb_reduced[:, 1].max())

                # Padding
                pc1_padding = (pc1_max - pc1_min) * 0.05
                pc2_padding = (pc2_max - pc2_min) * 0.05

                global_xlim = (pc1_min - pc1_padding, pc1_max + pc1_padding)
                global_ylim = (pc2_min - pc2_padding, pc2_max + pc2_padding)

                for p in self.log:
                    for config in self.log[p]:
                        if 'total' not in config:
                            for inds in self.log[p][config]:
                                if 'total' in inds:
                                    self.pca(
                                        self.log[p][config][inds],
                                        shared_pca,
                                        problem_type=p,
                                        save_folder='pca_plots',
                                        name_=f'{p}_{config}',
                                        xlim=global_xlim,
                                        ylim=global_ylim
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

        if plot_aocc:
            print(f'\n --- Plotting AOCC points ---')
            df = pd.read_csv('results/aocc_results.csv')
            self.plot_aocc_per_problem(df)

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

    @staticmethod
    def compute_ela(X, y):
        ela_distr = ela.calculate_ela_distribution(X, y)
        ela_meta = ela.calculate_ela_meta(X, y)
        ela_disp = ela.calculate_dispersion(X, y)
        ela_ic = ela.calculate_information_content(X, y)
        ela_nbc = ela.calculate_nbc(X, y)
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
            'ela_level.mmce_qda_25': ela_11,
            'ela_level.lda_qda_25': ela_12
        }

        return pd.Series(ela_values)

    def update_ela_stats(self):
        ela_stats = pd.read_csv(self.original_stats_path)

        all_ela_values = {}
        path_by_size = "../Folder_Points/500D/by_size"
        for size in os.listdir(path_by_size):
            all_ela_values[size] = {}
            new_ela_stats = ela_stats.copy()  # The copy stats that will be updated and output
            size_path = f'../Folder_Points/500D/by_size/{size}'
            if not size_path[-3:] == 'csv':
                print(f'\n\n ++++ #### SIZE {size} #### ++++ \n\n')

                os.listdir(f'{size_path}/ELA')
                for problem_path in os.listdir(f'{size_path}/ELA'):
                    if 'p1' in problem_path:
                        problem = 'p1'
                        dim = 5
                    elif 'p2' in problem_path:
                        problem = 'p2'
                        dim = 5
                    elif 'p3' in problem_path:
                        problem = 'p3'
                        dim = 20  # 20 because 15 is missing in ela_stats

                    print(f'---- PROBLEM {problem} ----')

                    full_path = f'{path_by_size}/{size}/ELA/{problem_path}'
                    raw_ela_values = pd.read_csv(full_path, index_col='feature')  # MB ELA values
                    all_ela_values[size][problem] = raw_ela_values

                    for feature in self.features:
                        # Get the row corresponding to the feature and dimensionality
                        condition = (new_ela_stats['dimension'] == dim) & (new_ela_stats['feature'] == feature)
                        feat_dim_row = new_ela_stats.loc[condition]
                        min_ = feat_dim_row['min'].iloc[0]
                        max_ = feat_dim_row['max'].iloc[0]
                        feat_value = raw_ela_values.loc[feature].iloc[0]

                        if feat_value < min_:
                            print(f'{feat_value: 3f} < {min_: 3f}. Updating!')
                            new_ela_stats.loc[condition, 'min'] = float(feat_value)
                            print(f'New row: {new_ela_stats.loc[condition].to_string()}\n')
                        elif feat_value > max_:
                            print(f'{feat_value: 3f} > {max_: 3f}. Updating!')
                            new_ela_stats.loc[condition, 'max'] = float(feat_value)
                            print(f'New row: {new_ela_stats.loc[condition].to_string()}\n')

                    new_ela_stats.to_csv(f'{size_path}/{size}_updated_ELA_stats.csv', index=False)

    def min_max_ela(self):
        path = '../Folder_Points/500D/by_size'
        for size in os.listdir(path):
            stats_csv = f'{path}/{size}/{size}_updated_ELA_stats.csv'
            stats_df = pd.read_csv(stats_csv)
            ela_path = f'{path}/{size}/ELA'
            for p_ela_csv in os.listdir(ela_path):
                if 'p1' in p_ela_csv:
                    problem = 'p1'
                    dim = 5
                elif 'p2' in p_ela_csv:
                    problem = 'p2'
                    dim = 5
                elif 'p3' in p_ela_csv:
                    problem = 'p3'
                    dim = 20  # 20 because 15 is missing in ela_stats

                full_ela_path = f'{ela_path}/{p_ela_csv}'
                ela_series = pd.read_csv(full_ela_path, index_col='feature')

                # Min-max normalization on ELA values:
                stats_filtered = stats_df[
                    (stats_df['dimension'] == dim) & (stats_df['dataset'] == 'BBOB_SM_all')]

                # Explicitly join using left_index=True because 'feature' was set as the index
                merged_df = pd.merge(ela_series, stats_filtered[['feature', 'min', 'max']],
                                     left_index=True, right_on='feature', how='left')

                denominator = merged_df['max'] - merged_df['min']
                denominator = denominator.replace(0, np.nan)
                merged_df['normalized_value'] = (merged_df['value'] - merged_df['min']) / denominator
                merged_df['normalized_value'] = merged_df['normalized_value'].fillna(0.0)
                ela_minmax = merged_df[['feature', 'normalized_value']].rename(
                    columns={'normalized_value': 'value'})

                ela_minmax = ela_minmax.set_index('feature')
                print(ela_minmax.to_string())
                save_name = f'../Folder_Points/500D/data_{problem}/ELA_min_max/minmax_{p_ela_csv}'
                ela_minmax.to_csv(save_name)

    def load_logs(self):
        print(self.log_dir)
        for problem_ in os.listdir(self.log_dir):
            print(problem_)
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

    def feature_stats_plot(self):
        updated_stats = pd.read_csv(self.updated_stats_path)
        original_stats = pd.read_csv(self.original_stats_path)

        updated_12 = updated_stats.loc[(updated_stats['dimension'] == 5) & (updated_stats['feature'].isin(self.features))]
        original_12 = original_stats.loc[(original_stats['dimension'] == 5) & (original_stats['feature'].isin(self.features))]
        updated_3 = updated_stats.loc[(updated_stats['dimension'] == 20) & (updated_stats['feature'].isin(self.features))]
        original_3 = original_stats.loc[(original_stats['dimension'] == 20) & (original_stats['feature'].isin(self.features))]

        for dim, p in [(5, '1, 2'), (20, '3')]:
            updated = updated_stats.loc[(updated_stats['dimension'] == dim) & (updated_stats['feature'].isin(self.features))]
            original = original_stats.loc[(original_stats['dimension'] == dim) & (original_stats['feature'].isin(self.features))]

            original_min, original_max = original['min'], original['max']
            updated_min, updated_max = updated['min'], updated['max']

    def pca(self, individuals, pre_fitted_pca, problem_type, save_folder, name_, xlim, ylim):
        pca_dic = {}
        proxy_data = pd.DataFrame(columns=self.features)
        mb_vector = pd.DataFrame(columns=self.features)

        generations = []
        if problem_type == 'p1':
            mb_vector.loc[0] = self.original_minmaxEla_p1.values()
        elif problem_type == 'p2':
            mb_vector.loc[0] = self.original_minmaxEla_p2.values()
        elif problem_type == 'p3':
            mb_vector.loc[0] = self.original_minmaxEla_p3.values()

        for i, individual in enumerate(individuals):
            proxy_dic = individual['metadata']["Proxy min-max ELA values"]
            proxy_data.loc[i] = proxy_dic.values()
            generations.append(individual['generation'])

        generations = pd.Series(generations)

        proxies_reduced = pre_fitted_pca.transform(proxy_data)
        mb_reduced = pre_fitted_pca.transform(mb_vector)
        expl_var = pre_fitted_pca.explained_variance_ratio_

        fig, ax = plt.subplots(figsize=(9, 6))

        # Scatterplot
        proxies_s = ax.scatter(
            proxies_reduced[:, 0],
            proxies_reduced[:, 1],
            c=generations,
            cmap="viridis",
            s=40,
            alpha=0.8,
            edgecolors="none"
        )

        # Original MB point
        mb_s = ax.scatter(
            mb_reduced[:, 0],
            mb_reduced[:, 1],
            marker='*',
            s=300,
            color="red",
            alpha=0.6,
            edgecolors="black",
            linewidths=0.75,
            label=f"MB{problem_type[1]}"
        )

        ax.set(
            title=f"PCA by Generations ({name_})",
            xlabel=f"1st Principal Component ({expl_var[0] * 100:.1f}%)",
            ylabel=f"2nd Principal Component ({expl_var[1] * 100:.1f}%)",
            xlim=xlim,  # Global bounds
            ylim=ylim
        )

        # Axes
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        ax.legend(loc="upper right", frameon=True)

        # Colorbar
        cbar = fig.colorbar(proxies_s, ax=ax)
        cbar.set_label("Evolutionary Generation", rotation=270, labelpad=15)

        plt.tight_layout()
        filename = f"{self.save_folder_name}/{save_folder}/PCA_results_{name_}.png"
        plt.savefig(filename, dpi=900)
        plt.close()

        return pca_dic

    def pca_proxy_standings(self, save_folder):
        """
        Generates 3 PCA plots (one per problem) comparing the MB target against
        the 9 selected proxy functions (pod1-3, med1-3, worst1-3).

        :param proxy_ela_dicts: Nested dictionary of the 9 proxies' ELA values per problem.
                                Format: {'p1': {'pod1': {ela_dict}, ...}, 'p2': {...}, 'p3': {...}}
        """
        # Define the discrete light-to-dark color scheme
        color_map = {
            'pod1': '#a1d99b', 'pod2': '#31a354', 'pod3': '#005a32',  # Greens
            'med1': '#9ecae1', 'med2': '#3182bd', 'med3': '#08519c',  # Blues
            'worst1': '#fc9272', 'worst2': '#de2d26', 'worst3': '#a50f15'  # Reds
        }

        expl_var = self.pca.explained_variance_ratio_

        for p in ['p1', 'p2', 'p3']:
            if p not in self.standings_ELA_values:
                continue

            fig, ax = plt.subplots(figsize=(9, 6), dpi=300)

            # 1. PLOT THE ORIGINAL MB TARGET
            mb_vector = pd.DataFrame(columns=self.features)
            if p == 'p1':
                mb_vector.loc[0] = self.original_minmaxEla_p1.values()
            elif p == 'p2':
                mb_vector.loc[0] = self.original_minmaxEla_p2.values()
            elif p == 'p3':
                mb_vector.loc[0] = self.original_minmaxEla_p3.values()

            mb_reduced = self.pca.transform(mb_vector)

            ax.scatter(
                mb_reduced[:, 0], mb_reduced[:, 1],
                marker='*', s=450, color="gold", alpha=0.9,
                edgecolors="black", linewidths=1.2,
                label=f"MB{p[1]} (Target)", zorder=5
            )

            # 2. PLOT THE 9 PROXIES
            proxies = self.standings_ELA_values[p]
            for standing, ela_dict in proxies.items():
                if standing not in color_map:
                    continue

                proxy_df = pd.DataFrame([ela_dict.values()], columns=self.features)
                proxy_reduced = self.pca.transform(proxy_df)

                # Scatter the proxy point
                ax.scatter(
                    proxy_reduced[:, 0], proxy_reduced[:, 1],
                    color=color_map[standing],
                    s=150, alpha=0.9,
                    edgecolors="black", linewidths=0.8,
                    label=standing, zorder=4
                )

                # Optional: Add a subtle text label slightly offset from the point
                # to make visual identification instant without checking the legend
                ax.annotate(
                    standing,
                    (proxy_reduced[0, 0], proxy_reduced[0, 1]),
                    xytext=(6, 6), textcoords="offset points",
                    fontsize=9, fontweight="bold", alpha=0.7
                )

            # 3. FORMAT AXES AND LEGEND
            ax.set(
                title=f"PCA Topology of Proxies vs. Real-World Target ({p.upper()})",
                xlabel=f"1st Principal Component ({expl_var[0] * 100:.1f}%)",
                ylabel=f"2nd Principal Component ({expl_var[1] * 100:.1f}%)",
                xlim=self.pca_x_lim,
                ylim=self.pca_y_lim
            )
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            ax.grid(True, linestyle="--", alpha=0.4)

            # Move legend outside the plot so it doesn't cover points
            ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", frameon=True, title="Standings")

            # 4. SAVE
            plt.tight_layout()
            filename = f"{self.save_folder_name}/{save_folder}/PCA_proxy_topology_{p}.png"
            os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)
            plt.savefig(filename, bbox_inches="tight")
            plt.close()

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
                worst_proxies.append(row)
            if len(worst_proxies) == 3:
                break

        # Fix: worst1 should be the 'best' and worst3 the absolute worst
        worst_proxies = worst_proxies[::-1]

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
                    max_evals = 450

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
        df_wide['SE'] = df_wide[seed_cols].std(axis=1)
        filename = f'{self.save_folder_name}/{save_path}'
        df_wide.to_csv(filename)

        return df_wide

    def compute_A12(self, path_convergence_data, save_path):
        """
        Computes A12 effect size RMSE and proxy fitness, saving 3 CSV files (one per problem).
        Includes Min-Max normalization within each problem.
        """
        analysis_path = path_convergence_data
        bsf_data = {}

        # 1. PARSE DATA (Unchanged)
        for seed in os.listdir(analysis_path):
            seed_path = os.path.join(analysis_path, seed)
            if not os.path.isdir(seed_path): continue
            for p in os.listdir(seed_path):
                p_path = os.path.join(seed_path, p)
                if not os.path.isdir(p_path): continue
                if p not in bsf_data: bsf_data[p] = {}
                max_evals = 150 if p in ['p1', 'p2'] else 450

                for standing in os.listdir(p_path):
                    standing_path = os.path.join(p_path, standing)
                    if not os.path.isdir(standing_path): continue
                    if standing not in bsf_data[p]: bsf_data[p][standing] = {}

                    for algo in os.listdir(standing_path):
                        algo_path = os.path.join(standing_path, algo)
                        if not os.path.isdir(algo_path): continue
                        if algo not in bsf_data[p][standing]: bsf_data[p][standing][algo] = {}

                        for f in os.listdir(algo_path):
                            if f[:3] == 'IOH': continue
                            data_dir = os.path.join(algo_path, f)
                            if not os.path.isdir(data_dir): continue

                            for dat in os.listdir(data_dir):
                                if not dat.endswith('.dat'): continue
                                dat_path = os.path.join(data_dir, dat)

                                df = pd.read_csv(dat_path, sep=" ")
                                df = df[:max_evals]
                                raw_y = df["raw_y"].to_numpy()

                                best_so_far = []
                                current_bsf = float('inf')
                                for y_ in raw_y:
                                    if y_ < current_bsf:
                                        current_bsf = y_
                                    best_so_far.append(current_bsf)
                                while len(best_so_far) < max_evals:
                                    best_so_far.append(current_bsf)
                                bsf_data[p][standing][algo][seed] = best_so_far

        # 2. COMPUTE A12 & EXTRACT FITNESS
        proxy_standings = ['pod1', 'pod2', 'pod3', 'med1', 'med2', 'med3', 'worst1', 'worst2', 'worst3']

        for p in ['p1', 'p2', 'p3']:
            if p not in bsf_data: continue
            standings = bsf_data[p].keys()
            mb_standing = next((s for s in standings if 'MB' in s), None)
            if not mb_standing: continue

            algos = sorted(list(bsf_data[p][mb_standing].keys()))
            pairs = list(itertools.combinations(algos, 2))
            cuts = [25, 50, 75, 100, 125, 150] if p in ['p1', 'p2'] else [75, 150, 225, 300, 375, 450]

            def get_90_A12(standing_name):
                a12_values = []
                for (algo1, algo2) in pairs:
                    for cut in cuts:
                        cut_idx = cut - 1
                        algo1_vals, algo2_vals = [], []
                        seeds1 = set(bsf_data[p][standing_name].get(algo1, {}).keys())
                        seeds2 = set(bsf_data[p][standing_name].get(algo2, {}).keys())
                        common_seeds = seeds1.intersection(seeds2)

                        for s in common_seeds:
                            algo1_vals.append(bsf_data[p][standing_name][algo1][s][cut_idx])
                            algo2_vals.append(bsf_data[p][standing_name][algo2][s][cut_idx])

                        algo1_vals, algo2_vals = np.array(algo1_vals), np.array(algo2_vals)
                        wins = np.sum(algo1_vals < algo2_vals)
                        ties = np.sum(algo1_vals == algo2_vals)
                        n_seeds = len(common_seeds)

                        a12 = (wins + 0.5 * ties) / n_seeds if n_seeds > 0 else 0.5
                        a12_values.append(a12)
                return np.array(a12_values)

            mb_a12 = get_90_A12(mb_standing)
            standings_p = self.standings_total[p]

            p_results = []
            for proxy in proxy_standings:
                if proxy in bsf_data[p]:
                    proxy_a12 = get_90_A12(proxy)
                    rmse = np.sqrt(np.mean((mb_a12 - proxy_a12) ** 2))
                    try:
                        fitness = standings_p.loc[standings_p['standing'] == proxy]['fitness'].values[0]
                    except IndexError:
                        fitness = np.nan

                    p_results.append({
                        'standing': proxy,
                        'A12_RMSE': rmse,
                        'fitness': fitness
                    })

            # 3. NORMALIZE & SAVE PROBLEM-SPECIFIC CSV
            df_p = pd.DataFrame(p_results)

            if len(df_p) > 1:
                rmse_min, rmse_max = df_p['A12_RMSE'].min(), df_p['A12_RMSE'].max()
                fit_min, fit_max = df_p['fitness'].min(), df_p['fitness'].max()

                # Prevent division by zero if values are identical
                df_p['norm_A12_RMSE'] = (df_p['A12_RMSE'] - rmse_min) / (
                            rmse_max - rmse_min) if rmse_max > rmse_min else 0
                df_p['norm_fitness'] = (df_p['fitness'] - fit_min) / (fit_max - fit_min) if fit_max > fit_min else 0
            else:
                df_p['norm_A12_RMSE'] = 0.0
                df_p['norm_fitness'] = 0.0

            df_p.set_index('standing', inplace=True)

            p_num = p.replace('p', '')
            filename = f"{self.save_folder_name}/{save_path}_p{p_num}.csv"
            os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)
            df_p.to_csv(filename)
            print(f"Saved {filename}")

    def compute_AOCC_RMSE(self, path_aocc_results, save_path, use_t_stat=False):
        """
        Computes RMSE based on pairwise differences in Mean AOCC.
        Format: index=standing (proxy), columns=[AOCC_RMSE, norm_AOCC_RMSE, fitness, norm_fitness].
        """
        aocc_df = pd.read_csv(path_aocc_results)
        algos = sorted(['baxus', 'botorch', 'cmaes', 'de', 'one_plus_one', 'turbo1'])
        pairs = list(itertools.combinations(algos, 2))  # 15 unique pairs

        proxy_standings = ['pod1', 'pod2', 'pod3', 'med1', 'med2', 'med3', 'worst1', 'worst2', 'worst3']

        for p in [1, 2, 3]:
            prob_name = f'p{p}'
            mb_standing = f'MB{p}'

            # Isolate dataframe for current problem to speed up lookups
            df_p = aocc_df[aocc_df['problem'] == prob_name]

            # For computing the t-statistic:
            def get_pairwise_t_stats(standing_name):
                """Returns a length-15 array of t-statistics (SE-weighted differences)."""
                df_s = df_p[df_p['standing'] == standing_name]
                if df_s.empty:
                    return None

                algo_means = dict(zip(df_s['algo'], df_s['mean']))
                algo_ses = dict(zip(df_s['algo'], df_s['SE']))

                t_stats = []
                for (algo1, algo2) in pairs:
                    mean_diff = algo_means[algo1] - algo_means[algo2]

                    # Calculate combined standard error (assuming independent samples)
                    combined_se = np.sqrt(algo_ses[algo1] ** 2 + algo_ses[algo2] ** 2)

                    # Prevent division by zero if an algorithm was entirely deterministic
                    if combined_se == 0:
                        combined_se = 1e-9

                    t_stat = mean_diff / combined_se
                    t_stats.append(t_stat)
                return np.array(t_stats)

            # For computing raw AOCC differences (no SE):
            def get_pairwise_diffs(standing_name):
                """Returns a length-15 array of Mean AOCC differences for a given standing."""
                df_s = df_p[df_p['standing'] == standing_name]
                if df_s.empty:
                    return None

                # Dictionary lookup is much faster/cleaner than chaining pandas filters
                algo_means = dict(zip(df_s['algo'], df_s['mean']))

                diffs = []
                for (algo1, algo2) in pairs:
                    # Calculate the margin of victory/defeat between the two algorithms
                    diff = algo_means[algo1] - algo_means[algo2]
                    diffs.append(diff)
                return np.array(diffs)

            if use_t_stat:
                func = get_pairwise_t_stats
            else:
                func = get_pairwise_diffs

            # 1. Get the Real-World (MB) pairwise differences
            mb_diffs = func(mb_standing)
            if mb_diffs is None:
                continue

            standings_p = self.standings_total[prob_name]
            p_results = []

            # 2. Compare against Proxies
            for proxy in proxy_standings:
                proxy_diffs = func(proxy)
                if proxy_diffs is not None:
                    # Compute RMSE between the 15 MB margins and the 15 Proxy margins
                    rmse = np.sqrt(np.mean((mb_diffs - proxy_diffs) ** 2))

                    try:
                        fitness = standings_p.loc[standings_p['standing'] == proxy]['fitness'].values[0]
                    except IndexError:
                        fitness = np.nan

                    p_results.append({
                        'standing': proxy,
                        'AOCC_RMSE': rmse,
                        'fitness': fitness
                    })

            # 3. Normalize & Save Problem-Specific CSV
            res_df = pd.DataFrame(p_results)

            if len(res_df) > 1:
                rmse_min, rmse_max = res_df['AOCC_RMSE'].min(), res_df['AOCC_RMSE'].max()
                fit_min, fit_max = res_df['fitness'].min(), res_df['fitness'].max()

                res_df['norm_AOCC_RMSE'] = (res_df['AOCC_RMSE'] - rmse_min) / (
                            rmse_max - rmse_min) if rmse_max > rmse_min else 0
                res_df['norm_fitness'] = (res_df['fitness'] - fit_min) / (fit_max - fit_min) if fit_max > fit_min else 0
            else:
                res_df['norm_AOCC_RMSE'] = 0.0
                res_df['norm_fitness'] = 0.0

            res_df.set_index('standing', inplace=True)

            filename = f"{self.save_folder_name}/{save_path}_p{p}.csv"
            os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)
            res_df.to_csv(filename)
            print(f"Saved {filename}")


    def plot_aocc_per_problem(self, df_wide):
        """Generates grouped error-bar plots of AOCC values (mean ± SE) per problem.

        Parameters:
        df_wide : pd.DataFrame
            Output DataFrame from compute_AOCC containing 'problem', 'standing',
            'algo', 'mean', and 'SE'.
        save_folder : str
            Directory where the output plot images will be saved.
        """
        save_folder = f"{self.save_folder_name}/aocc_point_plots"
        os.makedirs(save_folder, exist_ok=True)
        sns.set_theme(style="whitegrid", palette="Set2")

        unique_problems = df_wide["problem"].unique()

        for problem in unique_problems:
            # print(problem)
            sub_df = df_wide[df_wide["problem"] == problem].copy()

            # Place Real-World target (e.g. MB1/MB2) first on the x-axis if present
            standings = list(sub_df["standing"].unique())
            mb_standings = [s for s in standings if "MB" in s]
            other_standings = [s for s in standings if "MB" not in s]
            # standing_order = mb_standings + sorted(other_standings)
            standing_order = [f'MB{problem[1]}', 'pod1', 'pod2', 'pod3', 'med1', 'med2', 'med3', 'worst1', 'worst2', 'worst3']
            # print(standing_order)

            unique_algos = sorted(sub_df["algo"].unique())
            num_algos = len(unique_algos)

            # Offset width to jitter points horizontally across standings
            width = 0.12
            standing_x_map = {s: i for i, s in enumerate(standing_order)}

            fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

            for idx, algo in enumerate(unique_algos):
                algo_df = sub_df[sub_df["algo"] == algo].copy()

                # Map x-coordinates with categorical jitter offset
                x_coords = [
                    standing_x_map[s] + (idx - num_algos / 2) * width + width / 2
                    for s in algo_df["standing"]
                ]

                ax.errorbar(
                    x_coords,
                    algo_df["mean"],
                    yerr=algo_df["SE"],
                    fmt="o-",
                    label=algo,
                    capsize=4,
                    capthick=1.5,
                    elinewidth=1.5,
                    markersize=6,
                    alpha=0.85,
                )

            ax.set_xticks(range(len(standing_order)))
            ax.set_xticklabels(standing_order, fontsize=11, fontweight="bold")
            ax.set_xlabel(
                "Standing / Problem Target", fontsize=12, fontweight="bold"
            )
            ax.set_ylabel("Mean AOCC (± SE)", fontsize=12, fontweight="bold")
            ax.set_title(
                f"Algorithm Performance Comparison Across Standings — {problem.upper()}",
                fontsize=13,
                fontweight="bold",
                pad=15,
            )

            ax.set_ylim(0, 1.05)
            ax.grid(True, linestyle="--", alpha=0.5)
            ax.legend(
                title="Algorithm",
                bbox_to_anchor=(1.02, 1),
                loc="upper left",
                frameon=True,
            )

            plt.tight_layout()
            save_path = os.path.join(save_folder, f"aocc_comparison_{problem}.png")
            plt.savefig(save_path, bbox_inches="tight")
            plt.close()
            print(f"Saved plot: {save_path}")

    def compare_AOCCs(self, path_aocc_results, save_path):
        full_path = f'{self.save_folder_name}/{path_aocc_results}'
        aocc_results = pd.read_csv(full_path)

        for p in [1, 2, 3]:
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
            self.min_tau = min(df_taus['tau'].min(), self.min_tau)
            self.max_tau = max(df_taus['tau'].max(), self.max_tau)
            self.min_fit = min(df_taus['fitness'].min(), self.min_fit)
            self.max_fit = max(df_taus['fitness'].max(), self.max_fit)
            filename = f'{self.save_folder_name}/{save_path}_p{p}.csv'
            df_taus.to_csv(filename)

    def scatter_fitness_metric(self, path_results, save_path, metric='tau', use_normalized=True):
        """
        Scatter plot comparing fitness against a performance metric.
        :param metric: Base metric name ('tau', 'A12_RMSE' or 'AOCC_t_stat').
        :param use_normalized: If True, uses the [0, 1] normalized versions of the columns.
        """
        for p in [1, 2, 3]:
            filename = f'{self.save_folder_name}/{path_results}'
            df_metric = pd.read_csv(f'{filename}_p{p}.csv', index_col=0)

            # Dynamically select columns based on normalization flag
            if use_normalized and metric != 'tau':
                x_col = f'norm_{metric}'
                y_col = 'norm_fitness'
            else:
                x_col = metric
                y_col = 'fitness'

            metric_vals = df_metric[x_col].to_numpy()
            fitness = df_metric[y_col].to_numpy()
            standings = df_metric.index.to_numpy()

            ranks = pd.Series([i for i, s in enumerate(standings)])
            norm_ranks = (ranks - ranks.min()) / (ranks.max() - ranks.min())

            fig, ax = plt.subplots(figsize=(9, 6))
            cmap = plt.get_cmap("viridis")

            # Jitter relative to the local data bounds
            x_range = metric_vals.max() - metric_vals.min()
            y_range = fitness.max() - fitness.min()
            jitter_amplitude_x = (x_range * 0.015) if x_range > 0 else 0.015
            jitter_amplitude_y = (y_range * 0.015) if y_range > 0 else 0.015

            rng = np.random.default_rng(seed=42)

            for i in range(len(metric_vals)):
                jx = rng.uniform(-jitter_amplitude_x, jitter_amplitude_x)
                jy = rng.uniform(-jitter_amplitude_y, jitter_amplitude_y)
                plot_x = metric_vals[i] + jx
                plot_y = fitness[i] + jy

                ax.scatter(
                    plot_x, plot_y, color=cmap(norm_ranks[i]),
                    s=350, alpha=0.8, edgecolors="black", linewidths=0.5
                )

                ax.text(
                    plot_x, plot_y, str(ranks[i] + 1), color="white",
                    fontsize=9, fontweight="bold", va="center", ha="center"
                )

            # Trend line
            m, b = np.polyfit(metric_vals, fitness, 1)
            x_line = np.linspace(metric_vals.min(), metric_vals.max(), 100)
            y_line = m * x_line + b
            ax.plot(
                x_line, y_line, color="red", linestyle="--",
                linewidth=2, alpha=0.7, label=f"Trend (slope: {m:.2f})"
            )

            # FIX FOR THE BUG: Extract min/max dynamically from the loaded array
            x_min, x_max = metric_vals.min(), metric_vals.max()
            y_min, y_max = fitness.min(), fitness.max()

            x_padding = (x_max - x_min) * 0.05 if x_max > x_min else 0.1
            y_padding = (y_max - y_min) * 0.05 if y_max > y_min else 0.1

            # Use global tau limits if requested, otherwise strictly fit to data
            if metric == 'tau' and not use_normalized:
                x_min, x_max = self.min_tau, self.max_tau
                title_text = "Kendall's tau"
            else:
                title_text = f"Normalized {metric}" if use_normalized else metric

            ax.set(
                title=f"{title_text} vs. Fitness (p{p})",
                xlabel=title_text,
                ylabel="Normalized Fitness (ELA Distance)" if use_normalized else "Fitness",
                xlim=(x_min - x_padding, x_max + x_padding),
                ylim=(y_min - y_padding, y_max + y_padding)
            )

            ax.legend()
            plt.tight_layout()
            plt.savefig(f"{self.save_folder_name}/{save_path}_{metric}_p{p}.png", dpi=900)
            plt.close()


if __name__ == "__main__":
    log_dir = "../data_and_results/LLaMEA_results"
    save_folder_name = 'results'
    algo_results = '../data_and_results/algo_results'
    analyzer = LLaMEAAnalyzer(
        log_dir=log_dir,
        save_folder_name=save_folder_name,
        aocc_path=algo_results
    )
    aocc_path = 'results/aocc_results.csv'

    # analyzer.load_logs()
    log = analyzer.log
    df = analyzer.experiments_data

    # analyzer.run(
    #     progress_plots=False,
    #     pca_plots=False,
    #     diversity_plots=False,
    #     get_proxy_standings=False,
    #     compute_aocc=False,
    #     plot_aocc=True,
    #     compare_aocc=False,
    #     kendall_fitness_scatter=False
    # )

    # analyzer.compute_A12(algo_results, 'A12_values')
    # metric_ = 'A12_RMSE'
    # analyzer.scatter_fitness_metric('A12_values', 'scatterplot_fitness', metric=metric_, use_normalized=True)

    # analyzer.compute_AOCC_RMSE(aocc_path, 'AOCC_pairwise_diffs')
    # metric_ = 'AOCC_pairwise_diff'
    # analyzer.scatter_fitness_metric('AOCC_pairwise_diffs', 'scatterplot_fitness', metric=metric_, use_normalized=True)

    analyzer.pca_proxy_standings(save_folder_name)
