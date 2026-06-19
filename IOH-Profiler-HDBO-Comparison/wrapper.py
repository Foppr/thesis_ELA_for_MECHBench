import time
import numpy as np
import sys
import os
from ioh import get_problem

mechbench_path = os.path.abspath("../MECHBench/MECHBench")
sys.path.append(mechbench_path)

from MECHBench.MECHBench.src import sob  # Uncomment/change if you run in a parent folder
# from src import sob  # Uncomment if you run in the MECHBench folder

import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

class Py_CMA_ES_Wrapper:
    def __init__(self, func, dim, ub, lb, total_budget, random_seed):
        import pathlib
        my_dir = pathlib.Path(__file__).parent.resolve()
        bayes_bo_lib = os.path.join(
            my_dir, 'mylib', 'lib_BO_bayesoptim', 'Bayesian-Optimization')
        self.func = func
        self.dim = dim
        self.total_budget = total_budget
        self.random_seed = random_seed
        self.ub = ub
        self.lb = lb

    def run(self):
        from bayes_optim import RandomForest, BO, GaussianProcess
        import cma
        from bayes_optim.extension import RealSpace

        import random
        space = RealSpace([self.lb, self.ub], random_seed=self.random_seed) * self.dim
        ma = float('-inf')
        argmax = None
        for i in range(10*self.dim):
            x = space.sample(1)[0]
        def generate_initial_point():
            return np.random.uniform(low=self.lb, high=self.ub, size = self.dim)

        cma.fmin2(self.func, generate_initial_point, 1., restarts=5,options={'bounds': [

                 [self.lb]*self.dim, [self.ub]*self.dim], 'maxfevals': self.total_budget, 'seed': self.random_seed, 'tolx': 1e-8})


    

        def get_acq_time(self):
            return self.opt.acq_opt_time

        def get_mode_time(self):
            return self.opt.mode_fit_time

        def get_iter_time(self):
            return self.opt.cum_iteration_time

class SaasboWrapper:
    def __init__(self, func, dim, ub, lb, total_budget, DoE_size, random_seed):
        import pathlib
        my_dir = pathlib.Path(__file__).parent.resolve()
        sys.path.append(os.path.join(my_dir, 'mylib', 'lib_saasbo'))

        self.func = func
        self.dim = dim
        self.ub = ub
        self.lb = lb
        self.total_budget = total_budget
        self.Doe_size = DoE_size
        self.random_seed = random_seed

    def run(self):
        #from saasbo import run_saasbo, get_acq_time, get_mode_time
        from saasbo import Saasbo


        # run_saasbo(
        #     self.func,
        #     np.ones(self.dim) * self.ub,
        #     np.ones(self.dim) * self.lb,
        #     self.total_budget,
        #     self.Doe_size,
        #     self.random_seed,
        #     alpha=0.01,
        #     num_warmup=256,
        #     num_samples=256,
        #     thinning=32,
        #     device="cpu",
        # )

        self.opt = Saasbo(func=self.func,
                          dim=self.dim,
                          ub=self.ub,
                          lb=self.lb,
                          total_budget=self.total_budget,
                          DoE_size=self.Doe_size,
                          random_seed=self.random_seed)

        print(self.opt.run_saasbo(self.func,np.ones(self.dim) * self.ub,np.ones(self.dim) * self.lb,self.total_budget,self.Doe_size,self.random_seed,alpha=0.01,num_warmup=256,num_samples=256,thinning=32,device="cpu",))

    def get_acq_time(self):
        return self.opt.acq_opt_time

    def get_mode_time(self):
        return self.opt.mode_fit_time

    def get_iter_time(self):
        return self.opt.cum_iteration_time



class BO_sklearnWrapper:
    def __init__(self, func, dim, ub, lb, total_budget, DoE_size, random_seed):
        import pathlib
        my_dir = pathlib.Path(__file__).parent.resolve()
        sys.path.append(os.path.join(my_dir, 'mylib', 'lib_BO_sklearn'))

        self.func = func
        self.dim = dim
        self.ub = ub
        self.lb = lb
        self.total_budget = total_budget
        self.Doe_size = DoE_size
        self.random_seed = random_seed

    def run(self):
        from bosklearn import bosklearn

        self.opt= bosklearn(func=self.func,
                          dim=self.dim,
                          ub=self.ub,
                          lb=self.lb,
                          total_budget=self.total_budget,
                          DoE_size=self.Doe_size,
                          random_seed=self.random_seed)
        self.opt.gp_minimize(self.func,  # the function to minimize
                    # the bounds on each dimension of x
                    list((((self.lb, self.ub),) * self.dim)),
                    acq_func="EI",  # the acquisition function
                    n_calls=self.total_budget,  # the number of evaluations of f
                    n_random_starts=self.Doe_size,  # the number of random initialization points
                    noise=0.1 ** 2,  # the noise level (optional)
                    random_state=self.random_seed)

    def get_acq_time(self):
        return self.opt.acq_opt_time

    def get_mode_time(self):
        return self.opt.mode_fit_time

    def get_iter_time(self):
        return self.opt.cum_iteration_time

