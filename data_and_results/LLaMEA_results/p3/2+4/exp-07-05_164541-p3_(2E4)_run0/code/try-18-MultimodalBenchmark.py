import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay terms with modified coefficients
        exp_term = np.sum(np.exp(-0.3 * x**2) * np.sin(2.5 * np.pi * x))
        
        # Trigonometric oscillations with increased frequency
        trig_term = np.sum(np.sin(4 * np.pi * x) * np.cos(6 * np.pi * x))
        
        # Polynomial interaction terms with cubic and quartic components
        poly_term = np.sum(x**3 - 8 * x**2 + 4 * x)
        
        # Additional coupling terms between dimensions
        coupling_term = np.sum((x[:-1] - x[1:])**2)
        
        # Combine all terms with different weights
        return 0.15 * exp_term + 0.1 * trig_term + 0.02 * poly_term + 0.05 * coupling_term + 1.5