import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Highly multimodal term with exponentially increasing frequency
        f2 = 0.5 * np.sum(np.cos(np.pi * np.exp(2 * np.abs(x_norm)) * x_norm))
        
        # Additional complex penalty term to encourage convergence
        f3 = 0.05 * np.sum(np.abs(x_norm)**3)
        
        # Add a hard constraint term to increase difficulty
        f4 = 2.0 * np.sum(np.sin(3 * np.pi * x_norm)**4)
        
        return f1 + f2 + f3 + f4