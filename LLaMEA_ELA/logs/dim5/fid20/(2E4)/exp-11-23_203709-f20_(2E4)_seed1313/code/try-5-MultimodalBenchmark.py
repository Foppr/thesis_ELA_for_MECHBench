import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic_term = np.sum(x_norm**2)
        
        # Product of sinusoidal terms creating multiple local minima with higher frequency
        sinusoidal_term = np.prod(np.sin(1.0 * x_norm))
        
        # Additional cubic terms for complexity with modified coefficients
        cubic_term = np.sum(x_norm**3)
        
        # Add a cross-term interaction to increase landscape complexity
        cross_term = np.sum(x_norm[:-1] * x_norm[1:])
        
        # Combine terms with different weights
        result = 0.2 * quadratic_term + 0.6 * sinusoidal_term + 0.02 * cubic_term + 0.1 * cross_term
        
        return result