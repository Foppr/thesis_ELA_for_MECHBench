import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with shifted phase to create more complex landscape
        f2 = np.sum(np.sin(7 * np.pi * (x_norm + 0.15)) ** 2)
        
        # Product term with modified frequency to increase dimension interaction
        f3 = np.prod(np.cos(0.9 * np.pi * x_norm))
        
        # Additional cubic term for increased nonlinearity
        f4 = np.sum(x_norm**3)
        
        # Cross-term interaction between dimensions
        f5 = np.sum(x_norm[:-1] * x_norm[1:])
        
        # Combine terms with different weights
        result = 0.3 * f1 + 0.35 * f2 + 0.25 * f3 + 0.05 * f4 + 0.05 * f5
        
        return result