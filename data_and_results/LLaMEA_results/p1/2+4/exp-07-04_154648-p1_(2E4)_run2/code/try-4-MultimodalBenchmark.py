import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Additional multimodal terms with local minima
        f2 = 0.2 * np.sum(np.sin(7 * np.pi * x_norm)**8)
        f3 = 0.1 * np.sum(np.cos(4 * np.pi * x_norm)**6)
        f4 = 0.05 * np.sum((x_norm - 0.3)**4)
        
        # Combine terms
        return f1 + f2 + f3 + f4