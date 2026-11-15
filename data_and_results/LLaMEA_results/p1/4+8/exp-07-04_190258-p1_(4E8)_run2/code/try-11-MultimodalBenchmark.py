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
        f2 = 0.15 * np.sum(np.sin(6.0 * x) * np.exp(-0.15 * x**2))
        
        # Additional challenging landscape with shifted components
        f3 = 0.02 * np.sum(np.cos(12.0 * x) * np.exp(-0.07 * x**2))
        
        # Cross-terms to increase interaction between dimensions
        f4 = 0.05 * np.sum(x[:-1] * x[1:] * np.sin(2.0 * x[:-1] + 3.0 * x[1:]))
        
        return f1 + f2 + f3 + f4