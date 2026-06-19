import sys
from pathlib import Path
import os
root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root))

mechbench_path = os.path.abspath("MECHBench/MECHBench")
sys.path.append(mechbench_path)

from MECHBench.MECHBench.src import sob  # Uncomment/change if you run in a parent folder
# from src import sob  # Uncomment if you run in the MECHBench folder

import numpy as np
import pandas as pd
from sampler import sampler


'''
Added the following block to identify if the current system 
'''

#runnerOptions = {"open_radioss_main_path":"/home/ivanolar/Documents/OpenRadioss2/OpenRadioss_linux64/OpenRadioss/",
#                 "write_vtk":False,
#                 "np":4, # Number of processes to run the simulation
#                 "nt":1,
#                 "h_level":1,
#                 "gmsh_verbosity":0,
#}   

runnerOptions = {"np":1, # Number of processes to run the simulation
                 "nt":8,
                 "h_level":1,
                 "gmsh_verbosity":0,
}

r'''
Once the optimization problem instance has been generate, 
the model is determined (mesh and fem data loaded) only when the variable array has been input.
'''


def main():#p=2, dim=5, size=125):

    # handle arguments
    # p = sys.argv[0]
    # dim = sys.argv[1]
    # size = sys.argv[2]
    # filename = sys.argv[3]

    if sys.argv[1] is None:
        p = 2
    else:
        p = int(sys.argv[1])

    if sys.argv[2] is None:
        dim = 5
    else:
        dim = int(sys.argv[2])

    if sys.argv[3] is None:
        size = 500
    else:
        size = int(sys.argv[3])

    sim_id = 1869  # Attribute to define the simulation id and connected results folder name
    dim = dim #vector = [np.zeros((20,)).tolist()] # Vector where the objective function is evaluated, it has as many components as the second input argument in get_problem below
    problem_id = p  # 1: star box, 2: three point bending, 3: crash tube
    n_datapoints = size*dim
    seed = 42

    filename_points = f"points_{size}d{dim}_p{p}_seed_{seed}.csv"
    filename_obj_values = f"objective_values_{size}d{dim}_p{p}.csv"

    vector = np.random.uniform(0,0,(dim,)).tolist()  # Vector where the objective function is evaluated, it has as many components as the second input argument in get_problem below
    print(f"Evaluating vector: {vector}")

    problem_output_types = {
        1: ["intrusion", "specific-energy-absorbed", "penalized_sea"],
        2: ["intrusion", "penalized_mass", "mass"],
        3: ["load_uniformity"]
    }

    outputs = problem_output_types[p]
    f = sob.get_problem(problem_id, dim, outputs, runner_options=runnerOptions)
    points = sampler(n_datapoints, seed=seed)
    points.to_csv(f"{filename_points}")

    objective_values = pd.DataFrame(columns=outputs)
    for i, point in enumerate(points.iterrows()):
        obj_value = f(point[1], sim_id)
        objective_values.loc[i] = obj_value
        print(obj_value)

    objective_values.to_csv(f"{filename_obj_values}")


if __name__ == '__main__':
    main()
