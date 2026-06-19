import os
import sys
import numpy as np
import ioh
from ioh import ProblemClass

current_script_dir = os.path.dirname(os.path.abspath(__file__))
thesis_code_dir = os.path.abspath(os.path.join(current_script_dir, "..", ".."))
mechbench_path = os.path.join(thesis_code_dir, "MECHBench", "MECHBench")
sys.path.append(mechbench_path)

from src import sob
from MECHBench.MECHBench.src import sob  # Uncomment/change if you run in a parent folder
# from src import sob  # Uncomment if you run in the MECHBench folder
from utils import ert, get_meshgrid

from one_plus_one_es import OnePlusOneES
from particle_swarm_optimization import ParticleSwarmOptimization


result_string = (
    "FCE:\t{:10.8f}\t{:10.4f}\n"
    "ERT:\t{:10.4f}\t{:10.4f}\n"
    "{}/{} runs reached target"
)


def run_for_MECHBench(alg, problem_id, dim, iterations, seed):
    print(f"Running algorithm {alg} on MECHBench problem {problem_id}")
    alg_name = str(alg)

    alg.budget = dim * 30  # 30D budget

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
    problem = sob.get_problem(problem_id, dim, outputs, runner_options=runnerOptions)

    fopts = []
    evals = []
    n_succ = 0
    for i in range(iterations):
        np.random.seed(seed + i * 7)
        alg(problem)
        fopts.append(problem.state.current_best.y)
        evals.append(problem.state.evaluations)
        n_succ += (problem.state.current_best.y - problem.optimum.y) < alg.target
        problem.reset()

    print(f"Completed {iterations} reps with {alg_name} on {problem}")
    print(
        result_string.format(
            np.mean(fopts),
            np.std(fopts),
            *ert(evals, n_succ),
            n_succ,
            iterations,
        )
    )
    print()


if __name__ == '__main__':
    # for alg in [OnePlusOneES, ParticleSwarmOptimization]:
    #     for problem in [1, 2, 3]:
    #         run_for_MECHBench(alg, problem, dim=5, iterations=100, seed=42)


    class OnePlusOneESWrapper:
        def __init__(self, f, budget, deck_id):
            self.f = f
            self.optimizer = OnePlusOneES(budget=budget, deck_id=deck_id)

        def run(self):
            return self.optimizer(self.f)

    problem_id = 1
    dim = 5
    runnerOptions = {"np": 1,  # Number of processes to run the simulation
                     "nt": 8,
                     "h_level": 1,
                     "gmsh_verbosity": 0,
                     }

    problem_output_types = {
        1: "penalized_sea",
        2: "penalized_mass",
        3: "load_uniformity"
    }

    outputs = problem_output_types[problem_id]
    problem = sob.get_problem(problem_id, dim, outputs, runner_options=runnerOptions)
    deck_id = 100  # <-- EDIT
    f = lambda x: problem(np.asarray(x), deck_id=deck_id)

    f_wrapped = ioh.wrap_problem(
        f,
        name=f"mechbench_p{problem}",
        optimization_type=ioh.OptimizationType.MIN,
        lb=-5,
        ub=5,
        dimension=dim
    )

    # class Bounds:
    #     def __init__(self, lb, ub):
    #         self.lb = lb
    #         self.ub = ub
    #
    # problem.bounds = Bounds(-5, 5)

    opoesw = OnePlusOneESWrapper(f=f_wrapped, budget=30*dim, deck_id=100)
    opoesw.run()