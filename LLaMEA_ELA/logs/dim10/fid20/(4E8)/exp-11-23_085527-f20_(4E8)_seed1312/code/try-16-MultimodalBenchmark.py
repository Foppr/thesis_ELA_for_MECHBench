import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for better conditioning
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Sum of sinusoidal terms with higher frequencies to create more local minima
        f2 = 0.2 * np.sum(np.sin(8 * np.pi * x_normalized))
        
        # Additional cubic terms to increase landscape complexity
        f3 = 0.1 * np.sum(x_normalized**3)
        
        # Product term to create complex interactions between dimensions
        f4 = np.prod(np.cos(0.3 * np.pi * x_normalized))
        
        # Combine terms with different weights to control landscape complexity
        return f1 + f2 + f3 + 0.3 * f4