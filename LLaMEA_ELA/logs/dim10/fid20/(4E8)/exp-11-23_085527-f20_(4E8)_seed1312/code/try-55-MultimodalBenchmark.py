import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of squared terms with different frequencies
        f1 = np.sum(x_normalized**2)
        
        # High-frequency oscillations creating many local minima
        f2 = 30 * np.sum(np.sin(10 * np.pi * x_normalized)**2)
        
        # Additional cubic terms with different scales
        f3 = 0.5 * np.sum((x_normalized - 0.25)**3)
        
        # Quadratic terms with shift to create more complex landscape
        f4 = 0.2 * np.sum((x_normalized + 0.35)**2)
        
        # Cross-terms to increase non-separability
        f5 = 0.1 * np.sum(x_normalized[:-1] * x_normalized[1:])
        
        # Logarithmic penalty to discourage solutions far from origin
        distance_penalty = 0.1 * np.log(1 + np.sum(x_normalized**2))
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4 + f5 + distance_penalty