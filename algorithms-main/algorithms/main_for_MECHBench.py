import os
import sys
import numpy as np
import ioh
from ioh import ProblemClass
from datetime import datetime

now = datetime.now().strftime('%Y_%m_%d_%H%M')

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


deck_id = 100  # <-- EDIT deck_id


class JdenobelWrapper:
    def __init__(self, f, optimizer):
        self.f = f
        self.optimizer = optimizer

    def run(self):
        return self.optimizer(self.f)


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


if __name__ == '__main__':
    for problem_id, dim in [(1, 5), (2, 5), (3, 15)]:
        for alg, alg_name in [(ParticleSwarmOptimization, 'PSO'), (OnePlusOneES, 'OnePlusOneES')]:
            print(f"Running MECHBench {problem_id} on alg {alg_name}")

            outputs = problem_output_types[problem_id]
            problem = sob.get_problem(problem_id, dim, outputs, runner_options=runnerOptions)

            f = lambda x: problem(np.asarray(x), deck_id=deck_id)

            f_wrapped = ioh.wrap_problem(
                f,
                name=f"mechbench_p{problem_id}_{alg_name}_{now}",
                optimization_type=ioh.OptimizationType.MIN,
                lb=-5,
                ub=5,
                dimension=dim
            )

            budget = 30 * dim
            optimizer = alg(budget=budget)

            # Logging
            logger = ioh.logger.Analyzer(
                algorithm_name=alg_name,
                root="data",
                folder_name=f"{alg_name}_{now}",
                store_positions=True,
                triggers=[ioh.logger.trigger.ALWAYS]  # Log at every step, not just improvements (there will be just 30D lines anyway)
            )

            if hasattr(optimizer, "sigma"):
                logger.watch(optimizer, "sigma")

            f_wrapped.attach_logger(logger)

            opoesw = JdenobelWrapper(f=f_wrapped, optimizer=optimizer)

            if alg == OnePlusOneES:
                # Decrease step size σ:
                # Currently sigma = np.linalg.norm(problem.bounds.lb - problem.bounds.ub) / np.sqrt(problem.meta_data.n_variables)
                # Which equals 4.47. So a0 easily goes out of bounds
                opoesw.sigma0 = 1.0

            opoesw.run()