class BO_bayesoptimWrapper:
    # BO of Hao
    def __init__(self, func, dim, ub, lb, total_budget, DoE_size, random_seed):
        sys.path.append('./mylib/' + 'lib_' + "BO_bayesoptim")
        print(sys.path)

        self.func = func
        self.dim = dim
        self.ub = ub
        self.lb = lb
        self.total_budget = total_budget
        self.Doe_size = DoE_size
        self.random_seed = random_seed

    def run(self):
        from bayes_optim import BO, RealSpace
        from bayes_optim.surrogate import GaussianProcess

        space = RealSpace([self.lb, self.ub]) * \
            self.dim  # create the search space

        # hyperparameters of the GPR model
        thetaL = 1e-10 * (self.ub - self.lb) * np.ones(self.dim)
        thetaU = 10 * (self.ub - self.lb) * np.ones(self.dim)
        model = GaussianProcess(  # create the GPR model
            thetaL=thetaL, thetaU=thetaU
        )

        opt = BO(
            search_space=space,
            obj_fun=self.func,
            model=model,
            DoE_size=self.Doe_size,  # number of initial sample points
            max_FEs=self.total_budget,  # maximal function evaluation
            verbose=True
        )
        opt.run()


class BO_development_bayesoptimWrapper:
    # Latest changes from Hao's repository
    def __init__(self, func, dim, ub, lb, total_budget, DoE_size, random_seed):
        import pathlib
        my_dir = pathlib.Path(__file__).parent.resolve()
        bayes_bo_lib = os.path.join(
            my_dir, 'mylib', 'lib_BO_bayesoptim', 'Bayesian-Optimization')
        if not os.path.isdir(bayes_bo_lib):
            raise ImportError(
                'No such module Bayesian-Optimization, please consider cloning this repository: https://github.com/wangronin/Bayesian-Optimization to the folder mylib/lib_BO_bayesoptim/')
        sys.path.insert(0, bayes_bo_lib)
        print(sys.path)

        self.func = func
        self.dim = dim
        self.ub = ub
        self.lb = lb
        self.total_budget = total_budget
        self.Doe_size = DoE_size
        self.random_seed = random_seed

    def run(self):
        from bayes_optim.extension import RealSpace
        from bayes_optim.bayes_opt import BO

        space = RealSpace([self.lb, self.ub], random_seed=self.random_seed) * self.dim
        opt = BO(
            search_space=space,
            obj_fun=self.func,
            DoE_size=self.Doe_size,
            n_point=1,
            random_seed=self.random_seed,
            acquisition_optimization={"optimizer": "BFGS"},
            max_FEs=self.total_budget,
            verbose=False,
        )
        opt.run()

class KPCABOWrapper:
     # Latest changes from Hao's repository
    def __init__(self, func, dim, ub, lb, total_budget, DoE_size, random_seed):
        import pathlib
        my_dir = pathlib.Path(__file__).parent.resolve()
        bayes_bo_lib = os.path.join(
            my_dir, 'mylib', 'lib_BO_bayesoptim', 'Bayesian-Optimization')
        if not os.path.isdir(bayes_bo_lib):
            raise ImportError(
                'No such module Bayesian-Optimization, please unzip the folder Bayesian-Optimization.zip and move the unzip folder to mylib/lib_BO_bayesoptim/')
        sys.path.insert(0, bayes_bo_lib)
        print(sys.path)

        self.func = func
        self.dim = dim
        self.ub = ub
        self.lb = lb
        self.total_budget = total_budget
        self.Doe_size = DoE_size
        self.random_seed = random_seed

    def run(self):
        

        from bayes_optim import RandomForest, BO, GaussianProcess

        from bayes_optim.extension import PCABO, RealSpace, KernelPCABO, KernelFitStrategy
        from bayes_optim.mylogging import eprintf

        import random   
        

        space = RealSpace([self.lb, self.ub], random_seed=self.random_seed) * self.dim
        self.opt = KernelPCABO(
            search_space=space,
            obj_fun=self.func,
            DoE_size=self.Doe_size,
            max_FEs=self.total_budget,
            verbose=False,
            n_point=1,
            acquisition_optimization={"optimizer": "BFGS"},
            max_information_loss=0.1,
            kernel_fit_strategy=KernelFitStrategy.AUTO,
            NN=self.dim,
            random_seed=self.random_seed
        )

        print(self.opt.run())

    def get_acq_time(self):
        return self.opt.acq_opt_time

    def get_mode_time(self):
        return self.opt.mode_fit_time

    def get_iter_time(self):
        return self.opt.cum_iteration_time


class randomWrapper:
    def __init__(self, func, dim, ub, lb, total_budget, DoE_size, random_seed):

        self.func = func
        self.dim = dim
        self.ub = ub
        self.lb = lb
        self.total_budget = total_budget
        self.Doe_size = DoE_size
        self.random_seed = random_seed

    def run(self):
        import ioh

        def random_search(func, search_space, budget):
            """
               Implementa la ricerca casuale per minimizzare un problema di dimensione n.

               Parameters:
               - objective_function: La funzione obiettivo da minimizzare. Deve accettare un vettore di dimensione n come input e restituire un valore numerico.
               - search_space: Una lista di tuple, ognuna contenente il range di valori ammissibili per ciascuna dimensione.
               - budget: Il numero massimo di valutazioni della funzione obiettivo consentite.

               Returns:
               - best_solution: La migliore soluzione trovata.
               - best_score: Il valore minimo della funzione obiettivo associato alla migliore soluzione.
               """
            best_solution = None
            best_score = float('inf')

            for _ in range(budget):
                solution = [np.random.uniform(low, high) for (low, high) in search_space]
                score = self.func(solution)

                # Aggiorna la migliore soluzione se necessario
                if score < best_score:
                    best_solution = solution
                    best_score = score
                print(best_score)
            return best_solution, best_score
        search_space = [(self.lb, self.ub) for _ in range(self.dim)]
        budget = self.total_budget
        random_search(self.func, search_space, budget)


