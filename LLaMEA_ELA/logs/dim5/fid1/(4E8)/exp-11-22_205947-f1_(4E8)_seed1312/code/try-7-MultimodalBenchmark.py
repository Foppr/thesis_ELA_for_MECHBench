import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Polynomial terms
        poly_term = np.sum(x_norm**2)
        
        # Sinusoidal oscillations creating multiple local minima
        sin_term = np.sum(np.sin(5 * np.pi * x_norm) ** 2)
        
        # Additional complexity with higher frequency oscillations
        high_freq_term = np.sum(np.sin(10 * np.pi * x_norm) ** 4)
        
        # Combine terms with different weights
        result = 0.5 * poly_term + 0.3 * sin_term + 0.2 * high_freq_term
        
        return result