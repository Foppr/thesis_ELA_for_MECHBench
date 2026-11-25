import numpy as np

class SinusoidalBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for consistent scaling
        x_normalized = x / 5.0
        
        # Central attractive basin term
        basin_term = np.sum(x_normalized**2)
        
        # Sinusoidal oscillations in each dimension
        sin_term = np.sum(np.sin(5 * np.pi * x_normalized) * np.exp(-0.5 * x_normalized**2))
        
        # Additional multi-modal component
        modal_term = np.sum(np.sin(3 * np.pi * x_normalized) * np.cos(2 * np.pi * x_normalized))
        
        # Combine terms with different weights
        return 10 * basin_term + sin_term + 0.5 * modal_term