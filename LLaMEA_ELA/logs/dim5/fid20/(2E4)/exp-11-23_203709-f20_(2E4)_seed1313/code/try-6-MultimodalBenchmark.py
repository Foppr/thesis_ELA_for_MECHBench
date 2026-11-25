import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponential decay terms that create deep valleys
        exp_term = np.sum(np.exp(-x_scaled**2 / 2.0))
        
        # Trigonometric peaks creating multiple local minima
        trig_term = np.sum(np.cos(3.0 * x_scaled) * np.sin(5.0 * x_scaled))
        
        # Polynomial terms for additional complexity
        poly_term = np.sum(x_scaled**4)
        
        # Combine all terms with different weights
        result = -exp_term + 0.5 * trig_term + 0.01 * poly_term
        
        return result