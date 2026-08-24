import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        f1 = np.sum(x**2)
        
        # Multimodal term with higher frequency oscillations and modified exponential decay
        f2 = 0.25 * np.sum(np.sin(12 * x) * np.exp(-0.25 * x**2))
        
        # Additional high-frequency oscillatory term with different decay
        f3 = 0.18 * np.sum(np.cos(18 * x) * np.exp(-0.15 * x**2))
        
        # Cross-term interaction to increase complexity
        f4 = 0.07 * np.sum(np.sin(4 * x) * np.cos(9 * x) * np.exp(-0.08 * x**2))
        
        # Additional nonlinear interaction term
        f5 = 0.03 * np.sum((x**3) * np.sin(5 * x) * np.exp(-0.1 * x**2))
        
        return f1 + f2 + f3 + f4 + f5