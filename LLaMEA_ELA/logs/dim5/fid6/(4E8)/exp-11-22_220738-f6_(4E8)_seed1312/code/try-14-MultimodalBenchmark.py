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
        f2 = np.sum(np.sin(7 * np.pi * x_norm)**2)
        
        # Sum of exponential terms with shifted arguments to create multiple local minima
        f3 = np.sum(np.exp(-x_norm**2) * np.cos(3 * np.pi * x_norm + 1.0))
        
        # Additional interaction terms between dimensions
        f4 = np.sum(np.sin(x_norm[:-1] - x_norm[1:])**2)
        
        # Combine terms with different weights to create complex landscape
        return 0.6 * f1 + 0.25 * f2 + 0.15 * f3 + 0.3 * f4 + 8 * np.sum(np.sin(x_norm)) + 4 * np.sum(np.cos(x_norm))