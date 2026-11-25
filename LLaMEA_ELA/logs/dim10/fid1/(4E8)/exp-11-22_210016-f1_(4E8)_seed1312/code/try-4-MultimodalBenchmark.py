import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms
        poly_term = np.sum(x**2) + 0.1 * np.sum(x**4)
        
        # Sinusoidal oscillations
        sin_term = np.sum(np.sin(5.0 * x))
        
        # Cross-term interaction
        cross_term = np.sum(x[:-1] * x[1:])
        
        # Combine all terms
        result = poly_term + sin_term + 0.5 * cross_term
        
        return result