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
            sin_term += np.sin(12 * np.pi * x_norm[i]) * np.exp(-0.5 * (x_norm[i] - 0.4)**2)
        
        # Additional quadratic term with multiple minima
        quad_term = 0.0
        for i in range(self.dim):
            quad_term += (x_norm[i] - 0.2)**2 * (1 + np.sin(6 * np.pi * x_norm[i])**2)
            
        # Cross-dimensional interaction terms
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += 0.1 * np.sin(8 * np.pi * x_norm[i]) * np.cos(4 * np.pi * x_norm[j])
        
        # Combine terms with different weights
        result = sum_sq + 0.6 * sin_term + 0.25 * quad_term + 0.1 * interaction_term
        
        return result