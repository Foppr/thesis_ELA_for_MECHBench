import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms to create multiple local minima
        f2 = np.sum(np.sin(5 * np.pi * x_normalized)**2)
        
        # Additional penalty term for large values
        f3 = 0.1 * np.sum(np.abs(x_normalized)**3)
        
        # Combine terms with different weights
        return f1 + 0.5 * f2 + f3