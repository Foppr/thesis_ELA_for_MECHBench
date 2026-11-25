import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay terms to create varying terrain difficulty
        exp_terms = np.sum(np.exp(-0.1 * np.abs(x)) * np.cos(2.0 * x))
        
        # Trigonometric functions creating multiple nested local minima
        trig_terms = np.sum(np.sin(3.0 * x) * np.sin(0.5 * x) + np.cos(4.0 * x) * np.cos(1.0 * x))
        
        # Polynomial with mixed powers to add complexity
        poly_terms = np.sum(x**4 + 0.5 * x**3 - 2.0 * x**2 + 0.1 * x)
        
        # Combine all components with different weights
        result = 0.4 * exp_terms + 0.3 * trig_terms + 0.3 * poly_terms
        
        return result