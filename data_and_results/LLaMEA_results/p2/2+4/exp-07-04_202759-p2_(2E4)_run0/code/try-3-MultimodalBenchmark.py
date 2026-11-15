import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with multiple local minima
        f2 = np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        # Product term that creates complex landscape
        f3 = np.prod(np.cos(2 * np.pi * x_norm) + 0.5)
        
        # Combine terms with different weights to create challenging landscape
        return f1 + 0.1 * f2 + 0.01 * f3