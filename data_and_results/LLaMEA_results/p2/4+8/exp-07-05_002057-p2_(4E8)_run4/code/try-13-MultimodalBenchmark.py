import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        f1 = np.sum(x**2)
        
        # High-frequency oscillatory term with exponential growth
        f2 = np.sum(np.sin(10 * x) * np.exp(-0.05 * x**2) * np.cos(20 * x))
        
        # Nested multimodal term with increasing frequency
        f3 = 0.5 * np.sum(np.sin(15 * x) * np.exp(-0.1 * x**2) * np.sin(30 * x))
        
        # Additional complex interaction term
        f4 = 0.3 * np.sum(np.sin(25 * x) * np.cos(5 * x) * np.exp(-0.02 * x**2))
        
        # Combine all terms with varying weights
        return f1 + f2 + f3 + f4