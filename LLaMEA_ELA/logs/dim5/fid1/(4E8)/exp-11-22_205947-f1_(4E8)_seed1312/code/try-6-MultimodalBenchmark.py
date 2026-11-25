import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of squares term
        sum_sq = np.sum(x_norm**2)
        
        # Multiple sinusoidal terms creating multiple local minima
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(10 * np.pi * x_norm[i]) * np.exp(-0.5 * (x_norm[i] - 0.5)**2)
        
        # Additional quadratic term with multiple minima
        quad_term = 0.0
        for i in range(self.dim):
            quad_term += (x_norm[i] - 0.3)**2 * (1 + np.sin(5 * np.pi * x_norm[i])**2)
            
        # Combine terms with different weights
        result = sum_sq + 0.5 * sin_term + 0.3 * quad_term
        
        return result