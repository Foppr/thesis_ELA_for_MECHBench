import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        quadratic = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms to create multiple local minima
        sinusoidal = np.sum(np.sin(5 * np.pi * x_norm))
        
        # Product term to create interaction between dimensions
        product = np.prod(np.cos(0.5 * np.pi * x_norm))
        
        # Combine terms with different weights
        return 0.1 * quadratic + 0.3 * sinusoidal + 0.6 * product + 1.0