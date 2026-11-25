import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of squared terms with different weights
        sum_sq = np.sum(x_normalized**2)
        
        # Multiple local minima created by sinusoidal modulation
        sinusoidal_term = np.sum(np.sin(5 * np.pi * x_normalized)**2)
        
        # Add a global minimum at origin with additional penalty terms
        return sum_sq + 0.1 * sinusoidal_term + 0.01 * np.sum(x_normalized**4)