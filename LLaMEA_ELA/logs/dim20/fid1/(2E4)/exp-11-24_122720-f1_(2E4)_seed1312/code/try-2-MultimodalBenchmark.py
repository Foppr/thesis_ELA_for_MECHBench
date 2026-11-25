import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sine terms with different frequencies
        f2 = np.sum(np.sin(5 * np.pi * x_norm))
        
        # Product of cosines for additional complexity
        f3 = np.prod(np.cos(2 * np.pi * x_norm))
        
        # Combine terms with different weights to create multimodality
        return 0.1 * f1 - 0.01 * f2 + 0.05 * f3 + 1.0