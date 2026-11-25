import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of squared terms with different scales
        term1 = np.sum(x_norm**2)
        
        # Product of cosines creating multiple local minima
        term2 = np.prod(np.cos(1.0 * x_norm))
        
        # Additional high-frequency sinusoidal component for complexity
        term3 = np.sum(np.sin(0.8 * x_norm) * np.cos(0.6 * x_norm))
        
        # Polynomial interaction terms to increase landscape complexity
        term4 = 0.1 * np.sum(x_norm**4)
        
        # Combine terms with different weights to create challenging landscape
        return term1 + 0.2 * term2 + 0.1 * term3 + 0.05 * term4