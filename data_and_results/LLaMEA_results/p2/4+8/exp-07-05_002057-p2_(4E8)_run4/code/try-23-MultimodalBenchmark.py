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
        f2 = 0.15 * np.sum(np.sin(7 * x) * np.exp(-0.15 * x**2))
        
        # Additional oscillatory term with higher frequency
        f3 = 0.08 * np.sum(np.cos(15 * x) * np.exp(-0.08 * x**2))
        
        # Cross-term interaction to increase conditioning
        f4 = 0.02 * np.sum(x[:-1] * x[1:] * np.sin(3 * x[:-1] + 2 * x[1:]))
        
        return f1 + f2 + f3 + f4