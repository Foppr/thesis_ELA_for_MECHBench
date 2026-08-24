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
            f_val += 0.1 * np.sin(5 * x[i]) * np.cos(3 * x[i])
        
        # Add grid-like structure with multiple local minima
        grid_term = 0
        for i in range(self.dim):
            grid_term += np.sin(2 * np.pi * x[i] / 2.0) * np.cos(2 * np.pi * x[i] / 2.0)
        
        # Add interaction terms between dimensions
        interaction_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += 0.01 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        return f_val + 0.5 * grid_term + interaction_term