import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms to create multiple local minima
        f2 = 0.1 * np.sum(np.sin(5 * np.pi * x_norm))
        
        # Product term to create complex landscape
        f3 = np.prod(np.cos(0.5 * np.pi * x_norm))
        
        # Combine terms with different weights
        result = f1 + f2 + 0.5 * f3
        
        return result