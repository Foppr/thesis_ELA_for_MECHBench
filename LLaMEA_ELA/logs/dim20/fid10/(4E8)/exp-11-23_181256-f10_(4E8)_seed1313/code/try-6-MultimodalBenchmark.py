import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic_term = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms creating multiple local minima
        sinusoidal_term = np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        # Product term creating complex landscape
        product_term = np.prod(np.cos(np.pi * x_norm))
        
        # Combine terms with different weights
        result = quadratic_term + 0.1 * sinusoidal_term - 0.05 * product_term
        
        return result