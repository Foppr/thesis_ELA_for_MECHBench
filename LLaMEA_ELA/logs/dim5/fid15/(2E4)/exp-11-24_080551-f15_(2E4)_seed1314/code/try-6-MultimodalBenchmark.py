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
        sinusoidal_term = np.sum(np.sin(3 * np.pi * x_norm)**2)
        
        # Additional high-frequency sinusoidal term for increased complexity
        high_freq_term = np.sum(np.sin(10 * np.pi * x_norm)**2)
        
        # Product term creating correlation between dimensions with different scaling
        product_term = np.prod(np.cos(0.3 * np.pi * x_norm))
        
        # Additional coupling term between dimensions to increase interdependency
        coupling_term = np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Combine terms with different weights to create challenging landscape
        return quadratic_term + 0.15 * sinusoidal_term + 0.08 * high_freq_term - 0.07 * product_term + 0.05 * coupling_term