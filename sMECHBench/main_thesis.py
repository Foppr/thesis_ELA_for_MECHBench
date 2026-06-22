import ioh
from models import RSM, RandomForestModel, XGBModel, GPModel, BayesianNetworkModel 
from optimizers.maria_laura.wrapper import Py_CMA_ES_Wrapper, turbo1Wrapper, BO_botorchWrapper, BAxUS_botorchWrapper
from optimizers.maria_laura.wrapper import wrapopt
from optimizers.modde.modularde import ModularDE
from optimizers.modde.parameters import Parameters
from optimizers.jacob.algorithms.one_plus_one_es import OnePlusOneES
from scipy.optimize import differential_evolution
from optimizers.DE_wrapper import DE
from optimizers.OnePlusOneES_wrapper import OnePlusOneESWrapper
from MECHBench.smechbench_experiment_utils import get_objective_function

from tqdm import tqdm

import numpy as np
import warnings

# SEED = 1312


def get_models(problem, size):
    MODELS_SEED = 1312
    if problem==1:
        targets = ['intrusion', 'specific_energy_absorbed']
    elif problem==2:
        targets = ['intrusion', 'mass']
    elif problem==3:
        targets = ['load_uniformity']

    models = {
        "rsm" : {f'rsm_{target}' : RSM.load(f'RSM_{target}_p{problem}_{size}D.pkl', target=target, problem=problem, dset_size=size, seed=MODELS_SEED) for target in targets},
        "rf" : { f'rf_{target}': RandomForestModel.load(f'RF_{target}_p{problem}_{size}D.pkl', problem=problem, target=target, dset_size=size, seed=MODELS_SEED) for target in targets },
        "xgb" : {f'xgb_{target}' : XGBModel.load(f'XGB_{target}_p{problem}_{size}D.ubj', problem=problem, target=target, dset_size=size, seed=MODELS_SEED) for target in targets},
        "gp" : {f'gp_{target}' : GPModel.load(f'GP_{target}_p{problem}_{size}D.pt') for target in targets},
        "bn" : {f'bayesian' : BayesianNetworkModel.load(f"BN_p{problem}_{size}D.pkl", problem, size, MODELS_SEED)}
    }

    return models

#TODO: The rest of the params
def instantiate_optimizers(obj_function, dim, SEED):

    ub = 5
    lb = -5
    budget = 30*dim
    doe_size = 3*dim

    cmaes = Py_CMA_ES_Wrapper(obj_function, dim, ub, lb , budget, SEED)
    turbo1 = turbo1Wrapper(obj_function, dim, ub, lb, budget, doe_size, SEED)
    botorch = BO_botorchWrapper(obj_function, dim, ub, lb, budget, doe_size, SEED)
    baxus = BAxUS_botorchWrapper(obj_function, dim, ub, lb, budget, doe_size, SEED)

    # cmaes = wrapopt("pyCMA")

    de = DE(obj_function, dim, ub, lb)
    # de_params = Parameters(d=dim)
    # de = ModularDE(fitness_func=obj_function, parameters=de_params) #TODO: how to configure unsure
    one_plus_one = OnePlusOneESWrapper(obj_function, budget)

    return {
        "cmaes" : cmaes,
        "turbo1" : turbo1,
        "botorch" : botorch,
        "baxus" : baxus,
        "de" : de,
        "one_plus_one" : one_plus_one
    }

def instantiate_optimizer(obj_function, dim, optimizer_name, SEED):
    ub = 5
    lb = -5
    budget = 30*dim
    doe_size = 3*dim

    if optimizer_name=='cmaes':
        return Py_CMA_ES_Wrapper(obj_function, dim, ub, lb, budget, SEED)
    
    if optimizer_name == 'turbo1':
        return turbo1Wrapper(obj_function, dim, ub, lb, budget, doe_size, SEED)
    
    if optimizer_name == 'botorch':
        return BO_botorchWrapper(obj_function, dim, ub, lb, budget, doe_size, SEED)
    
    if optimizer_name == 'baxus':
        return BAxUS_botorchWrapper(obj_function, dim, ub, lb, budget, doe_size, SEED)
    
    if optimizer_name == 'de':
        return DE(obj_function, dim, ub, lb)
    
    if optimizer_name == 'one_plus_one':
        return OnePlusOneESWrapper(obj_function, budget)
    
    

def aocc(all_the_parameters):
    #TODO: calculate aocc
    pass

