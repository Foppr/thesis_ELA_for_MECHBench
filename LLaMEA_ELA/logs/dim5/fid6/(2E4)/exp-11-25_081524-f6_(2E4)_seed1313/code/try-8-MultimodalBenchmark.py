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
        sinusoidal = np.sum(np.sin(5.0 * x)) + 0.5 * np.sum(np.sin(3.0 * x)**2)
        
        # Additional challenge with cross-terms (modified interaction)
        cross_terms = 0.2 * np.sum(x[:-1] * x[1:]**2)
        
        # Increased nonlinearity with higher order terms
        nonlinear = 0.05 * np.sum(x**6) + 0.3 * np.sum(np.sin(7.0 * x))
        
        return polynomial + sinusoidal + cross_terms + nonlinear