class linearPCABOWrapper:
    def __init__(self, func, dim, ub, lb, total_budget, DoE_size, random_seed):
        #import sys
        #sys.path.append('./mylib/' + 'lib_' + "linearPCABO")
        #print(sys.path)
        import pathlib
        my_dir = pathlib.Path(__file__).parent.resolve()
        bayes_bo_lib = os.path.join(
            my_dir, 'mylib', 'lib_BO_bayesoptim', 'Bayesian-Optimization')
        if not os.path.isdir(bayes_bo_lib):
            raise ImportError(
                'No such module Bayesian-Optimization, please unzip the folder Bayesian-Optimization.zip and move the unzip folder to mylib/lib_BO_bayesoptim/')
        sys.path.insert(0, bayes_bo_lib)
        print(sys.path)
        #sys.path.insert(0, bayes_bo_lib)
        #print(sys.path)
        self.func = func
        self.dim = dim
        self.ub = ub
        self.lb = lb
        self.total_budget = total_budget
        self.Doe_size = DoE_size
        self.random_seed = random_seed

    def run(self):
        #import sys
        #sys.path.insert(0, "./mylib/lib_linearPCABO/Bayesian-Optimization")
        from bayes_optim.extension import PCABO, RealSpace

        space = RealSpace([self.lb, self.ub]) * self.dim
        self.opt = PCABO(
            search_space=space,
            obj_fun=self.func,
            DoE_size=self.Doe_size,
            max_FEs=self.total_budget,
            verbose=False,
            n_point=1,
            n_components=0.90,
            acquisition_optimization={"optimizer": "BFGS"},
            random_seed=self.random_seed
        )
        
        print(self.opt.run())

    def get_acq_time(self):
        return self.opt.acq_opt_time

    def get_mode_time(self):
        return self.opt.mode_fit_time

    def get_iter_time(self):
        return self.opt.cum_iteration_time


class RDUCBWrapper:
    def __init__(self, func, dim, ub, lb, total_budget, DoE_size, random_seed):
        # import sys
        # sys.path.append('./mylib/' + 'lib_' + "linearPCABO")
        # print(sys.path)
        import pathlib
        my_dir = pathlib.Path(__file__).parent.resolve()
        sys.path.append(os.path.join(my_dir, 'mylib', 'lib_RDUCB/HEBO/RDUCB'))
        print(sys.path)
        # sys.path.insert(0, bayes_bo_lib)
        # print(sys.path)
        self.func = func
        self.dim = dim
        self.ub = ub
        self.lb = lb
        self.total_budget = total_budget
        self.Doe_size = DoE_size
        self.random_seed = random_seed

    def run(self):
        # import sys
        # sys.path.insert(0, "./mylib/lib_linearPCABO/Bayesian-Optimization")

        from hdbo.algorithms import RDUCB
        self.opt = RDUCB( algorithm_random_seed=self.random_seed,
    eps=-1,
    exploration_weight= 'lambda t: 0.5 * np.log(2*t)',
    graphSamplingNumIter=100,
    learnDependencyStructureRate=1,
    lengthscaleNumIter=2,
    max_eval=-4,
    noise_var= 0.1,
    param_n_iter=16,
    size_of_random_graph=0.2,
    # data_random_seed=self.random_seed,
    fn_noise_var=0.15,
    grid_size=150,
    fn= self.func,
n_iter=self.total_budget-self.Doe_size,
n_rand=self.Doe_size, dim=self.dim,)
        self.opt.run()

    def get_acq_time(self):
        return self.opt.mybo.acq_opt_time

    def get_mode_time(self):
        return self.opt.mybo.mode_fit_time

    def get_iter_time(self):
        return self.opt.mybo.cum_iteration_time


class turbo1Wrapper:
    def __init__(self, func, dim, ub, lb, total_budget, DoE_size, random_seed):
        #import sys
        #sys.path.append('./mylib/' + 'lib_' + "turbo1")
        #print(sys.path)
        import pathlib
        my_dir = pathlib.Path(__file__).parent.resolve()
        sys.path.append(os.path.join(my_dir, 'mylib', 'lib_turbo1'))
        print(sys.path)
        
        self.func = func
        self.dim = dim
        self.ub = ub
        self.lb = lb
        self.total_budget = total_budget
        self.Doe_size = DoE_size
        self.random_seed = random_seed

    def run(self):
        from turbo import Turbo1
        import torch
        import math
        import matplotlib
        import matplotlib.pyplot as plt
        self.opt = Turbo1(
            f=self.func,  # Handle to objective function
            lb=np.ones(self.dim) * self.lb,  # Numpy array specifying lower bounds
            ub=np.ones(self.dim) * self.ub,  # Numpy array specifying upper bounds
            n_init=self.Doe_size,  # Number of initial bounds from an Latin hypercube design
            max_evals=self.total_budget,  # Maximum number of evaluations
            batch_size=5,  # How large batch size TuRBO uses
            verbose=True,  # Print information from each batch
            use_ard=True,  # Set to true if you want to use ARD for the GP kernel
            max_cholesky_size=2000,  # When we switch from Cholesky to Lanczos
            n_training_steps=50,  # Number of steps of ADAM to learn the hypers
            min_cuda=1024,  # Run on the CPU for small datasets
            device="cpu",  # "cpu" or "cuda"
            dtype="float64",  # float64 or float32
        )
        self.opt.optimize()

    def get_acq_time(self):
        return self.opt.acq_opt_time

    def get_mode_time(self):
        return self.opt.mode_fit_time

    def get_iter_time(self):
        return self.opt.cum_iteration_time


