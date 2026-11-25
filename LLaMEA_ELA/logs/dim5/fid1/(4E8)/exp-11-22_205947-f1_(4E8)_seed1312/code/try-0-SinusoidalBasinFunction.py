import numpy as np

class SinusoidalBasinFunction:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for consistent scaling
        x_normalized = x / 5.0
        
        # Central attractive basin term
        basin_term = -np.exp(-np.sum(x_normalized**2) / (2 * 0.5**2))
        
        # Sinusoidal oscillation terms
        sin_term = np.sum(np.sin(5 * np.pi * x_normalized) ** 2)
        
        # Additional quadratic penalty for staying away from center
        penalty = 0.1 * np.sum(x_normalized**2)
        
        return basin_term + sin_term + penalty