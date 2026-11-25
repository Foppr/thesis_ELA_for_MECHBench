import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of quadratic terms (central quadratic basin)
        quadratic_term = np.sum(x_normalized**2)
        
        # Sum of sinusoidal oscillations creating multiple local minima (increased frequency)
        sinusoidal_term = 0.0
        for i in range(self.dim):
            sinusoidal_term += np.sin(7 * np.pi * x_normalized[i]) ** 2
        
        # Product of all dimensions with quadratic penalty (modified)
        product_term = 1.0
        for i in range(self.dim):
            product_term *= (x_normalized[i] ** 2 + 0.05)
        
        # Additional cubic interaction terms for increased complexity
        cubic_term = 0.0
        for i in range(self.dim):
            cubic_term += x_normalized[i] ** 3
        
        # Combine terms with different weights to create challenging landscape
        return 8 * quadratic_term + 7 * sinusoidal_term + 0.15 * product_term + 0.5 * cubic_term