class turbomWrapper:
    def __init__(self, func, dim, ub, lb, total_budget, DoE_size, random_seed):
        #import sys
        #sys.path.append('./mylib/' + 'lib_' + "turbom")
        #print(sys.path)
        
        import pathlib
        my_dir = pathlib.Path(__file__).parent.resolve()
        sys.path.append(os.path.join(my_dir, 'mylib', 'lib_turbo1'))
        print(sys.path)
        
        self.func = func
        self.dim = dim
        self.ub = ub
        self.lb = lb
        self.total_budget = total_budget
        self.Doe_size = DoE_size
        self.random_seed = random_seed

    def run(self):
        from turbo import TurboM
        import torch
        import math
        import matplotlib
        import matplotlib.pyplot as plt
        #tr = math.floor(self.total_budget / self.Doe_size) - 1
        tr = int(self.dim/5)
        n_init = math.floor(self.Doe_size/tr)
        self.opt = TurboM(
            f=self.func,  # Handle to objective function
            lb=np.ones(self.dim) * self.lb,  # Numpy array specifying lower bounds
            ub=np.ones(self.dim) * self.ub,  # Numpy array specifying upper bounds
            n_init=n_init,  # Number of initial bounds from an Symmetric Latin hypercube design
            max_evals=self.total_budget,  # Maximum number of evaluations
            n_trust_regions=tr,  # Number of trust regions
            batch_size=5,  # How large batch size TuRBO uses
            verbose=True,  # Print information from each batch
            use_ard=True,  # Set to true if you want to use ARD for the GP kernel
            max_cholesky_size=2000,  # When we switch from Cholesky to Lanczos
            n_training_steps=50,  # Number of steps of ADAM to learn the hypers
            min_cuda=1024,  # Run on the CPU for small datasets
            device="cpu",  # "cpu" or "cuda"
            dtype="float64",  # float64 or float32
        )
        self.opt.optimize()

    def get_acq_time(self):
        return self.opt.acq_opt_time

    def get_mode_time(self):
        return self.opt.mode_fit_time

    def get_iter_time(self):
        return self.opt.cum_iteration_time

class EBOWrapper:
    def __init__(self, func, dim, ub, lb, total_budget, DoE_size, random_seed):
         # import sys
                 # sys.path.append('./mylib/' + 'lib_' + "EBO")
                         # print(sys.path)

        import pathlib
        my_dir = pathlib.Path(__file__).parent.resolve()
        sys.path.append(os.path.join(my_dir, 'mylib', 'lib_EBO'))
        print(sys.path)

        self.func = func
        self.dim = dim
        self.ub = ub
        self.lb = lb
        self.total_budget = total_budget
        self.Doe_size = DoE_size
        self.random_seed = random_seed

    def run(self):
        import numpy.matlib as nm
        import functools
        from ebo_core.ebo import ebo
        from test_functions.simple_functions import sample_z
        import time
        import logging

        dx = self.dim
        z = sample_z(dx)
        k = np.array([10] * dx)
        x_range = nm.repmat([[self.lb], [self.ub]], 1, self.dim)
        x_range = x_range.astype(float)
        sigma = 0.01
        n = self.Doe_size
        budget = self.total_budget
        f = self.func
        f = functools.partial(lambda f, x: -f(x), f)
        options = {'x_range': x_range,  # input domain
                  'dx': x_range.shape[1],  # input dimension
                  'max_value': 0,  # target value
                  'T': budget,  # number of iterations
                  'B': 1,  # number of candidates to be evaluated
                  'dim_limit': 3,  # max dimension of the input for each additive function component
                  'isplot': 0,  # 1 if plotting the result; otherwise 0.
                  'z': None, 'k': None,  # group assignment and number of cuts in the Gibbs sampling subroutine
                  'alpha': 1.,  # hyperparameter of the Gibbs sampling subroutine
                  'beta': np.array([5., 2.]),
                  'opt_n': 1000,  # points randomly sampled to start continuous optimization of acfun
                  'pid': 'test3',  # process ID for Azure
                  'datadir': 'tmp_data/',  # temporary data directory for Azure
                  'gibbs_iter': 10,  # number of iterations for the Gibbs sampling subroutine
                  'useAzure': False,  # set to True if use Azure for batch evaluation
                  'func_cheap': True,  # if func cheap, we do not use Azure to test functions
                  'n_add': None,  # this should always be None. it makes dim_limit complicated if not None.
                  'nlayers': 100,  # number of the layers of tiles
                  'gp_type': 'l1',  # other choices are l1, sk, sf, dk, df
                  'gp_sigma': 0.1,  # noise standard deviation
                  'n_bo': 10,  # min number of points selected for each partition
                  'n_bo_top_percent': 0.5,  # percentage of top in bo selections
                  'n_top': 10,  # how many points to look ahead when doing choose Xnew
                  'min_leaf_size': 10,  # min number of samples in each leaf
                  'max_n_leaves': 10,  # max number of leaves
                  'thresAzure': 1,  # if batch size > thresAzure, we use Azure
                  'save_file_name': 'tmp/tmp.pk',
                  }
        self.opt = ebo(f, options)
        start = time.time()
        self.opt.run()

        print("elapsed time: ", time.time() - start)

    def get_acq_time(self):
        return self.opt.acq_opt_time

    def get_mode_time(self):
        return self.opt.mode_fit_time

    def get_iter_time(self):
        return self.opt.cum_iteration_time

