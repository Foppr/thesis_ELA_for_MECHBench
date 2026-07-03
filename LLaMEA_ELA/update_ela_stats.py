"""
For every size (30d, 60d, 125d, 250d, 250d), update the ELA statistics based on the new, raw MECHBench ELA values.
Outputs five new ELA_stats CSVs, one for every size, based on the new p1-p3 ELA values.
"""

import pandas as pd
import os
import pflacco.classical_ela_features as ela
import re
import numpy as np


class LLaMEA_Preprocessor:
    def __init__(self, points_path='Folder_Points/500D'):
        self.points_path = points_path

    def run(self):
        """
        Compute min-max normalized MECHBench points,
        Compute ELA features from normalized points
        """
        path = '../Folder_Points/500D'
        for data_p in os.listdir(path):
            if data_p == 'by_size':  # skip the 'by_size' folder
                continue

            points_path = f'{path}/{data_p}/points'
            ELA_path = f'{path}/{data_p}/ELA'
            if not os.path.exists(points_path):
                os.mkdir(points_path)
            if not os.path.exists(ELA_path):
                os.mkdir(ELA_path)

            for csv in os.listdir(points_path):
                points = pd.read_csv(f'{points_path}/{csv}', index_col='id')

                if 'p1' in csv:
                    y_col = 'penalized_sea'
                    other_cols = ['intrusion', 'specific_energy_absorbed']
                elif 'p2' in csv:
                    y_col = 'penalized_mass'
                    other_cols = ['intrusion', 'mass']
                elif 'p3' in csv:
                    y_col = 'load_uniformity'
                    other_cols = []

                points[y_col] = points[y_col].replace(0, 1e-100)  # since y=0 breaks log (ela computation uses log)
                points_min = points.min()
                points_max = points.max()
                denominator = points_max - points_min
                denominator = denominator.replace(0, 1)
                points_scaled = (points - points_min) / denominator

                data_p_path = f'{path}/{data_p}'
                points_min_max_dir = f'{data_p_path}/points_min_max'
                if not os.path.exists(points_min_max_dir):
                    os.mkdir(points_min_max_dir)

                points_scaled.to_csv(f'{points_min_max_dir}/min_max_{csv}')

                # COMPUTE ELA VALUES ON NORMALIZED POINTS
                X_y = points_scaled.drop(other_cols, axis=1)

                X = X_y.drop(y_col, axis=1)
                y = X_y[y_col]

                ela_ser = self.compute_ela(X, y)
                ela_ser.to_csv(f'{ELA_path}/ela_{csv}', index_label='feature', header=['value'])

                # SAVE TO by_size DIRECTORY FOR STATS UPDATE
                size = re.search(r'(\d+d)', csv).group(1)
                by_size_path = f'{path}/by_size/{size}'
                ela_ser.to_csv(f'{by_size_path}/ELA/ela_{csv}', index_label='feature', header=['value'])

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

    @staticmethod
    def update_stats():
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
            'ela_level.mmce_qda_25',
            'ela_level.lda_qda_25'
        ]

        ela_stats = pd.read_csv("ela_feature_stats.csv")

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

                    for feature in features:
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


if __name__ == '__main__':
    preprocessor = LLaMEA_Preprocessor()
    # preprocessor.run()
    # preprocessor.update_stats()
    preprocessor.min_max_ela()