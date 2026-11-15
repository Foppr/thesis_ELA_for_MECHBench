import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Enhanced multimodal terms with higher-order nonlinearities
        f2 = 0.3 * np.sum(np.sin(9 * np.pi * x_norm)**10)
        f3 = 0.25 * np.sum(np.cos(5 * np.pi * x_norm)**8)
        f4 = 0.15 * np.sum(np.sin(3 * np.pi * x_norm)**6)
        f5 = 0.1 * np.sum((x_norm + 0.2)**6)
        f6 = 0.08 * np.sum(np.cos(7 * np.pi * x_norm)**4)
        
        # Cross-terms for increased interaction between dimensions
        cross_term = 0.05 * np.sum(x_norm[:-1] * x_norm[1:] * np.sin(2 * np.pi * x_norm[:-1]))
        
        # Combine all terms
        return f1 + f2 + f3 + f4 + f5 + f6 + cross_term