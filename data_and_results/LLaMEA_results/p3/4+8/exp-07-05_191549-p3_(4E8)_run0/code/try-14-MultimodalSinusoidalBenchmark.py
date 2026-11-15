import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add sinusoidal modulation with multiple peaks
        for i in range(self.dim):
            f_val += 0.15 * np.sin(6 * x[i]) * np.cos(4 * x[i])
        
        # Add grid-like structure with multiple local minima
        grid_term = 0
        for i in range(self.dim):
            grid_term += 0.8 * np.sin(3 * np.pi * x[i] / 2.0) * np.cos(3 * np.pi * x[i] / 2.0)
        
        # Add interaction terms between dimensions with higher complexity
        interaction_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += 0.02 * np.sin(2 * x[i] + x[j]) * np.cos(x[i] - 2 * x[j])
        
        # Add a small perturbation term to increase landscape irregularity
        perturbation = 0
        for i in range(self.dim):
            perturbation += 0.05 * np.sin(7 * x[i]) * np.cos(5 * x[i])
        
        return f_val + 0.6 * grid_term + interaction_term + perturbation