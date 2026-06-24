import ioh
# from models import RSM, RandomForestModel, XGBModel, GPModel #,  BayesianNetworkModel
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
