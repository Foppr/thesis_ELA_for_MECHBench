import ioh
import warnings
import argparse
import numpy as np
import sys
sys.path.append('..')
from tqdm import tqdm
from main_thesis import instantiate_optimizer
from MECHBench.smechbench_experiment_utils import get_objective_function

import matplotlib
matplotlib.use('Agg')   
import matplotlib.pyplot as plt

def main():
    # problems = [1,2,3]
    # seeds = list(range(1312, 1312+15))
    parser = argparse.ArgumentParser()
    parser.add_argument('--problem', type=int)
    parser.add_argument('--optimizer', type=str)
    parser.add_argument('--deck_id', type=int)
    parser.add_argument('--seed', type=int)
    args = parser.parse_args()


    problem=args.problem
    optimizer_name = args.optimizer
    seed = args.seed
    print(f"---------------------------------")
    print(f"RUNNING SEED {seed} OPTIMIZER {optimizer_name} ON PROBLEM {problem}")

    if problem == 1 or problem == 2:
        dim =5
    else:
        dim = 15

    f_no_deck_id = get_objective_function(problem)
    deck_id = args.deck_id
    f = lambda x: f_no_deck_id(np.clip(x, -5, 5), deck_id=deck_id)

    def dummy_optimum(instance, n_variables):
        return ioh.RealSolution(x=[0]*dim, y=-1e10)

    f_wrapped = ioh.wrap_problem(
        f, 
        name=f"mechbench_p{problem}",
        optimization_type=ioh.OptimizationType.MIN,
        lb=-5,
        ub=5,
        dimension=dim,
        # known_optimum=ioh.RealSolution(x=[0]*dim, y=-1e10)
        calculate_objective=dummy_optimum
    )

    logger = ioh.logger.Analyzer(
        root=f'analysis/logger_data/mechbench/seed{seed}/p{problem}',
        folder_name=f"{optimizer_name}",
        algorithm_name=f"{optimizer_name}_mechbench",
        store_positions=True,
        triggers=[ioh.logger.trigger.ALWAYS]
    )

    f_wrapped.attach_logger(logger)

    optimizer = instantiate_optimizer(f_wrapped, dim, optimizer_name, seed)
    optimizer.run()
    logger.close()

    # n_total = len(problems)*len(seeds)*6
    # with tqdm(total=n_total) as pbar:
    #     for seed in seeds:
    #         for problem in problems:
    #             if problem == 1 or problem == 2:
    #                 dim=5
    #             elif problem == 3:
    #                 dim=15
            
    #             f_no_deck_id = get_objective_function(problem)

    #             f = lambda x: f_no_deck_id(x, deck_id=1)
                
    #             optimizers_dict = {
    #                 "cmaes" : None,
    #                 "turbo1": None,
    #                 "botorch": None,
    #                 "baxus": None,
    #                 "de": None,
    #                 "one_plus_one": None
    #             }

    #             for optimizer_name, _ in optimizers_dict.items():
    #                 f_wrapped = ioh.wrap_problem(
    #                     f,
    #                     name=f"mechbench_p{problem}",
    #                     optimization_type=ioh.OptimizationType.MIN,
    #                     lb=-5,
    #                     ub=5,
    #                     dimension=dim
    #                 )

    #                 logger = ioh.logger.Analyzer(
    #                     root=f'analysis/logger_data/mechbench/seed{seed}/p{problem}',
    #                     folder_name=f"{optimizer_name}",
    #                     algorithm_name=f"{optimizer_name}_mechbench",
    #                     store_positions=True,
    #                     triggers=[ioh.logger.trigger.ALWAYS]
    #                 )

    #                 f_wrapped.attach_logger(logger)

    #                 tqdm.write(f"\nProblem: {problem }\nOptimizer:{optimizer_name}\n")
    #                 optimizer = instantiate_optimizer(f_wrapped, dim, optimizer_name, seed)
    #                 optimizer.run()
    #                 logger.close()
    #                 pbar.update(1)

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    main()
