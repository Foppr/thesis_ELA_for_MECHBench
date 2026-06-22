# covnergence data tools

import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

sys.path.append('..')

from models import RSM, RandomForestModel, XGBModel, GPModel, BayesianNetworkModel
from scipy.stats import kendalltau 

FANCY_NAMES_MODELS = {
    'rsm': 'Response Surface Methodology',
    'rf': 'Random Forest',
    'xgb': 'XGBoost',
    'gp': 'Gaussian Process',
    'bn': 'Bayesian Network'
}

FANCY_NAMES_OPTIMIZERS = {
    'cmaes': 'CMA-ES',
    'turbo1': 'TuRBO-1',
    'botorch': 'BoTorch',
    'baxus': 'BAxUS',
    'de': 'DE',
    'one_plus_one': '1+1 ES'
}

def all_models_r2():
    SEED = 1312
    sizes = [30, 60, 125, 250, 500]
    problems = [1,2,3]

    for problem in problems:

        if problem==1:
            targets = ['intrusion', 'specific_energy_absorbed']
        elif problem==2:
            targets = ['intrusion', 'mass']
        elif problem==3:
            targets = ['load_uniformity']

        df = pd.DataFrame()
        df["size"] = ["30D", "60D", "125D", "250D", "500D"]
        for size in sizes:
            models = {
                "rsm" : {f'rsm_{target}' : RSM.load(f'RSM_{target}_p{problem}_{size}D.pkl', target=target, problem=problem, dset_size=size, seed=SEED) for target in targets},
                "rf" : { f'rf_{target}': RandomForestModel.load(f'RF_{target}_p{problem}_{size}D.pkl', target=target, problem=problem, dset_size=size, seed=SEED) for target in targets },
                "xgb" : {f'xgb_{target}' : XGBModel.load(f'XGB_{target}_p{problem}_{size}D.ubj', target=target, problem=problem, dset_size=size, seed=SEED) for target in targets},
                "gp" : {f'gp_{target}' : GPModel.load(f'GP_{target}_p{problem}_{size}D.pt')for target in targets},#, target=target, problem=problem, dset_size=size, seed=SEED) for target in targets},
                "bn" : {f'bayesian' : BayesianNetworkModel.load(f"BN_p{problem}_{size}D.pkl", problem=problem, dset_size=size, seed=SEED)}
            }


            model_scores = {}
            for model_class, model_dict in models.items():
                for model_name, _ in model_dict.items():
                    model_scores[model_name] = None     

            r2_values = {}
            for model_class, model_dict in models.items():
                for model_name, model in model_dict.items():
                    if model_class == 'bn':
                        preds = model.pred()
                        metrics = model.metrics(preds)
                        for target in model.targets:
                            # r2 = metrics[target]['r-squared']
                            #TODO: save value
                            r2_values[f'bayesian_{target}'] = metrics[target]['r-squared']
                    else:
                        preds = model.pred()
                        metrics = model.metrics(preds)
                        # r2 = metrics['r-squared']
                        r2_values[model_name] = metrics['r-squared']
                
            for model_name, r2_value in r2_values.items():
                df.loc[df['size'] == f"{size}D", model_name] = r2_value
                

        # for model_name, r2_value in r2_values.items():
        #     df.loc[df['size']==f"{size}D", 'model_name'] = r2_value

    # print(df)
        df.to_csv(f'r2_scores/r2_problem{problem}.csv', index=False)
        return df
    

def dat_to_df(dat):
    return pd.read_csv(dat, sep='\s+')

def read_convergence_data(filename):
    data = {
        'evaluations': [],
        'best': []
    }
    df = dat_to_df(filename)
        # for line_nr, line in enumerate(file):
        #     if line_nr == 0:
        #         continue
        #     line = line.strip()
        #     cols = line.split()
        
        #     data['evaluations'].append(float(cols[0]))
        #     data["best"].append(float(cols[2])) #TODO: check that this is current minimum
    
    df['best'] = df['raw_y'].cummin() 
    #TODO: add runtime from runtime files


    # data['evaluations'] = df['evaluations'].to_list()
    # data['best'] = df['best'].to_list()
    
    # return data

    return df

def plt_convergence_curve(data, model_class, problem, size):

    fig, ax = plt.subplots(figsize=(6, 4.5))

    for optimizer, convergence_data in data.items():
        ax.step(
            convergence_data['evaluations'], convergence_data['best'], where='post',
            label=FANCY_NAMES_OPTIMIZERS[optimizer]
        )

    ax.set_xlabel("Function evaluations")
    ax.set_ylabel("Current best f(x)")
    # ax.set_title(f"{FANCY_NAMES_MODELS[model_class]} "
                #  f"({size}D) — Problem {problem}")
    if model_class == 'mechbench':
        ax.set_title(f"Problem: {problem} on MECHBench")
    else:
        ax.set_title(f"Problem: {problem} Model Class: {FANCY_NAMES_MODELS[model_class]} Training Data: {size}D")
    ax.legend()
    plt.tight_layout()
    return fig

    # #TODO: define colors for each optimizer

    # # per_optimizer_data = [optimizer for optimizer in data if optimizer["problem"]==problem and optimizer["size"]==size and optimizer["model_class"]==model_class] 

    # fig, ax = plt.subplots(figsize=(8,5))

    # # for d in data:
    # for size, size_data in data.items():#.items():
    #     ax.plot(
    #         size_data['evaluations'],
    #         size_data['best'],
    #         label=size #TODO: color
    #     )

    # ax.set_xlabel("Function evaluations")
    # ax.set_ylabel("Current best f(x)")
    # ax.set_title(f"{FANCY_NAMES_MODELS[model_class]} optimized with {FANCY_NAMES_OPTIMIZERS[optimizer]} (Problem {problem})")
    # ax.legend(title='Training set size (\u00d7n_dimensions)')
    # # ax.grid(True, ls)
    # plt.tight_layout()
    # return fig

