import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        f1 = np.sum(x**2)
        
        # Enhanced multimodal term with stronger oscillations
        f2 = 0.2 * np.sum(np.sin(10 * x) * np.exp(-0.2 * x**2))
        
        # Additional high-frequency oscillatory term
        f3 = 0.15 * np.sum(np.sin(20 * x) * np.exp(-0.1 * x**2))
        
        # Modified cosine term for more complex landscape
        f4 = 0.1 * np.sum(np.cos(15 * x) * np.exp(-0.05 * x**2))
        
        # Cross-term interaction to increase complexity
        f5 = 0.05 * np.sum(x[:-1] * x[1:] * np.sin(5 * (x[:-1] + x[1:])))
        
        return f1 + f2 + f3 + f4 + f5