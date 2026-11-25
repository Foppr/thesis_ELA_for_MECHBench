import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Add sinusoidal oscillations to create multiple local minima
        f2 = 0.1 * np.sum(np.sin(5 * np.pi * x_norm))
        
        # Add a quartic term to increase complexity
        f3 = 0.01 * np.sum(x_norm**4)
        
        # Combine terms with different weights
        result = f1 + f2 + f3
        
        return result