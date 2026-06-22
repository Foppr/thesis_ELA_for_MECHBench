import os
import sys
import numpy as np
import ioh
from ioh import ProblemClass
from modde.modularde import ModularDE  # New import for Modular DE

current_script_dir = os.path.dirname(os.path.abspath(__file__))
thesis_code_dir = os.path.abspath(os.path.join(current_script_dir, ".."))
mechbench_path = os.path.join(thesis_code_dir, "MECHBench", "MECHBench")
sys.path.append(mechbench_path)

from src import sob

deck_id = 100  # <-- EDIT deck_id

runnerOptions = {
    "np": 1,  # Number of processes to run the simulation
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
        alg_name = "L-SHADE"
        print(f"Running MECHBench {problem_id} on alg {alg_name} (Dim: {dim})")

        outputs = problem_output_types[problem_id]
        problem = sob.get_problem(problem_id, dim, outputs, runner_options=runnerOptions)

        f = lambda x: problem(np.asarray(x), deck_id=deck_id)

        # Wrap the MECHBench problem into IOHexperimenter
        f_wrapped = ioh.wrap_problem(
            f,
            name=f"mechbench_p{problem_id}_{alg_name}",
            optimization_type=ioh.OptimizationType.MIN,
            lb=-5,
            ub=5,
            dimension=dim
        )

        # Correcting explicit bounds allocation safely
        f_wrapped.bounds.lb = np.full(dim, -5.0)
        f_wrapped.bounds.ub = np.full(dim, 5.0)

        budget = 30 * dim

        # Initialize ModularDE with the exact configuration from the README
        # We pass the wrapped function and specify the evaluation budget directly
        lshade = ModularDE(
            f_wrapped,
            budget=budget,
            base_sampler='uniform',
            mutation_base='target',
            mutation_reference='pbest',
            bound_correction='expc_center',
            crossover='bin',
            lpsr=True,
            lambda_=18 * dim,
            memory_size=6,
            use_archive=True,
            init_stats=True,
            adaptation_method_F='shade',
            adaptation_method_CR='shade'
        )

        # Setup Logging
        logger = ioh.logger.Analyzer(
            algorithm_name=alg_name,
            root="data",
            folder_name=alg_name,
            store_positions=True,
            triggers=[ioh.logger.trigger.ALWAYS]  # Log every step
        )

        # Watch internal ModDE parameters if initialized successfully
        if hasattr(lshade, "parameters") and hasattr(lshade.parameters, "stats"):
            logger.watch(lshade.parameters.stats, "curr_F")
            logger.watch(lshade.parameters.stats, "curr_CR")

        # Attach the logger to the wrapped problem context
        f_wrapped.attach_logger(logger)

        # Execute the algorithm loop
        lshade.run()

        print(f"Finished MECHBench {problem_id} successfully.")