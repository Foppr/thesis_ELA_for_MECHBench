import numpy as np
from scipy.optimize import differential_evolution

class DE:
    def __init__(self, objective_function, dim, ub, lb):#, **kwargs):
        self.objective_function = objective_function
        bounds = [(lb, ub) for _ in range(dim)]
        self.bounds = bounds
        self.result = None

    def run(self):
        self.result = differential_evolution(self.objective_function, self.bounds)#, **self.kwargs)
        return self.result
