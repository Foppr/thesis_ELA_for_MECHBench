import numpy as np

class SinusoidalBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for consistent scaling
        x_normalized = x / 5.0
        
        # Central quadratic basin term
        basin_term = np.sum(x_normalized**2)
        
        # Stronger sinusoidal oscillations with exponential decay
        sin_term = np.sum(np.sin(10 * np.pi * x_normalized) * np.exp(-0.1 * np.abs(x_normalized)))
        
        # Additional high-frequency multi-modal component
        modal_term = np.sum(np.sin(15 * np.pi * x_normalized) * np.cos(8 * np.pi * x_normalized) * np.exp(-0.5 * x_normalized**2))
        
        # Cross-term interaction between dimensions
        cross_term = np.sum(x_normalized[:-1] * x_normalized[1:] * np.sin(7 * np.pi * (x_normalized[:-1] + x_normalized[1:])))
        
        # Combine all terms with different weights
        return 5 * basin_term + sin_term + 0.3 * modal_term + 0.1 * cross_term