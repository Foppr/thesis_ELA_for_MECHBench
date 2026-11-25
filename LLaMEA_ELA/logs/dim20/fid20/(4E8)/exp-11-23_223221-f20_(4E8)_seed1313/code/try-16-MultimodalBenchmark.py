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
        sinusoidal = np.sum(np.sin(5.0 * x)) * np.exp(-0.1 * np.sum(x**2))
        
        # Cross-term interactions
        cross_terms = np.sum(x[:-1] * x[1:]) * 0.5
        
        return polynomial + sinusoidal + cross_terms