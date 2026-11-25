import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different weights
        quadratic = np.sum(x_norm**2)
        
        # Product of sinusoidal terms to create multiple local minima
        sinusoidal = np.prod(np.sin(5 * np.pi * x_norm))
        
        # Additional cubic term for non-linearity
        cubic = np.sum(x_norm**3)
        
        # Combine terms with different weights to create a challenging landscape
        return 0.1 * quadratic + 0.5 * sinusoidal + 0.01 * cubic + 1.0