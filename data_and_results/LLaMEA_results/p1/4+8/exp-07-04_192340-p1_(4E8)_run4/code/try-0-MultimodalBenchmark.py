import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms with different frequencies
        f2 = np.sum(np.sin(5 * np.pi * x_normalized) ** 2)
        
        # Product term creating complex landscape
        f3 = np.prod(np.cos(x_normalized))
        
        # Combine terms with different weights
        result = 0.5 * f1 + 0.3 * f2 + 0.2 * f3
        
        # Add a small noise term to make it non-convex
        noise = 0.01 * np.sum(np.random.random(self.dim) * x_normalized**2)
        
        return result + noise