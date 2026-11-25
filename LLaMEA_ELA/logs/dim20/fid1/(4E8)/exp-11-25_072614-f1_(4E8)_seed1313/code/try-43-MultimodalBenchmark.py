import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms
        polynomial = np.sum(x**2) + 0.15 * np.sum(x**4) + 0.02 * np.sum(x**6) + 0.005 * np.sum(x**8)
        
        # Sinusoidal oscillations to create multiple local minima
        sinusoidal = np.sum(np.sin(6.0 * x)) + 0.6 * np.sum(np.sin(12.0 * x)) + 0.15 * np.sum(np.sin(18.0 * x))
        
        # Exponential perturbations to increase landscape complexity
        exponential = np.sum(np.exp(-0.4 * x**2)) + 0.4 * np.sum(np.exp(-x**2))
        
        # Cross-terms to add interactions between dimensions
        cross_terms = 0.1 * np.sum(x[:-1] * x[1:]) + 0.05 * np.sum(x**3)
        
        # Combined function with global minimum at origin
        return polynomial + sinusoidal + exponential + cross_terms