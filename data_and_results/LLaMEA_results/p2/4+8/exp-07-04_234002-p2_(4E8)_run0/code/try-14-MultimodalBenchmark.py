import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with different frequencies
        f2 = np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        # Sum of higher-order polynomial terms for increased complexity
        f3 = np.sum(x_norm**4)
        
        # Product of all dimensions (creates complex landscape)
        f4 = np.prod(x_norm)
        
        # Add a radial component to create more challenging landscape
        radial = np.sum(x_norm**2) ** 0.5
        
        # Combine terms with different weights
        result = 0.3 * f1 + 0.2 * f2 + 0.2 * f3 + 0.2 * f4 + 0.1 * radial
        
        # Ensure global minimum is at origin
        return result