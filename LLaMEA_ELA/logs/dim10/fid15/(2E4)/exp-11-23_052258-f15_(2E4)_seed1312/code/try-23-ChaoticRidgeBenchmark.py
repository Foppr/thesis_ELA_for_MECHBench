import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential growth terms to create steep ascents
        f1 = np.sum(np.exp(0.3 * x**2))
        
        # Trigonometric coupling between dimensions for complex interactions
        f2 = 0.4 * np.sum(np.sin(x[:-1] + x[1:]) + np.cos(x[:-1] - x[1:]))
        
        # Asymmetric ridge structure with varying weights
        f3 = 0.25 * np.sum((x[:-1] - x[1:]) ** 4 + (x[:-1] + x[1:]) ** 2)
        
        # Chaotic component using a logistic map-like formulation
        f4 = 0.15 * np.sum(np.sin(8.0 * np.abs(x)) * np.cos(3.0 * x) * np.exp(-0.1 * x**2))
        
        # Additional higher-order polynomial terms for increased complexity
        f5 = 0.1 * np.sum(x**6)
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5