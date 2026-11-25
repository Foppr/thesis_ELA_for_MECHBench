import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms
        poly_term = np.sum(x**2)
        
        # Sinusoidal oscillations
        sin_term = np.sum(np.sin(0.5 * x) * np.sin(0.3 * x))
        
        # Cross-term interactions
        cross_term = np.sum(x[:-1] * x[1:])
        
        # Combined function with different weights
        return 0.1 * poly_term + 0.5 * sin_term + 0.05 * cross_term