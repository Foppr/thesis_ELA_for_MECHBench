import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different weights
        quadratic_term = np.sum(x_normalized**2)
        
        # Sum of sine terms with higher frequency to create more local minima
        sine_term = np.sum(np.sin(7 * np.pi * x_normalized))
        
        # Product term with different frequency to create complex interaction between dimensions
        product_term = np.prod(np.cos(0.3 * np.pi * x_normalized))
        
        # Additional cosine term to increase landscape complexity
        cosine_term = np.sum(np.cos(3 * np.pi * x_normalized**2))
        
        # Combine all terms with different weights
        result = 0.15 * quadratic_term - 0.6 * sine_term + 0.25 * product_term - 0.1 * cosine_term
        
        return result