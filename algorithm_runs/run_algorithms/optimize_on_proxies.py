import ioh
import warnings
import argparse
import numpy as np
import os
import sys
sys.path.append('..')
sys.path.append('../..')
from tqdm import tqdm
from main_analysis import instantiate_optimizer
from process_results import LLaMEAAnalyzer
import gpytorch
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    problems = [1, 2, 3]
    seed = int(os.environ.get("SEED", 1312))
    optimizers = ['cmaes', 'de', 'one_plus_one', 'turbo1', 'botorch', 'baxus']
    print(f'\n\n### SEED {seed} ###\n\n')
    i = 0
    for problem in problems:  # 3
        for optimizer_name in optimizers:  # 6
            print(f"---------------------------------\n")
            print(f"RUNNING SEED {seed} OPTIMIZER {optimizer_name} ON PROBLEM {problem}\n")
            print(f"---------------------------------\n")

            if problem == 1 or problem == 2:
                dim = 5
            else:
                dim = 15

            def dummy_optimum(instance, n_variables):
                return ioh.RealSolution(x=[0]*dim, y=-1e10)

            # Get proxy code
            base_dir = 'exps_0704'
            analyzer = LLaMEAAnalyzer(save_folder_name='llamea_graphs')
            analyzer.load_logs(base_dir)

            log = analyzer.log

            total = log[f'p{problem}'][f'p{problem}_total']

            proxies = analyzer.get_podium_median_worst(total)

            for ranking in proxies:  # podium, median, worst
                for proxy in ranking.iterrows():  # number 1, 2, 3  # 9
                    i += 1
                    standing = proxy[1]['standing']
                    print(f'Starting run on {standing} --- {i} / 162')

                    name = proxy[1]['name']
                    code = proxy[1]['code']
                    exec(code, globals())

                    proxy_class = globals()[name]
                    proxy_instance = proxy_class(dim=dim)
                    f = proxy_instance.f

                    f_wrapped = ioh.wrap_problem(
                        f,
                        name=f"p{problem}_seed{seed}_{standing}_opt{optimizer_name}",
                        optimization_type=ioh.OptimizationType.MIN,
                        lb=-5,
                        ub=5,
                        dimension=dim,
                        # known_optimum=ioh.RealSolution(x=[0]*dim, y=-1e10)
                        calculate_objective=dummy_optimum
                    )

                    logger = ioh.logger.Analyzer(
                        root=f'analysis/logger_data/proxies/seed{seed}/p{problem}/{standing}',
                        folder_name=f"{optimizer_name}",
                        algorithm_name=f"{optimizer_name}_mechbench",
                        store_positions=True,
                        triggers=[ioh.logger.trigger.ALWAYS]
                    )

                    f_wrapped.attach_logger(logger)

                    optimizer = instantiate_optimizer(f_wrapped, dim, optimizer_name, seed)

                    try:
                        optimizer.run()
                    except Exception as e:
                        errors = open('errors_algo_runs.txt', 'a')
                        line = f'p{problem} | {seed} | {optimizer_name} | {standing} RAN INTO AN ERROR --- {type(e)}: {e}\n'
                        errors.write(line)
                        print(line)
                        errors.close()

                    # optimizer.run()
                    logger.close()


if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    # Add jitted to protect against cholesky failing (rugged proxies vs. botorch)
    with gpytorch.settings.cholesky_jitter(1e-3), gpytorch.settings.cholesky_max_tries(6):
        main()
