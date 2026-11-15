import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_normalized**2)
        
        # Multimodal term with multiple local minima
        f2 = 0.1 * np.sum(np.sin(5 * np.pi * x_normalized)**6)
        
        # Additional penalty term to make the landscape more challenging
        f3 = 0.01 * np.sum(np.abs(x_normalized)**0.5)
        
        return f1 + f2 + f3