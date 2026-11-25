import numpy as np

class SinusoidalBasinFunction:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Central attracting basin with quadratic terms
        basin_term = np.sum(x_norm**2)
        
        # Sinusoidal oscillations in multiple directions
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(2 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
        
        # Additional mixed terms for complexity
        mixed_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mixed_term += x_norm[i] * x_norm[j] * np.sin(np.pi * (x_norm[i] + x_norm[j]))
        
        # Combine all terms with different weights
        result = 0.5 * basin_term + 0.3 * sin_term + 0.2 * mixed_term
        
        # Add a small constant to ensure positive definiteness
        return result + 1.0