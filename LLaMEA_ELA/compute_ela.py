import pflacco.classical_ela_features as ela
import os
import pandas as pd

points_path = "../Folder_Points/500D"
abs_path = os.path.abspath(points_path)

problem_type = 'data_p3'
dataset = '500d15_p3_seed1312_upto3750.csv'

points_df = pd.read_csv(f"{abs_path}/{problem_type}/points/{dataset}")
X = points_df.iloc[:, 1:16]
y = points_df.iloc[:, -1]

# Normalize
y[y == 0] = 0.1 ** 100  # since y=0 breaks log
if y.max() == y.min():
    for i in range(len(y)):
        y[i] = 0
else:
    X = (X - X.min()) / (X.max() - X.min())
    y = (y - y.min()) / (y.max() - y.min())

ela_distr = ela.calculate_ela_distribution(X, y)
ela_level = ela.calculate_ela_level(X, y)
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
ela_11 = ela_level['ela_level.mmce_qda_25']
ela_12 = ela_level['ela_level.lda_qda_25']

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

ela_df = pd.Series(ela_values)
ela_df.index.name = 'feature'
ela_df.name = 'value'

dataset = dataset[:-4]
ela_df.to_csv(f"{abs_path}/{problem_type}/ELA/{dataset}_ela.csv")
