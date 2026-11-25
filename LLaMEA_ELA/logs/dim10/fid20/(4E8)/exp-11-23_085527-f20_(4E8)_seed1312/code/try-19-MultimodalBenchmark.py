import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for better conditioning
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms to create multiple local minima
        f2 = 0.1 * np.sum(np.sin(5 * np.pi * x_normalized))
        
        # Product term to create complex interactions between dimensions
        f3 = np.prod(np.cos(0.5 * np.pi * x_normalized))
        
        # Combine terms with different weights to control landscape complexity
        return f1 + f2 + 0.5 * f3