import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different weights
        quadratic_term = np.sum(x_normalized**2)
        
        # Sum of sine terms to create multiple local minima
        sine_term = np.sum(np.sin(5 * np.pi * x_normalized))
        
        # Product term to create complex interaction between dimensions
        product_term = np.prod(np.cos(0.5 * np.pi * x_normalized))
        
        # Combine all terms with different weights
        result = 0.1 * quadratic_term - 0.5 * sine_term + 0.3 * product_term
        
        return result