import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Add sinusoidal modulation with higher frequency and different coefficient
        f2 = 0.15 * np.sum(np.sin(7 * np.pi * x_norm))
        
        # Add a quartic term to create additional complexity
        f3 = 0.01 * np.sum(x_norm**4)
        
        # Add interactive cross-terms to increase dimensionality interaction
        f4 = 0.05 * np.sum(x_norm[:-1] * x_norm[1:])
        
        return f1 + f2 + f3 + f4