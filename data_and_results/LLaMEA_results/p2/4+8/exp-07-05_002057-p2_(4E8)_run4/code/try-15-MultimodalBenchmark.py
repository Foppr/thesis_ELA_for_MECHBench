import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Nested multimodal term with varying frequencies
        f2 = 0.5 * np.sum(np.sin(10 * x) * np.cos(5 * x) * np.exp(-0.1 * x**2))
        
        # Additional ridge-like structure
        f3 = 0.3 * np.sum(np.sin(3 * x) * np.cos(7 * x) * np.exp(-0.05 * x**2))
        
        # Central basin with multiple local minima
        f4 = 0.2 * np.sum(np.sin(15 * x) * np.exp(-0.2 * x**2))
        
        return f1 + f2 + f3 + f4