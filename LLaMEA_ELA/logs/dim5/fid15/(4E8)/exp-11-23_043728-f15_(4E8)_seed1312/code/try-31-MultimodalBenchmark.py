import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic_term = np.sum(x_norm**2)
        
        # Multiple sinusoidal oscillations creating multiple local minima
        sin_term = np.sum(np.sin(7 * np.pi * x_norm)**2)
        
        # Additional polynomial terms for increased complexity
        poly_term = np.sum(x_norm**4) + 0.15 * np.sum(x_norm**6)
        
        # Coupled interaction terms between variables to create more complex landscape
        interaction_term = np.sum((x_norm[:-1] + x_norm[1:])**2)
        
        # Shifted local minima to increase difficulty
        shifted_term = np.sum(np.sin(3 * np.pi * (x_norm + 0.2))**2)
        
        # Combine all terms with different weights to create a challenging landscape
        return quadratic_term + 0.6 * sin_term + 0.015 * poly_term + 0.3 * interaction_term + 0.4 * shifted_term