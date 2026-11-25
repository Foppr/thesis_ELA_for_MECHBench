import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4)
        
        # Sinusoidal oscillations to create multiple local minima
        sinusoidal = np.sum(np.sin(6.0 * x)) + 0.5 * np.sum(np.sin(2.5 * x)**2)
        
        # Additional challenge with asymmetric cross-terms and higher-order interactions
        cross_terms = 0.1 * np.sum(x[:-2] * x[2:]**2) + 0.05 * np.sum((x[:-1] + x[1:])**3) + 0.02 * np.sum(x**5)
        
        return polynomial + sinusoidal + cross_terms