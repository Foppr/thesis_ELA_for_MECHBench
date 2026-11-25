import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different weights
        quadratic = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms to create multiple local minima
        sinusoidal = np.sum(np.sin(5 * np.pi * x_norm))
        
        # Additional penalty term for large values
        penalty = 0.1 * np.sum(x_norm**4)
        
        return quadratic + sinusoidal + penalty