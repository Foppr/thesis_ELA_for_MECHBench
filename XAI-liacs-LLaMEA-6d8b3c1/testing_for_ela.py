import pandas as pd

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

proxy_values = {1: [0.7969192902120477, -0.6558817167517744, 0.7792156042469198, 0.37996290206851757,
                     0.6678516941956094, 0.946697736541971, -0.5464555464555463, 0.09782509782509777,
                     -0.292160063153279, 0.26887061673940293, 0.0512, 1.2652393650773377],
                2: [1.3444197793385961, -0.09077899620305786, 0.03035075149743842, 0.6562963963022602, 0.05759788798755019, 0.6629501495596392, -0.3862953862953862, 0.16334516334516327, -0.45951245143705327, 0.20372791584903938, 0.2325818181818182, 1.0769204614829575]
                }

original_values = {1: [0.8612642659920741, 1.515364330067641, 0.19225468762932482, 0.4526333869944706, 0.12417909208757347, 0.24273707958599725, -0.8431158431158429, 0.31622531622531613, -0.27220799194696776, 0.2100563696526213, 0.07643636363636361, 3.5773686273696472],
                   2: [0.8612642659920741, 1.515364330067641, 0.19225468762932482, 0.4526333869944706, 0.12417909208757347, 0.24273707958599725, -0.8431158431158429, 0.31622531622531613, -0.27220799194696776, 0.2100563696526213, 0.07643636363636361, 3.5773686273696472]
                   }

proxy_dict = {}
original_dict = {}
for i, name in enumerate(features):
    proxy_dict[name] = round(proxy_values[1][i], 3)
    original_dict[name] = round(original_values[1][i], 3)

print(original_dict)
print(proxy_dict)

original_dict = {
    'disp.ratio_mean_02': 0.861,
    'ela_distr.skewness': 1.515,
    'ela_meta.lin_simple.adj_r2': 0.192,
    'ela_meta.lin_simple.intercept': 0.453,
    'ela_meta.lin_simple.coef.max': 0.124,
    'ela_meta.quad_simple.adj_r2': 0.243,
    'ic.eps_ratio': -0.843,
    'ic.eps_s': 0.316,
    'nbc.nb_fitness.cor': -0.272,
    'pca.expl_var_PC1.cov_init': 0.21,
    'ela_level.mmce_qda_25': 0.076,
    'ela_level.lda_qda_25': 3.577
}
proxy_dict = {
    'disp.ratio_mean_02': 0.797,
    'ela_distr.skewness': -0.656,
    'ela_meta.lin_simple.adj_r2': 0.779,
    'ela_meta.lin_simple.intercept': 0.38,
    'ela_meta.lin_simple.coef.max': 0.668,
    'ela_meta.quad_simple.adj_r2': 0.947,
    'ic.eps_ratio': -0.546,
    'ic.eps_s': 0.098,
    'nbc.nb_fitness.cor': -0.292,
    'pca.expl_var_PC1.cov_init': 0.269,
    'ela_level.mmce_qda_25': 0.051,
    'ela_level.lda_qda_25': 1.265
}

# Use pairwise distance as per-feature feedback
feedback = f"The optimization landscape '{proxy_name}' had the following distances to the original ELA values: "
for i in range(len(proxy_ela_means)):
    pairwise_distance = proxy_ela_means[i] - mechbench_ela_means[i]
    solution.add_metadata(f"Distance to {proxy_ela_means.index[i]}", round(pairwise_distance, 3))
    feedback += f"{proxy_ela_means.index[i]}: {pairwise_distance: .3f} (Original value: {mechbench_ela_means[i]}, proxy value: {proxy_ela_means[i]}) \n"

mb_mean = self.mechbench_ela.mean()
mb_std = self.mechbench_ela.std()

# Handle cases where a feature has zero variance in MECHBench to prevent dividing by zero
mb_std = mb_std.replace(0, 1.0)

# 2. Standardize both groups independently using the target's baseline metrics
z_mean_mechbench = (self.mechbench_ela.mean() - mb_mean) / mb_std  # This will naturally be a vector of 0s
z_mean_proxy = (proxy_ela_means - mb_mean) / mb_std

distance_series = (z_mean_mechbench - z_mean_proxy).abs()
print(f"DISTANCE SERIES: \n{distance_series}")
distance_series.name = "feature_distance"

# solution.add_metadata("MECHBench_mean_z", z_mean_mechbench.to_numpy())
# solution.add_metadata("proxy_mean_z", z_mean_proxy.to_numpy())
# solution.add_metadata("proxy_mean_z", distance_series.to_numpy())

final_score = distance_series.mean()
print(f"MEAN DISTANCE: \n{final_score}")