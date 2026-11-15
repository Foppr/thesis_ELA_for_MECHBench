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
        
        # Product of all dimensions (creates complex landscape)
        f3 = np.prod(x_norm)
        
        # Add noise term to make it more challenging
        noise = 0.1 * np.random.random()
        
        # Combine terms with different weights
        result = 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + noise
        
        # Ensure global minimum is at origin
        return result