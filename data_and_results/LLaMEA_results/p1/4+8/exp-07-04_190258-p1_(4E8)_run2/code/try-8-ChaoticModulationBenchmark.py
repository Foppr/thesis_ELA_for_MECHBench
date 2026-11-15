import numpy as np

class ChaoticModulationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match initialized dimension")
        
        # Base quadratic term
        quadratic = 0.1 * np.sum(x**2)
        
        # Chaotic sinusoidal modulation with multiple frequencies
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(2.0 * np.pi * x[i]) * np.cos(3.0 * np.pi * x[i])
            chaotic += 0.5 * np.sin(5.0 * np.pi * x[i]) * np.cos(7.0 * np.pi * x[i])
        
        # Add a saddle point structure
        saddle = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                saddle += (x[i]**2 - x[i+1]**2) * np.sin(0.5 * np.pi * (x[i] + x[i+1]))
        
        # Add a global deceptive term
        deceptive = 0.3 * np.sin(0.2 * np.sum(x**2))
        
        return quadratic + chaotic + saddle + deceptive