class EBO_BWrapper:
    def __init__(self, func, dim, ub, lb, total_budget, DoE_size, random_seed):
         # import sys
                 # sys.path.append('./mylib/' + 'lib_' + "EBO")
                         # print(sys.path)

        import pathlib
        my_dir = pathlib.Path(__file__).parent.resolve()
        sys.path.append(os.path.join(my_dir, 'mylib', 'lib_EBO'))
        print(sys.path)

        self.func = func
        self.dim = dim
        self.ub = ub
        self.lb = lb
        self.total_budget = total_budget
        self.Doe_size = DoE_size
        self.random_seed = random_seed

    def run(self):
        import numpy.matlib as nm
        import functools
        from ebo_core.ebo import ebo
        from test_functions.simple_functions import sample_z
        import time
        import logging

        dx = self.dim
        z = sample_z(dx)
        k = np.array([10] * dx)
        x_range = nm.repmat([[self.lb], [self.ub]], 1, self.dim)
        x_range = x_range.astype(float)
        sigma = 0.01
        n = self.Doe_size
        budget = self.total_budget
        t= int (float(budget)/10)
        f = self.func
        f = functools.partial(lambda f, x: -f(x), f)
        options = {'x_range': x_range,  # input domain
                  'dx': x_range.shape[1],  # input dimension
                  'max_value': 0,  # target value
                  'T': t,  # number of iterations
                  'B': 10,  # number of candidates to be evaluated
                  'dim_limit': 3,  # max dimension of the input for each additive function component
                  'isplot': 0,  # 1 if plotting the result; otherwise 0.
                  'z': None, 'k': None,  # group assignment and number of cuts in the Gibbs sampling subroutine
                  'alpha': 1.,  # hyperparameter of the Gibbs sampling subroutine
                  'beta': np.array([5., 2.]),
                  'opt_n': 1000,  # points randomly sampled to start continuous optimization of acfun
                  'pid': 'test3',  # process ID for Azure
                  'datadir': 'tmp_data/',  # temporary data directory for Azure
                  'gibbs_iter': 10,  # number of iterations for the Gibbs sampling subroutine
                  'useAzure': False,  # set to True if use Azure for batch evaluation
                  'func_cheap': True,  # if func cheap, we do not use Azure to test functions
                  'n_add': None,  # this should always be None. it makes dim_limit complicated if not None.
                  'nlayers': 100,  # number of the layers of tiles
                  'gp_type': 'l1',  # other choices are l1, sk, sf, dk, df
                  'gp_sigma': 0.1,  # noise standard deviation
                  'n_bo': 10,  # min number of points selected for each partition
                  'n_bo_top_percent': 0.5,  # percentage of top in bo selections
                  'n_top': 10,  # how many points to look ahead when doing choose Xnew
                  'min_leaf_size': 10,  # min number of samples in each leaf
                  'max_n_leaves': 10,  # max number of leaves
                  'thresAzure': 1,  # if batch size > thresAzure, we use Azure
                  'save_file_name': 'tmp/tmp.pk',
                  }
        self.opt = ebo(f, options)
        start = time.time()
        self.opt.run()

        print("elapsed time: ", time.time() - start)

    def get_acq_time(self):
        return self.opt.acq_opt_time

    def get_mode_time(self):
        return self.opt.mode_fit_time

    def get_iter_time(self):
        return self.opt.cum_iteration_time

class ALEBOWrapper:
    def __init__(self, func, dim, ub, lb, total_budget, DoE_size, random_seed):
        # import sys
        # sys.path.append('./mylib/' + 'lib_' + "linearPCABO")
        # print(sys.path)
        
        # from ax.modelbridge.strategies.alebo import ALEBOStrategy
        # sys.path.insert(0, bayes_bo_lib)
        # print(sys.path)
        self.func = func
        self.dim = dim
        self.ub = ub
        self.lb = lb
        self.total_budget = total_budget
        self.Doe_size = DoE_size
        self.random_seed = random_seed
        self.iter = 0

    def run(self):
        # import pathlib
        # my_dir = pathlib.Path(__file__).parent.resolve()
        # sys.path.append(os.path.join(my_dir, 'mylib', 'lib_ALEBO'))
        # import numpy as np
        from ax.utils.measurement.synthetic_functions import branin
        print(sys.path)
        
        def branin_evaluation_function(parameterization):
            # Evaluates Branin on the first two parameters of the parameterization.
            # Other parameters are unused.
            x = np.array([parameterization["x0"], parameterization["x1"]])

            return {"objective": (branin(x), 0.0)}
        def function(parameterization):
            # Evaluates Branin on the first two parameters of the parameterization.
            # Other parameters are unused.
            x = np.array([parameterization[f'x{i}'] for i in range(self.dim)])
            self.iter+=1
            if self.iter == self.total_budget:
                print("Optimization is complete, cannot run another trial.")
                exit()
            return {"objective": (self.func(x), 0.0)}
        
        parameters = [
            {"name": "x0", "type": "range", "bounds": [self.lb, self.ub], "value_type": "float"},
            {"name": "x1", "type": "range", "bounds": [self.lb, self.ub], "value_type": "float"},
        ]
        parameters.extend([
            {"name": f"x{i}", "type": "range", "bounds": [self.lb, self.ub], "value_type": "float"}
            for i in range(2, self.dim)
        ])
        from ax.modelbridge.strategies.alebo import ALEBOStrategy
        alebo_strategy = ALEBOStrategy(D=self.dim, d=4, init_size=self.Doe_size)
        alebo_strategy._steps[0].model_kwargs.update({"seed": self.random_seed})
        from ax.service.managed_loop import optimize
        self.opt = optimize(
        parameters=parameters,
        experiment_name="test",
        objective_name="objective",
        evaluation_function=function,
        minimize=True,
        total_trials=self.total_budget,
        generation_strategy=alebo_strategy,
        )
        self.opt()
