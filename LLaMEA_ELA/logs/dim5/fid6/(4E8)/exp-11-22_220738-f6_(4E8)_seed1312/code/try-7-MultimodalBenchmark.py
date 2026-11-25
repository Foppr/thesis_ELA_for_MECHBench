import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with different frequencies
        f2 = np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        # Sum of exponential terms to create multiple local minima
        f3 = np.sum(np.exp(-x_norm**2) * np.cos(2 * np.pi * x_norm))
        
        # Combine terms with different weights to create complex landscape
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 10 * np.sum(np.sin(x_norm)) + 5 * np.sum(np.cos(x_norm))