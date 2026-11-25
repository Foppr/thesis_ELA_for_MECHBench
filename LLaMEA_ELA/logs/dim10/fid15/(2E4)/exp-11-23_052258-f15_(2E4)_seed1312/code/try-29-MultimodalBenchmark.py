import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x**2)
        
        # High-frequency sinusoidal terms to increase local optima
        f2 = 0.5 * np.sum(np.sin(20.0 * x))
        
        # Additional polynomial terms for complexity
        f3 = 0.1 * np.sum((x - 1.0)**6)
        
        # Higher-order interaction terms between dimensions
        f4 = 0.2 * np.sum(x[:-2] * x[1:-1] * x[2:])
        
        # Mixed polynomial and sinusoidal interaction
        f5 = 0.12 * np.sum((x[:-1] + np.sin(5.0 * x[:-1])) * x[1:])
        
        # Add a quartic term with shifted origin
        f6 = 0.05 * np.sum((x - 2.0)**4)
        
        # Additional chaotic sine coupling terms
        f7 = 0.15 * np.sum(np.sin(7.0 * x) * np.cos(3.0 * x))
        
        # Cross-dimensional exponential interactions
        f8 = 0.08 * np.sum(np.exp(-x[:-1]**2) * x[1:]**2)
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8