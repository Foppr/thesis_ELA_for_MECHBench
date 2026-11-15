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
        f2 = np.sum(np.sin(4 * np.pi * x_norm) ** 2 + 0.3 * np.sin(8 * np.pi * x_norm) ** 2)
        
        # Higher order polynomial terms for additional complexity
        f3 = np.sum(x_norm**5 + 0.2 * x_norm**7)
        
        # Cross-terms to increase dimensionality interaction
        f4 = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(3 * np.pi * x_norm[:-1] * x_norm[1:]))
        
        # Additional quadratic cross-terms for increased complexity
        f5 = np.sum((x_norm[:-2] * x_norm[1:-1] * x_norm[2:]) ** 2)
        
        # Combine all terms with carefully tuned weights
        return f1 + 0.25 * f2 + 0.03 * f3 + 0.15 * f4 + 0.05 * f5