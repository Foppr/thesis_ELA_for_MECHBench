import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of squared terms with different weights
        term1 = np.sum(x_norm**2)
        
        # Product of cosines creating multiple local minima
        term2 = np.prod(np.cos(0.5 * x_norm))
        
        # Additional sinusoidal component for complexity
        term3 = np.sum(np.sin(0.7 * x_norm))
        
        # Combine terms with different weights
        result = 0.1 * term1 - term2 + 0.05 * term3
        
        # Add a small noise term to make it non-trivial
        result += 0.01 * np.random.random()
        
        return result