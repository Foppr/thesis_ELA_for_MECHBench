import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic_term = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms creating multiple local minima
        sinusoidal_term = np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        # Product term creating correlation between dimensions
        product_term = np.prod(np.cos(0.5 * np.pi * x_norm))
        
        # Combine terms with different weights to create challenging landscape
        return quadratic_term + 0.1 * sinusoidal_term - 0.05 * product_term