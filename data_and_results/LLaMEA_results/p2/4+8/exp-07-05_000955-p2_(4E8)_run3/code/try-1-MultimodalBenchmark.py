import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        quadratic = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms to create multiple local minima
        sinusoidal = np.sum(np.sin(5 * np.pi * x_normalized))
        
        # Product term to create interaction between dimensions
        product = np.prod(np.cos(2 * np.pi * x_normalized))
        
        # Combine terms with different weights to create a challenging landscape
        return quadratic + 0.1 * sinusoidal + 0.05 * product