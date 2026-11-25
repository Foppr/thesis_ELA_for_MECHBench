import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms
        poly_term = np.sum(x**4)
        
        # Sinusoidal oscillations with different frequencies
        sin_term = np.sum(np.sin(0.7 * x) * np.cos(0.4 * x))
        
        # Cross-term interactions with quadratic scaling
        cross_term = np.sum((x[:-1] ** 2) * (x[1:] ** 2))
        
        # Combined function with different weights
        return 0.2 * poly_term + 0.6 * sin_term + 0.1 * cross_term