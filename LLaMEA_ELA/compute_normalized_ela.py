import pandas as pd
import numpy as np

original_ela_df = pd.read_csv("../Folder_Points/500D/data_p3/ELA/500d15_p3_seed1312_ela.csv")

ela_stats = pd.read_csv("../ela_feature_stats.csv")
stats_filtered = ela_stats[(ela_stats['dimension'] == 5) & (ela_stats['dataset'] == 'BBOB_SM_all')]
merged_df = pd.merge(original_ela_df, stats_filtered[['feature', 'min', 'max']], on='feature', how='left')
print(merged_df.to_string())

# If value > max or value < min, make them the new max/min
merged_df['min'] = np.minimum(merged_df['min'], merged_df['value'])
merged_df['max'] = np.maximum(merged_df['max'], merged_df['value'])

denominator = merged_df['max'] - merged_df['min']
denominator = denominator.replace(0, np.nan)
merged_df['normalized_value'] = (merged_df['value'] - merged_df['min']) / denominator
merged_df['normalized_value'] = merged_df['normalized_value'].fillna(0.0)

final_ela_df = merged_df[['feature', 'normalized_value']].rename(columns={'normalized_value': 'value'})
final_ela_df.set_index('feature', inplace=True)

print(final_ela_df.to_string())
final_ela_df.to_csv("normalized_ela_500d_p3.csv")