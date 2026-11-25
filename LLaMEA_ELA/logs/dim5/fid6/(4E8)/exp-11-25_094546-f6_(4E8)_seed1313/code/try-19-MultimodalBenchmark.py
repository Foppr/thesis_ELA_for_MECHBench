import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with higher frequency to create more local minima
        f2 = np.sum(np.sin(8 * np.pi * x_norm) ** 2)
        
        # Additional cubic polynomial terms for increased nonlinearity
        f3 = np.sum(x_norm**3)
        
        # Product term to create interaction between dimensions
        f4 = np.prod(np.cos(0.3 * np.pi * x_norm))
        
        # Combine terms with different weights to control difficulty
        return f1 + 0.15 * f2 + 0.05 * f3 - 0.03 * f4