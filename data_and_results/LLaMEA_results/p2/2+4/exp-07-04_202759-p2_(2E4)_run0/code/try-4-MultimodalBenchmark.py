import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with multiple local minima (modified frequency)
        f2 = np.sum(np.sin(7 * np.pi * x_norm)**2)
        
        # Product term that creates complex landscape (modified coefficient)
        f3 = np.prod(np.cos(3 * np.pi * x_norm) + 0.3)
        
        # Additional polynomial interaction term
        f4 = np.sum(x_norm**4)
        
        # Combine terms with different weights to create challenging landscape
        return f1 + 0.15 * f2 + 0.02 * f3 + 0.05 * f4