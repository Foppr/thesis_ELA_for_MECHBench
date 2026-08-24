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
        f2 = 0.25 * np.sum(np.sin(12 * x) * np.exp(-0.25 * x**2))
        
        # Additional high-frequency oscillatory term
        f3 = 0.2 * np.sum(np.sin(25 * x) * np.exp(-0.15 * x**2))
        
        # Modified cosine term for more complex landscape
        f4 = 0.15 * np.sum(np.cos(18 * x) * np.exp(-0.1 * x**2))
        
        # Cross-term interaction to increase complexity
        f5 = 0.08 * np.sum(x[:-1] * x[1:] * np.sin(6 * (x[:-1] + x[1:])))
        
        # Additional nonlinear interaction term
        f6 = 0.1 * np.sum(np.sin(x**3) * np.exp(-0.05 * x**2))
        
        return f1 + f2 + f3 + f4 + f5 + f6