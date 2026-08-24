import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        f1 = np.sum(x**2)
        
        # Multimodal term with higher frequency oscillations and exponential decay
        f2 = 0.2 * np.sum(np.sin(10 * x) * np.exp(-0.2 * x**2))
        
        # Additional high-frequency oscillatory term with different decay
        f3 = 0.15 * np.sum(np.cos(15 * x) * np.exp(-0.1 * x**2))
        
        # Cross-term interaction to increase complexity
        f4 = 0.05 * np.sum(np.sin(3 * x) * np.cos(7 * x) * np.exp(-0.05 * x**2))
        
        return f1 + f2 + f3 + f4