import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic_term = np.sum(x_normalized**2)
        
        # Multiple local minima created by sinusoidal modulations
        sinusoidal_term = np.sum(np.sin(5 * np.pi * x_normalized)**2)
        
        # Additional high-frequency oscillations for increased complexity
        high_freq_term = np.sum(np.sin(10 * np.pi * x_normalized) * np.cos(10 * np.pi * x_normalized))
        
        # Combine terms with different weights to create a challenging landscape
        return quadratic_term + 0.1 * sinusoidal_term + 0.05 * high_freq_term