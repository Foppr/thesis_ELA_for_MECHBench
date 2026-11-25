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
        poly_term = np.sum(x_norm**4) + 0.1 * np.sum(x_norm**6)
        
        # Add interaction terms between dimensions to increase landscape complexity
        interaction_term = 0.05 * np.sum((x_norm[:-1] + x_norm[1:])**2)
        
        # Combine all terms with different weights to create a challenging landscape
        return quadratic_term + 0.7 * sin_term + 0.01 * poly_term + interaction_term