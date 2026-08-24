import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms with different frequencies
        f2 = np.sum(np.sin(7 * np.pi * x_normalized) ** 2)
        
        # Product term that creates complex interactions
        f3 = np.prod(np.cos(0.3 * np.pi * x_normalized))
        
        # Additional polynomial interaction term
        f4 = np.sum(x_normalized**4)
        
        # Combine terms with different weights
        return f1 + 0.15 * f2 + 0.02 * f3 + 0.05 * f4