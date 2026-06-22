from .src import sob
import numpy as np
import pandas as pd
  

runnerOptions = {"np":9, # Number of processes to run the simulation
                 "nt":1,
                 "h_level":1,
                 "gmsh_verbosity":0,
                 "write_vtk":False,
}



def get_objective_function(problem):
    # dim = 15#vector = [np.zeros((20,)).tolist()] # Vector where the objective function is evaluated, it has as many components as the second input argument in get_problem below
    if problem == 1 or problem == 2:
        dim = 5
    elif problem == 3:
        dim = 15
    else:
        raise ValueError("Invalid problem type, give 1, 2, or 3")

    f = sob.get_problem(problem,dim, runner_options=runnerOptions)

    return f