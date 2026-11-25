import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4)
        
        # Sinusoidal oscillations
        sinusoidal = np.sum(np.sin(5.0 * x))
        
        # Cross-term interactions
        cross_terms = 0.5 * np.sum(x[:-1] * x[1:])
        
        # Combined function value
        return polynomial + sinusoidal + cross_terms