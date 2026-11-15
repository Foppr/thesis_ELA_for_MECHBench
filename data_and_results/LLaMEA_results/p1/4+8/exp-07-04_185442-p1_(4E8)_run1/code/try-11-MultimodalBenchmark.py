import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Multimodal term with altered frequencies and added sine interactions
        f2 = 0.15 * np.sum(np.cos(7 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Additional penalty term with higher order polynomial
        f3 = 0.02 * np.sum(x_norm**6)
        
        # Cross-term interaction to increase conditioning difficulty
        f4 = 0.05 * np.sum(x_norm[:-1] * x_norm[1:])
        
        return f1 + f2 + f3 + f4