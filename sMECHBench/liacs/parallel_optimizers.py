import argparse
import sys
sys.path.append('..')
from main_thesis import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--problem',    type=int, choices=[1, 2, 3])
    parser.add_argument('--size',       type=int, choices=[30, 60, 125, 250, 500])
    parser.add_argument('--model',      type=str, choices=['rsm', 'rf', 'xgb', 'gp', 'bn'])
    parser.add_argument('--optimizer',  type=str, choices=['cmaes', 'turbo1', 'botorch', 'baxus', 'de', 'one_plus_one'])
    parser.add_argument('--iterations', type=int, default=1)
    parser.add_argument('--seed', type=int, default=1312)
    args = parser.parse_args()

    SEED = args.seed
    dim = 5 if args.problem==1 or args.problem==2 else 15

    models_dict = get_models(args.problem, args.size)

    f_no_clip = model_obj_function(args.problem, args.model, models_dict)
    f = lambda x: f_no_clip(np.clip(x, -5, 5))

    for i in range(args.iterations):
        f_wrapped = ioh.wrap_problem(
            f,
            name=f"p{args.problem}_{args.model}_{args.size}D",
            optimization_type=ioh.OptimizationType.MIN,
            lb=-5, 
            ub=5,
            dimension=dim,
        )

        logger = ioh.logger.Analyzer(
            root=f'analysis/logger_data/iteration_seed_{SEED}/p{args.problem}/{args.model}/{args.size}D',
            folder_name=args.optimizer,
            algorithm_name=f"{args.optimizer}_{args.model}_p{args.problem}_{args.size}D",
            store_positions=True,
            triggers=[ioh.logger.trigger.ALWAYS]
        )

        f_wrapped.attach_logger(logger)

        # print(f"Problem: {args.problem} | Model: {args.model} | Size: {args.size}D | Optimizer: {args.optimizer} | Run: {i+1}/{args.iterations}")
        optimizer = instantiate_optimizer(f_wrapped, dim, args.optimizer, SEED)
        optimizer.run()
        logger.close()


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    SEED = 1312
    main()