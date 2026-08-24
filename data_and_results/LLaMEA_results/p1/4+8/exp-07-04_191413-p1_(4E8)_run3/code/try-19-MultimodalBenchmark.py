import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Multiple sinusoidal terms with different frequencies to create complex landscape
        f2 = np.sum(np.sin(3 * np.pi * x_norm) ** 2 + 0.5 * np.sin(6 * np.pi * x_norm) ** 2)
        
        # Higher order polynomial terms for additional complexity
        f3 = np.sum(x_norm**4 + 0.3 * x_norm**6)
        
        # Cross-terms to increase dimensionality interaction
        f4 = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(2 * np.pi * x_norm[:-1] * x_norm[1:]))
        
        # Combine all terms with carefully tuned weights
        return f1 + 0.2 * f2 + 0.05 * f3 + 0.1 * f4