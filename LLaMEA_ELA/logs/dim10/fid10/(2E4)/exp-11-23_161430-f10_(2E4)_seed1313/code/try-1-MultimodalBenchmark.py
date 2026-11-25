import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic_sum = np.sum(x_normalized**2)
        
        # Multiple sinusoidal components creating multiple local minima
        sin_sum = np.sum(np.sin(5 * np.pi * x_normalized)**2)
        
        # Add a cubic term for additional complexity
        cubic_term = np.sum(x_normalized**3)
        
        # Combine all terms with different weights
        result = quadratic_sum + 0.1 * sin_sum + 0.01 * cubic_term
        
        return result