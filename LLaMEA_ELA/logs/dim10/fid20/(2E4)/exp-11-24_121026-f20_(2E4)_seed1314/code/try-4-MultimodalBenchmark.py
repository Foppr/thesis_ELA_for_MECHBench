import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with multiple local minima and modified frequency
        f2 = np.sum(np.sin(7 * np.pi * x_norm)**6)
        
        # Additional cubic term for non-convexity with altered coefficient
        f3 = np.sum(x_norm**3)
        
        # Cross-term interaction between dimensions to increase complexity
        f4 = 0.05 * np.sum(x_norm[:-1] * x_norm[1:])
        
        return f1 + 0.15 * f2 + 0.02 * f3 + f4