def rank(data):
    # rank = pd.DataFrame(data)
    # return rank.rank(axis=1, method='min', ascending=True)
    grid = np.unique(np.concatenate([df.index.values for df in data.values()]))
    aligned = {}
    for optimizer, df in data.items():
        evals = df.index.values
        best = df['best'].values
        idx = np.searchsorted(evals, grid, side='right') - 1
        vals = np.where(idx >= 0, best[np.clip(idx, 0, len(best) - 1)], np.inf)
        aligned[optimizer] = vals
    rank_df = pd.DataFrame(aligned, index=grid)
    return rank_df.rank(axis=1, method='min', ascending=True)

def rank_at_evaluation(rank_data, evaluation):
    idx = rank_data.index[rank_data.index <= evaluation]
    return rank_data.loc[idx.max()]

def plt_rank(data, problem, model, size):

    rank_data = rank(data)
    fig, ax = plt.subplots(figsize=(6, 4.5))
    n_optimizers = rank_data.shape[1]
    evaluations = rank_data.index.values

    for optimizer in rank_data.columns:
        ranks = rank_data[optimizer].values
        line, = ax.step(
            evaluations, ranks, where='post',
            label=FANCY_NAMES_OPTIMIZERS[optimizer],
        )
        changed = np.r_[True, ranks[1:] != ranks[:-1]]
        ax.plot(evaluations[changed], ranks[changed], 'o', color=line.get_color(), markersize=5)

    ax.set_ylim(0.5, n_optimizers + 0.5)
    ax.set_yticks(range(1, n_optimizers + 1))
    ax.set_xlabel("evaluations")
    ax.set_ylabel("rank")
    ax.set_title(f"Problem: {problem} Model Class: {FANCY_NAMES_MODELS[model]} Training Data: {size}D")
    ax.legend()
    plt.tight_layout()

def aocc(best, lb, ub):

    y = np.asarray(best, dtype=float)
    y_normalized = (np.minimum(np.maximum(y, lb), ub) - lb)/(ub-lb)
    aocc = 1-y_normalized
    return float(np.mean(aocc))


def kendalls_tau(problem, mechbench_ranking, models_rankings, classes, sizes, slices):

    rows = "ugh" #TODO: correct this
    matrix = pd.DataFrame(index=rows, columns=slices)

    for model in classes:
        for size in sizes:

            row = f"{model}_{size}D"

            for evaluation in slices:
                mechbench_ranking_at_evaluation = rank_at_evaluation(mechbench_ranking, evaluation)
                model_ranking_at_evaluation = rank_at_evaluation(models_rankings[model][size], evaluation)

                tau, p = kendalltau(mechbench_ranking_at_evaluation, model_ranking_at_evaluation)
                matrix.iloc[row, evaluation] = tau
        
    # matrix.to_csv(f'tau_matrices/tau_p{problem}.csv', index=False)
    return matrix

# def get_ranking(problem, model):
#     aocc_table = pd.read_csv(f'aocc_tables/p{problem}/aocc_{model}.csv')
#     sorted_all_sizes = {
#         '30D': [],
#         '60D': [],
#         '125D': [],
#         '250D': [],
#         '500D': []

#     }
    
#     for size in aocc_table.iloc[:,:]:
#         if size not in ['30', '60', '125', '250', '500']:
#             optimizers = aocc_table[size]
#             continue
#         size_aoccs = aocc_table[size]
#         # optimizers = size_aoccs.index.values
#         size_list = []
#         # for size_aocc in size_aoccs:
#         #     for optimizer in optimizers:
#         for size_aocc, optimizer in zip(size_aoccs, optimizers):
#                 # aocc = float(aocc_table.loc[optimizer, size])
#             size_list.append((size_aocc, optimizer))
#         # optimizers = size.index.values()
#         # size_list = []
#         # for optimizer in optimizers:
#         #     aocc = size[optimizer]
#         #     size_list.append((aocc, optimizer))
        
#         sorted_algos = sorted(size_list, reverse=True)
#         for _, algo in sorted_algos:
#             sorted_all_sizes[f'{size}D'].append(FANCY_NAMES_OPTIMIZERS[algo])
#         # sorted_all_sizes[f'{size}D'] = 
#         # print(sorted_algos)

        
#     ranking_df = pd.DataFrame(sorted_all_sizes)
    

#     return ranking_df

    
    
