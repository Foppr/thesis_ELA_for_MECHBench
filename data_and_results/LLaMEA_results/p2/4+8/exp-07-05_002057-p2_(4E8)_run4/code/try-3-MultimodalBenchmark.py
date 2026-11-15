import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of squares term
        f1 = np.sum(x**2)
        
        # Multimodal term with multiple local minima
        f2 = 0.1 * np.sum(np.sin(5 * x) * np.exp(-0.1 * x**2))
        
        # Additional oscillatory term
        f3 = 0.05 * np.sum(np.cos(10 * x) * np.exp(-0.05 * x**2))
        
        return f1 + f2 + f3