import pflacco.classical_ela_features as ela
import os
import pandas as pd
import numpy as np

ELA_STATS = pd.read_csv("ela_feature_stats.csv")


def compute_ela(X, y, save_folder, normalize=True):
    if normalize:  # Min-max normalize the X and y if you haven't already
        y[y == 0] = 0.1 ** 100  # since y=0 breaks log
        if y.max() == y.min():
            for i in range(len(y)):
                y[i] = 0
        else:
            X = (X - X.min()) / (X.max() - X.min())
            y = (y - y.min()) / (y.max() - y.min())

    # Get the dictionaries
    ela_distr = ela.calculate_ela_distribution(X, y)
    ela_level = ela.calculate_ela_level(X, y)
    ela_meta = ela.calculate_ela_meta(X, y)
    ela_disp = ela.calculate_dispersion(X, y)
    ela_ic = ela.calculate_information_content(X, y)
    ela_nbc = ela.calculate_nbc(X, y)

    # Get the specific feature values
    ela_1 = ela_disp['disp.ratio_mean_02']  # 1) disp.ratio_mean_02
    ela_2 = ela_distr['ela_distr.skewness']  # 2) ela_distr.skewness
    ela_3 = ela_meta['ela_meta.lin_simple.adj_r2']  # 3) ela_meta.lin_simple.adj_r2
    ela_4 = ela_meta['ela_meta.lin_simple.intercept']  # 4) ela_meta.lin_simple.intercept
    ela_5 = ela_meta['ela_meta.lin_simple.coef.max']  # 5) ela_meta.lin_simple.coef.max
    ela_6 = ela_meta['ela_meta.quad_simple.adj_r2']  # 6) ela_meta.quad_simple.adj_r2
    ela_7 = ela_ic['ic.eps_ratio']  # 7) ic.eps_ratio
    ela_8 = ela_ic['ic.eps_s']  # 8) ic.eps_s
    ela_9 = ela_nbc['nbc.nb_fitness.cor']  # 9) nbc.nb_fitness.cor
    ela_10 = ela_level['ela_level.mmce_qda_25']
    ela_11 = ela_level['ela_level.lda_qda_25']

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
        'ela_level.mmce_qda_25': ela_10,
        'ela_level.lda_qda_25': ela_11
    }

    ela_df = pd.Series(ela_values)
    ela_df.index.name = 'feature'
    ela_df.name = 'value'

    if not os.path.exists(save_folder):
        os.mkdir(save_folder)

    path = f"{save_folder}/ela.csv"
    ela_df.to_csv(path)
    return ela_df


def minmax_ela(ela_df_, save_folder):

    stats_filtered = ELA_STATS[
        (ELA_STATS['dimension'] == 5) & (ELA_STATS['dataset'] == 'BBOB_SM_all')]

    # Explicitly join using left_index=True because 'feature' was set as the index
    merged_df = pd.merge(ela_df_, stats_filtered[['feature', 'min', 'max']],
                         left_index=True, right_on='feature', how='left')

    denominator = merged_df['max'] - merged_df['min']
    denominator = denominator.replace(0, np.nan)
    merged_df['normalized_value'] = (merged_df['value'] - merged_df['min']) / denominator
    merged_df['normalized_value'] = merged_df['normalized_value'].fillna(0.0)
    ela_minmax = merged_df[['feature', 'normalized_value']].rename(columns={'normalized_value': 'value'})

    # Re-index ela_proxy_minmax so it matches the structure expected by downstream absolute difference checks
    ela_minmax.set_index('feature', inplace=True)
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)

    path = f"{save_folder}/ela_minmax.csv"
    ela_minmax.to_csv(path)


if __name__ == '__main__':
    df_path = "../Folder_Points/500D/data_p1/points/500d5_p1_seed1312.csv"  # EDIT your path
    df = pd.read_csv(df_path, index_col=0)
    points = df.iloc[:, 0:5]  # EDIT to find X
    objective_values = df.iloc[:, -1]  # EDIT to find y
    print(points)
    print(objective_values)

    ela_df = compute_ela(points, objective_values, "test")
    minmax_ela(ela_df, "test")
