import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Exponential decay terms with different rates
        f2 = np.sum(np.exp(-0.5 * x**2) - 1.0)
        
        # High-frequency trigonometric perturbations
        f3 = 0.5 * np.sum(np.sin(10.0 * x) * np.cos(15.0 * x))
        
        # Additional quartic term for increased curvature
        f4 = 0.01 * np.sum(x**4)
        
        # Mixed polynomial and exponential interaction terms
        f5 = 0.005 * np.sum(np.exp(-x**2) * x**3)
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5