import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with multiple local minima and varying frequencies
        f2 = np.sum(np.sin(7 * np.pi * x_norm) ** 2 + 0.5 * np.sin(3 * np.pi * x_norm) ** 2)
        
        # Additional penalty term to create more complex landscape
        f3 = np.sum(x_norm**4)
        
        # Cross-terms to introduce interactions between dimensions
        f4 = 0.1 * np.sum(x_norm[:-1] * x_norm[1:])
        
        return f1 + 0.15 * f2 + 0.01 * f3 + 0.05 * f4