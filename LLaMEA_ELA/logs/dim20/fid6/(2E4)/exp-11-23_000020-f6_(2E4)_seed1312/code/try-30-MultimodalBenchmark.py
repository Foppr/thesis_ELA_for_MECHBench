import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with multiple local minima
        f2 = np.sum(np.sin(9 * np.pi * x_norm)**2)
        
        # Product term creating complex landscape
        f3 = np.prod(np.cos(0.5 * np.pi * x_norm) + 0.3)
        
        # Additional polynomial interaction term with cubic power
        f4 = np.sum(x_norm**3)
        
        # Shifted global minimum term
        f5 = np.sum((x_norm + 0.2)**2)
        
        # Additional quartic polynomial term for increased complexity
        f6 = np.sum(x_norm**4)
        
        # Combined with different weights to create a more challenging landscape
        return 0.15 * f1 + 0.25 * f2 + 0.3 * f3 + 0.1 * f4 + 0.1 * f5 + 0.05 * f6 + 1.5