#     def run(self):
#         # import sys
#         # sys.path.insert(0, "./mylib/lib_linearPCABO/Bayesian-Optimization")
#         parameters = [
#             {"name": "x0", "type": "range", "bounds": [self.lb, self.ub], "value_type": "float"},
#             {"name": "x1", "type": "range", "bounds": [self.lb, self.ub], "value_type": "float"},
#         ]
#         parameters.extend([
#             {"name": f"x{i}", "type": "range", "bounds": [self.lb, self.ub], "value_type": "float"}
#             for i in range(2, self.dim)
#         ])
#         alebo_strategy = ALEBOStrategy(D=self.dim, d=10, init_size=self.Doe_size)
#         from ax.service.managed_loop import optimize
#         self.opt = optimize(
#     parameters=parameters,
#     experiment_name="test",
#     objective_name="objective",
#     evaluation_function=self.func,
#     minimize=True,
#     total_trials=self.total_budget,
#     generation_strategy=alebo_strategy,
# )
#         self.opt()

    def get_acq_time(self):
        return self.opt.acq_opt_time

    def get_mode_time(self):
        return self.opt.mode_fit_time

    def get_iter_time(self):
        return self.opt.cum_iteration_time

class HEBOWrapper:
    def __init__(self, func, dim, ub, lb, total_budget, DoE_size, random_seed):
        # import sys
        # sys.path.append('./mylib/' + 'lib_' + "linearPCABO")
        # print(sys.path)
        # import pathlib
        # my_dir = pathlib.Path(__file__).parent.resolve()
        # sys.path.append(os.path.join(my_dir, 'mylib', 'lib_RDUCB/HEBO/RDUCB'))
        # print(sys.path)
        # sys.path.insert(0, bayes_bo_lib)
        # print(sys.path)
        self.func = func
        self.dim = dim
        self.ub = ub
        self.lb = lb
        self.total_budget = total_budget
        self.Doe_size = DoE_size
        self.random_seed = random_seed

    def run(self):
        # import sys
        # sys.path.insert(0, "./mylib/lib_linearPCABO/Bayesian-Optimization")
        import pandas as pd
        import numpy as np
        from hebo.design_space.design_space import DesignSpace
        from hebo.optimizers.hebo import HEBO
        # def obj(params: pd.DataFrame) -> np.ndarray:
        #     return ((params.values - 0.37) ** 2).sum(axis=1).reshape(-1, 1)
        def obj(params: pd.DataFrame) -> np.ndarray:
            # Imposta la funzione BBOB desiderata (ad esempio, la funzione 1)
            problem = self.func  # Parametri: dimensione, funzione BBOB (1-24)

            # Calcola il valore della funzione obiettivo per ciascuna riga dei parametri
            values = [problem(np.squeeze(row.values)) for _, row in params.iterrows()]

            # Restituisci i valori come un array numpy
            return np.array(values).reshape(-1, 1)

        dimension_specs = [{"name": f"param{i}", "type": "num", 'lb' : self.lb, 'ub' : self.ub } for i in
                           range(1, self.dim + 1)]
        space = DesignSpace().parse(dimension_specs)
        #space = DesignSpace().parse([{'name': 'x', 'type': 'int', 'lb': self.lb, 'ub': self.ub}])
        self.opt = HEBO(space, rand_sample=self.Doe_size, scramble_seed=self.random_seed )
        for i in range(self.total_budget):
            rec = self.opt.suggest(n_suggestions=1)
            self.opt.observe(rec, obj(rec))
            print('After %d iterations, best obj is %.2f' % (i, self.opt.y.min()))
            self.opt.cum_iteration_time = time.process_time()

    def get_acq_time(self):
        return self.opt.acq_opt_time

    def get_mode_time(self):
        return self.opt.mode_fit_time

    def get_iter_time(self):
        return self.opt.cum_iteration_time

import torch
import os
import sys
from botorch.models import SingleTaskGP
try:
    from botorch.fit import fit_gpytorch_mll
except ImportError:
    from botorch.fit import fit_gpytorch_model as fit_gpytorch_mll  # mll does not exist in my botorch version!
try:
    from botorch.acquisition.analytic import LogExpectedImprovement
except ImportError:
    # Fallback to the standard Expected Improvement if Log version is missing
    from botorch.acquisition.analytic import ExpectedImprovement as LogExpectedImprovement
from botorch.optim.optimize import optimize_acqf
from botorch.sampling import SobolQMCNormalSampler
from gpytorch.mlls import ExactMarginalLogLikelihood
from botorch.models.transforms import Normalize, Standardize
class BO_botorchWrapper:
    def __init__(self, func, dim, ub, lb, total_budget, DoE_size, random_seed):
        self.func = func
        self.dim = dim
        self.lb = torch.tensor([lb] * dim, dtype=torch.float32)
        self.ub = torch.tensor([ub] * dim, dtype=torch.float32)
        bounds = torch.stack([self.lb, self.ub])
        self.total_budget = total_budget
        self.DoE_size = DoE_size
        self.random_seed = random_seed
        torch.manual_seed(random_seed)
    def run(self):
        self.X = self.lb + (self.ub - self.lb) * torch.rand((self.DoE_size, self.dim))
        results = [[self.func(x.tolist())] for x in self.X]
        self.Y = torch.tensor(results, dtype=torch.float32).view(-1, 1)

        for i in range(self.total_budget - self.DoE_size):
            self.model = SingleTaskGP(self.X, self.Y, input_transform=Normalize(d=self.dim),
            outcome_transform=Standardize(m=1),)
            self.mll = ExactMarginalLogLikelihood(self.model.likelihood, self.model)
            fit_gpytorch_mll(self.mll)

            EI = LogExpectedImprovement(self.model, best_f=self.Y.max(), maximize=False)
            bounds = torch.stack([self.lb, self.ub]).unsqueeze(1) if self.dim == 1 else torch.stack([self.lb, self.ub])
            candidate, _ = optimize_acqf(
                EI,
                bounds=bounds,
                q=1,
                num_restarts=5,
                raw_samples=20,
            )

            new_y = torch.tensor([[self.func(candidate.tolist()[0])]])

            self.X = torch.cat([self.X, candidate])
            self.Y = torch.cat([self.Y, new_y])


