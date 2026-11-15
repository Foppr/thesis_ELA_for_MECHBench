import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of squares term (global minimum at origin)
        f1 = np.sum(x_normalized**2)
        
        # Highly multimodal term with exponentially increasing local minima
        f2 = np.sum(np.sin(np.pi * x_normalized * np.exp(2 * np.abs(x_normalized)))**4)
        
        # Additional penalty term to make the landscape more challenging
        f3 = 0.05 * np.sum(np.abs(x_normalized)**0.3)
        
        # Add a large global penalty for values far from the origin
        f4 = 10 * np.exp(-np.sum(x_normalized**2) / 2)
        
        return f1 + 0.5 * f2 + f3 + f4