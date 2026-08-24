import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay terms
        exp_term = np.sum(np.exp(-0.5 * x**2) * np.sin(2 * np.pi * x))
        
        # Trigonometric oscillations
        trig_term = np.sum(np.sin(3 * np.pi * x) * np.cos(5 * np.pi * x))
        
        # Polynomial interaction terms
        poly_term = np.sum(x**4 - 10 * x**2 + 5 * x)
        
        # Combine all terms with different weights
        return 0.1 * exp_term + 0.05 * trig_term + 0.01 * poly_term + 2.0