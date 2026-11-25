import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic_term = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms with multiple frequencies
        sinusoidal_term = np.sum(np.sin(5 * np.pi * x_normalized)**2)
        
        # Product of all dimensions (creates correlation between variables)
        product_term = np.prod(x_normalized)
        
        # Combine terms with different weights to create a challenging landscape
        return quadratic_term + 0.1 * sinusoidal_term + 0.01 * product_term