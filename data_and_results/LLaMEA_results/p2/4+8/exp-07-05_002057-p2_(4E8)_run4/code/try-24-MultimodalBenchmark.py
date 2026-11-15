import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        f1 = np.sum(x**2)
        
        # Multimodal term with chaotic oscillations and exponential decay
        f2 = 0.3 * np.sum(np.sin(12 * x) * np.exp(-0.15 * x**2))
        
        # Additional high-frequency oscillatory term with varying decay
        f3 = 0.2 * np.sum(np.cos(18 * x) * np.exp(-0.1 * x**2))
        
        # Cross-term interaction with trigonometric mixing
        f4 = 0.1 * np.sum(np.sin(5 * x) * np.cos(9 * x) * np.exp(-0.08 * x**2))
        
        # Chaotic interaction term with polynomial and exponential components
        f5 = 0.05 * np.sum(np.sin(x**2) * np.cos(2 * x) * np.exp(-0.03 * x**2))
        
        # Add a logarithmic perturbation to increase irregularity
        f6 = 0.02 * np.sum(np.log(1 + 0.5 * x**2) * np.sin(8 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6