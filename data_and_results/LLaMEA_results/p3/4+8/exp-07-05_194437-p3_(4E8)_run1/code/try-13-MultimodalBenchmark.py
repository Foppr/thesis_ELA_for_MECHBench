import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with higher frequency to create more local minima
        f2 = np.sum(np.sin(8 * np.pi * x_norm) ** 2)
        
        # Product term with modified cosine to increase landscape complexity
        f3 = np.prod(np.cos(0.3 * np.pi * x_norm) + 1.2)
        
        # Additional polynomial interaction term
        f4 = np.sum(x_norm**4)
        
        # Combine terms with different weights
        return f1 + 0.15 * f2 + 0.02 * f3 + 0.05 * f4