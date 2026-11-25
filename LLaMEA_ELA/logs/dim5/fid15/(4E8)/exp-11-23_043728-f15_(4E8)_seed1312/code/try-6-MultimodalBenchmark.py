import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        quadratic_term = np.sum(x_norm**2)
        
        # Multiple local minima created by sinusoidal modulation
        sinusoidal_term = np.sum(np.sin(5 * np.pi * x_norm) ** 2)
        
        # Additional quartic term for increased complexity
        quartic_term = np.sum(x_norm**4)
        
        # Combine terms with different weights
        result = quadratic_term + 0.1 * sinusoidal_term + 0.01 * quartic_term
        
        return result