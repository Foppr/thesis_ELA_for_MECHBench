import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of squares term
        f1 = np.sum(x**2)
        
        # Enhanced multimodal term with multiple local minima
        f2 = 0.2 * np.sum(np.sin(3.0 * x) * np.exp(-0.15 * x**2))
        
        # Additional challenging landscape with higher frequency oscillations
        f3 = 0.05 * np.sum(np.cos(15.0 * x) * np.exp(-0.03 * x**2))
        
        # Cross-term interaction to increase dimensionality challenge
        f4 = 0.1 * np.sum(np.sin(2.0 * x) * np.cos(4.0 * x) * np.exp(-0.1 * x**2))
        
        return f1 + f2 + f3 + f4