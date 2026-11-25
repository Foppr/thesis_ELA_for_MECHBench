import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic_sum = np.sum(x_normalized**2)
        
        # Product of sinusoidal terms with shifted frequencies to create multiple local minima
        sinusoidal_product = np.prod(np.sin(0.7 * np.pi * x_normalized + 0.2 * np.pi))
        
        # Additional harmonic terms with different frequencies for increased complexity
        harmonic_sum = np.sum(np.sin(2.5 * np.pi * x_normalized**2) + 0.5 * np.sin(4.0 * np.pi * x_normalized))
        
        # Combine all components with different weights
        result = quadratic_sum + 0.15 * sinusoidal_product + 0.08 * harmonic_sum
        
        return result