#TODO: adapt for model sizes
def model_obj_function(problem, model_class, models):
    if problem == 1:
        if model_class == 'bn':
            model = models[model_class]['bayesian']
        else:
            model_intrusion = models[model_class][f'{model_class}_intrusion']
            model_sea = models[model_class][f'{model_class}_specific_energy_absorbed']
        def f(point):  # point?
            point = point.reshape(1,-1)
            if model_class == 'bn':
                preds = model.predict(point)
                delta = preds['intrusion'].iloc[0]#, target='intrusion')
                SEA = preds['specific_energy_absorbed'].iloc[0]#, target='specific_energy_absorbed')
            # elif model_class=='gp':
            #     delta = model_intrusion.predict(point)[0]
            #     SEA = model_mass.
            else:
                # delta = model_intrusion.model.predict(point)
                # SEA = model_sea.model.predict(point)
                delta = model_intrusion.predict(point)[0]
                SEA = model_sea.predict(point)[0]
            if delta > 60:
                return 100*(delta - 60)
            else:
                return -1*SEA
    
    if problem == 2:
        if model_class == 'bn':
            model = models[model_class]['bayesian']
        else:
            model_intrusion = models[model_class][f'{model_class}_intrusion']
            model_mass = models[model_class][f'{model_class}_mass']
        def f(point):
            point = point.reshape(1,-1)
            if model_class == 'bn':

                delta = model.predict(point)['intrusion'].iloc[0]
                m = model.predict(point)['mass'].iloc[0]
            else:
                # delta = model_intrusion.model.predict(point)
                # m = model_mass.model.predict(point)
                delta = model_intrusion.predict(point)[0]
                m = model_mass.predict(point)[0]


            if delta > 50:
                return 4.25952+10*(((delta)/(50)) - 1)
            else:
                return m
            
    if problem == 3:

        if model_class == 'bn':
            model_lu = models[model_class][f'bayesian']
        else:
            model_lu = models[model_class][f'{model_class}_load_uniformity']

        def f(point):
            point = point.reshape(1,-1)
            if model_class == 'bn':
                # evidence = point.to_dictionary_somehow
                # lu = model_lu.magic_prediction_method_ypeee(evidence, target='load_uniformity')
                lu = model_lu.predict(point)[0]

            else:
                lu = model_lu.predict(point)[0]

            return lu
        
    return f

def evaluate_vectors_with_model(model, problem, models_dict, vectors):
    f = model_obj_function(problem, model, models_dict, vectors)

    return [f(vector) for vector in vectors]

def evaluate_vector_with_mechbench(problem, vectors):
    f = get_objective_function(problem)

    return [f(vector) for vector in vectors]

def show_and_save_rankings(results_path):
    #TODO: takes optimizer data and generates rankings side by side, save in csv and display in terminal
    pass

def main():
    problems = [1,2,3]
    sizes = [30, 60, 125, 250, 500]
    # sizes = [60, 125]
    # problems = [1, 2]



    #TODO: do this 15 times and avg
    n_models = 1 # change to 5 for all or 1 for bayesian
    n_optimizers = 2
    n_iterations = 1#5
    n_total = len(problems)*len(sizes)*n_models*n_optimizers*n_iterations
    with tqdm(total=n_total) as pbar:
        for problem in problems:
        # for problem in tqdm(problems, desc="problems"):
            for size in sizes:
            # for size in tqdm(sizes, desc="sizes", leave=False):
                if problem == 1 or problem == 2:
                    dim = 5
                elif problem == 3:
                    dim = 15

                #TODO: run what is needed on mechbench

                models_dict = get_models(problem, size)

                for model_class, models in models_dict.items():
                    f = model_obj_function(problem, model_class, models_dict)

                    optimizers_dict = {
                        # "cmaes" : None,
                        # "turbo1" : None,
                        # "botorch" : None,
                        # "baxus" : None,
                        "de" : None,
                        "one_plus_one" : None

                    }

                    for optimizer_name, _ in optimizers_dict.items():
                        f_wrapped = ioh.wrap_problem(
                            f,
                            name=f"p{problem}_{model_class}_{size}D",
                            optimization_type=ioh.OptimizationType.MIN,
                            lb=-5,
                            ub=5,
                            dimension=dim
                        )

                        logger = ioh.logger.Analyzer(
                            # root=ioh.logger.Path(f"analysis/logger_data/p{problem}/{model_class}/{size}D"),
                            root=f'analysis/test_dir/logger/data/p{problem}/{model_class}/{size}D',
                            folder_name=f"{optimizer_name}",
                            algorithm_name=f"{optimizer_name}_{model_class}_p{problem}{size}D",
                            store_positions=True,
                            triggers=[ioh.logger.trigger.ALWAYS]
                        )

                        f_wrapped.attach_logger(logger)

                        # optimizers=instantiate_optimizers(f_wrapped, dim)
                        # print(f"running optimizer: {optimizer_name} for model {model_class} and size {size}D")
                        tqdm.write(f"\nProblem: {problem} \nOptimizer: {optimizer_name}\nModel: {model_class}\nSize: {size}D\n")
                        optimizer = instantiate_optimizer(f_wrapped, dim, optimizer_name)
                        optimizer.run()

                        logger.close()
                        pbar.update(1)


    # models_dict = get_models(2, 125)
    # f = model_obj_function(2, 'rsm', models_dict)

    # dim = 5
    # test_points = np.random.uniform(-5, 5, size=(10, dim))
    # for i, p in enumerate(test_points):
    #     val = f(p)
    #     print(f"point {i}: {val}")

                # logger = ioh.logger.Analyzer( # is problem
                #     #TODO: fix parameters
                #     root=ioh.logger.Path(f"analysis/logger_data/p{problem}/{model_class}"),
                #     folder_name= f"{model_class}_p{problem}_{size}D_seed{SEED}", 
                #     algorithm_name=f"{model_class}_p{problem}_{size}D_seed{SEED})",
                #     store_positions=True
                # )
                
                
                
                # f = model_obj_function(problem, model_class, models_dict)

                # f_wrapped = ioh.wrap_problem(f)

                # f_wrapped.attach_logger(logger)

                # optimizers = instantiate_optimizers(f_wrapped, dim)

                # # for optimizer_name, optimizer in optimizers.items():
                # #     optimizer.run()
                # optimizers["botorch"].run()

            
    
    # show_and_save_rankings(results_path="figure this out")
            

if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    SEED = 1312
    main()



