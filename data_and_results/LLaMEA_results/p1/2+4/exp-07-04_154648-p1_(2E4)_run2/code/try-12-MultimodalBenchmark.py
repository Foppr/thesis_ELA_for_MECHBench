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
        f2 = 0.3 * np.sum(np.sin(9 * np.pi * x_norm)**10)
        f3 = 0.15 * np.sum(np.cos(5 * np.pi * x_norm)**8)
        f4 = 0.08 * np.sum((x_norm - 0.4)**6)
        f5 = 0.25 * np.sum(np.sin(3 * np.pi * x_norm)**4)
        f6 = 0.1 * np.sum(np.cos(6 * np.pi * x_norm)**5)
        
        # Combine terms
        return f1 + f2 + f3 + f4 + f5 + f6