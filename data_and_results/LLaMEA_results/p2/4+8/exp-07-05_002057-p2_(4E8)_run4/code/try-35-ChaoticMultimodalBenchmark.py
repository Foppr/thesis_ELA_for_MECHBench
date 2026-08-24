import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric chaotic component
        f1 = np.sum(np.sin(x) * np.cos(3 * x) * np.exp(-0.1 * x**2))
        
        # Polynomial chaotic component with high degree
        f2 = 0.5 * np.sum(x**4 - 2 * x**2 + 1)
        
        # Logarithmic barrier term to create complex landscape
        f3 = 0.3 * np.sum(np.log(1 + np.abs(x)) * np.exp(-0.05 * x**2))
        
        # Cross-term interaction with chaotic sine waves
        f4 = 0.2 * np.sum(np.sin(7 * x[:-1]) * np.cos(7 * x[1:]) * (x[:-1]**2 + x[1:]**2))
        
        # Additional chaotic oscillation term
        f5 = 0.1 * np.sum(np.sin(13 * x) * np.cos(11 * x) * np.exp(-0.02 * x**2))
        
        return f1 + f2 + f3 + f4 + f5