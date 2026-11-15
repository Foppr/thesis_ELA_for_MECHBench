import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Multimodal term with multiple local minima using higher frequency cosine
        f2 = 0.15 * np.sum(np.cos(7 * np.pi * x_norm))
        
        # Additional sine term to create more complex landscape
        f3 = 0.08 * np.sum(np.sin(3 * np.pi * x_norm))
        
        # Shifted local minima using sine modulation
        f4 = 0.05 * np.sum(np.sin(2 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Fourth-order penalty term
        f5 = 0.02 * np.sum(x_norm**4)
        
        return f1 + f2 + f3 + f4 + f5