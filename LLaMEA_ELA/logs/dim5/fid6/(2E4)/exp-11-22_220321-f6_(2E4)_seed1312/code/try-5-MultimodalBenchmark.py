import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial term for conditioning
        poly_term = np.sum(x_scaled**4)
        
        # Exponential decay terms with different frequencies
        exp_term = np.sum(np.exp(-2 * np.pi * np.abs(x_scaled)) * np.cos(3 * np.pi * x_scaled))
        
        # Periodic modulation creating multiple local minima
        periodic_term = np.sum(np.sin(7 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled))
        
        # Combined function with different weights
        return 0.5 * poly_term + 0.3 * exp_term + 0.2 * periodic_term + 0.01 * np.sum(x_scaled**6)