import os
import pathlib
import sys
import numpy as np
import torch


class BAxUS_botorchWrapper:
    def __init__(self, func, dim, ub, lb, total_budget, DoE_size, random_seed, deck_id):
        my_dir = pathlib.Path(__file__).parent.resolve()
        sys.path.append(os.path.join(my_dir, 'mylib', 'lib_BAxUS'))

        self.func = func
        self.dim = dim
        self.ub = ub
        self.lb = lb
        self.total_budget = total_budget
        self.Doe_size = DoE_size
        self.random_seed = random_seed
        self.deck_id = deck_id
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.dtype = torch.double

        # Log configuration
        self.log_dir = os.path.join(my_dir, 'algo_logs')
        os.makedirs(self.log_dir, exist_ok=True)
        func_name = self.func.__class__.__name__
        algo_name = self.__class__.__name__
        base_name = f"{func_name}_{algo_name}_{self.deck_id}_dim{self.dim}_seed{self.random_seed}_budget{self.total_budget}"
        self.log_path = os.path.join(self.log_dir, f"{base_name}.log")

        # Add (1) (2) etc if file already exists
        counter = 1
        while os.path.exists(self.log_path):
            self.log_path = os.path.join(self.log_dir, f"{base_name}({counter}).log")
            counter += 1

        self._write_to_log(f"=== Optimization Started ===")
        self._write_to_log(f"Algorithm: {algo_name} | Deck ID: {self.deck_id} | Budget: {self.total_budget}\n")

    def _write_to_log(self, message):
        """Helper method to append to log file"""
        with open(self.log_path, "a", encoding="utf-8") as log_file:
            log_file.write(str(message) + "\n")

    def _bbob_emb(self, x):
        """ Adatta una funzione BBOB:
            - Scala l'input da [-1,1] a [-5,5]
            - Negativizza per minimizzazione
        """
        x_scaled = self.lb + (self.ub - self.lb) * (x + 1) / 2

        # Log scaling metrics right before OpenRadioss runs
        self._write_to_log(f"[EVALUATION CALL] Target Vector Scaled:\n{x_scaled}")
        self._write_to_log(f"[EVALUATION CALL] Evaluating function: {self.func.__class__.__name__}")

        try:
            val = -self.func(x_scaled.tolist(), self.deck_id)
            self._write_to_log(f"[EVALUATION SUCCESS] Returned value: {val}")
            return val
        except TypeError:
            val = np.negative(self.func(x_scaled.tolist(), self.deck_id))
            self._write_to_log(f"[EVALUATION SUCCESS] Returned value: {val}")
            return val

    def run(self):
        import torch
        import botorch
        import math
        from gpytorch.constraints import Interval
        from gpytorch.kernels import MaternKernel, ScaleKernel
        from gpytorch.likelihoods import GaussianLikelihood
        from gpytorch.mlls import ExactMarginalLogLikelihood
        import gpytorch

        try:
            from botorch.acquisition.analytic import LogExpectedImprovement
        except ImportError:
            from botorch.acquisition.analytic import ExpectedImprovement as LogExpectedImprovement
        try:
            from botorch.exceptions import ModelFittingError
        except ImportError:
            ModelFittingError = RuntimeError
        try:
            from botorch.fit import fit_gpytorch_mll
        except ImportError:
            from botorch.fit import fit_gpytorch_model as fit_gpytorch_mll

        from BAxUS import (
            BaxusState,
            embedding_matrix,
            increase_embedding_and_observations,
            get_initial_points,
            create_candidate,
            update_state,
        )

        dim = self.dim
        n_init = self.Doe_size
        max_cholesky_size = float("inf")
        EVALUATION_BUDGET = self.total_budget
        NUM_RESTARTS = 10
        RAW_SAMPLES = 512
        N_CANDIDATES = min(5000, max(2000, 200 * dim))

        self._write_to_log("Initializing BAxUS Space Strategy...")
        state = BaxusState(dim=dim, eval_budget=EVALUATION_BUDGET - n_init)
        S = embedding_matrix(input_dim=state.dim, target_dim=state.d_init)

        X_baxus_target = get_initial_points(state.d_init, n_init)
        X_baxus_input = X_baxus_target @ S

        self._write_to_log(f"Generating initial DoE Pool of size: {n_init}")
        Y_baxus = torch.tensor(
            [self._bbob_emb(x) for x in X_baxus_input], dtype=self.dtype, device=self.device
        ).unsqueeze(-1)

        with botorch.settings.validate_input_scaling(False):
            for _ in range(EVALUATION_BUDGET - n_init):
                train_Y = (Y_baxus - Y_baxus.mean()) / Y_baxus.std()
                likelihood = GaussianLikelihood(noise_constraint=Interval(1e-8, 1e-3))
                model = SingleTaskGP(X_baxus_target, train_Y, likelihood=likelihood)
                mll = ExactMarginalLogLikelihood(model.likelihood, model)

                with gpytorch.settings.max_cholesky_size(max_cholesky_size):
                    try:
                        fit_gpytorch_mll(mll)
                    except ModelFittingError:
                        self._write_to_log("[WARNING] Cholesky failed, reverting to Adam optimizer.")
                        optimizer = torch.optim.Adam([{"params": model.parameters()}], lr=0.1)
                        for _ in range(100):
                            optimizer.zero_grad()
                            output = model(X_baxus_target)
                            loss = -mll(output, train_Y.flatten())
                            loss.backward()
                            optimizer.step()

                    X_next_target = create_candidate(
                        state=state,
                        model=model,
                        X=X_baxus_target,
                        Y=train_Y,
                        n_candidates=N_CANDIDATES,
                        num_restarts=NUM_RESTARTS,
                        raw_samples=RAW_SAMPLES,
                        acqf="ts",
                    )

                X_next_input = X_next_target @ S
                Y_next = torch.tensor(
                    [self._bbob_emb(x) for x in X_next_input], dtype=self.dtype, device=self.device
                ).unsqueeze(-1)

                state = update_state(state=state, Y_next=Y_next)

                X_baxus_input = torch.cat((X_baxus_input, X_next_input), dim=0)
                X_baxus_target = torch.cat((X_baxus_target, X_next_target), dim=0)
                Y_baxus = torch.cat((Y_baxus, Y_next), dim=0)

                # Log current loop state
                self._write_to_log(
                    f"Iteration {len(X_baxus_input)} | Target Dim: {len(X_baxus_target.T)} | "
                    f"Best Value Found: {state.best_value:.4f} | TR Length: {state.length:.4f}"
                )

                if state.restart_triggered:
                    state.restart_triggered = False
                    self._write_to_log("[RESTART] Target space bounds reached. Splitting target dimensions...")
                    S, X_baxus_target = increase_embedding_and_observations(
                        S, X_baxus_target, state.new_bins_on_split
                    )
                    self._write_to_log(f"[RESTART SUCCESS] New target space dimensionality: {len(S)}")
                    state.target_dim = len(S)
                    state.length = state.length_init
                    state.failure_counter = 0
                    state.success_counter = 0

        self._write_to_log("=== Optimization Finished Smoothly ===")

