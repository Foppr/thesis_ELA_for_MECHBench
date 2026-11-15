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
        f2 = 0.3 * np.sum(np.sin(12 * x) * np.exp(-0.15 * x**2))
        
        # Additional high-frequency oscillatory term with different decay
        f3 = 0.2 * np.sum(np.cos(18 * x) * np.exp(-0.1 * x**2))
        
        # Cross-term interaction to increase complexity
        f4 = 0.1 * np.sum(np.sin(4 * x) * np.cos(9 * x) * np.exp(-0.08 * x**2))
        
        # Additional cross-term with sine and cosine products
        f5 = 0.08 * np.sum(np.sin(6 * x) * np.sin(11 * x) * np.exp(-0.06 * x**2))
        
        # Modified interaction term with polynomial decay
        f6 = 0.05 * np.sum((x**2) * np.sin(8 * x) * np.cos(5 * x) * np.exp(-0.12 * x**2))
        
        return f1 + f2 + f3 + f4 + f5 + f6