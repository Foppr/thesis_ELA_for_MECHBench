import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of squared terms with different scales
        term1 = np.sum(x_normalized**2)
        
        # Product of cosines creating multiple local minima
        term2 = np.prod(np.cos(0.5 * x_normalized))
        
        # Additional sinusoidal component for complexity
        term3 = np.sum(np.sin(0.3 * x_normalized**2))
        
        # Combine terms with different weights
        result = 10 * term1 + 5 * term2 + 2 * term3
        
        return result