def wrapopt(optimizer_name, func, ml_dim, ml_total_budget, ml_DoE_size, random_seed, deck_id):
    ub = +5
    lb = -5
    if optimizer_name == "saasbo":
        return SaasboWrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget, DoE_size=ml_DoE_size,
                             random_seed=random_seed)
    if optimizer_name == "BO_sklearn":
        return BO_sklearnWrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget, DoE_size=ml_DoE_size,
                                 random_seed=random_seed)
    if optimizer_name == "BO_bayesoptim":
        return BO_bayesoptimWrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget, DoE_size=ml_DoE_size,
                                    random_seed=random_seed)
    if optimizer_name == "random":
        return randomWrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget, DoE_size=ml_DoE_size,
                             random_seed=random_seed)
    if optimizer_name == "linearPCABO":
        return linearPCABOWrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget, DoE_size=ml_DoE_size,
                             random_seed=random_seed)
    if optimizer_name == "turbo1":
        return turbo1Wrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget, DoE_size=ml_DoE_size,
                             random_seed=random_seed)
    if optimizer_name == "turbom":
        return turbomWrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget, DoE_size=ml_DoE_size,
                             random_seed=random_seed)
    if optimizer_name == 'BO_dev_Hao':
        return BO_development_bayesoptimWrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget, DoE_size=ml_DoE_size,
                             random_seed=random_seed)
    if optimizer_name == 'EBO':
        return EBOWrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget, DoE_size=ml_DoE_size,
                             random_seed=random_seed)
    if optimizer_name == 'EBO_B':
        return EBO_BWrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget, DoE_size=ml_DoE_size,
                             random_seed=random_seed)
    if optimizer_name == 'KPCABO':
        return KPCABOWrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget, DoE_size=ml_DoE_size,
                             random_seed=random_seed)
    if optimizer_name == 'pyCMA':
        return Py_CMA_ES_Wrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget,
                             random_seed=random_seed)

    if optimizer_name == 'RDUCB':
        return RDUCBWrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget, DoE_size=ml_DoE_size,
                             random_seed=random_seed)
    if optimizer_name == 'ALEBO':
        return ALEBOWrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget, DoE_size=ml_DoE_size,
                             random_seed=random_seed)
    if optimizer_name == 'HEBO':
        return HEBOWrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget, DoE_size=ml_DoE_size,
                             random_seed=random_seed)
    if optimizer_name == 'BO_botorch':
        return BO_botorchWrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget, DoE_size=ml_DoE_size,
                             random_seed=random_seed)
    if optimizer_name == 'BAxUS_botorch':
        # ADD: deck_id which is required by AbstractPhysicalModel.__call__
        return BAxUS_botorchWrapper(func=func, dim=ml_dim, ub=ub, lb=lb, total_budget=ml_total_budget, DoE_size=ml_DoE_size,
                             random_seed=random_seed, deck_id=deck_id)


if __name__ == "__main__":
    dim = 5
    total_budget = 30
    doe_size = dim
    seed = 1312

    # MECHBench setup
    problem_id = 1  # <-- CHANGE depending on problem

    runnerOptions = {"np": 1,  # Number of processes to run the simulation
                     "nt": 8,
                     "h_level": 1,
                     "gmsh_verbosity": 0,
                     }
    problem_output_types = {
        1: ["intrusion", "specific-energy-absorbed", "penalized_sea"],
        2: ["intrusion", "penalized_mass", "mass"],
        3: ["load_uniformity"]
    }
    outputs = problem_output_types[problem_id]
    f = sob.get_problem(problem_id, dim, outputs, runner_options=runnerOptions)

    algorithms = ["BO_botorch", "turbo1", "BAxUS_botorch", "pyCMA"]
    algorithm_name = "BAxUS_botorch"
    deck_id = 102
    # f = get_problem(1, dimension=dim, instance=1, problem_type='Real')

    # ADD: deck_id which is required by AbstractPhysicalModel.__call__
    opt = wrapopt(algorithm_name, f, dim, total_budget, doe_size, seed, deck_id)
    opt.run()
