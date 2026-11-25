import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component with multiple frequencies
        sin_term = np.sum(np.sin(2 * np.pi * x_norm) + 0.5 * np.sin(5 * np.pi * x_norm) + 
                         0.3 * np.sin(9 * np.pi * x_norm))
        
        # Polynomial radial component with different powers
        poly_radial = np.sum(x_norm ** 2 + 0.3 * (x_norm ** 4) + 0.1 * (x_norm ** 6))
        
        # Cross-dimensional interaction with exponential decay
        cross_term = 0.2 * np.sum(np.exp(-0.5 * (x_norm[:-1] ** 2 + x_norm[1:] ** 2)) * 
                                (x_norm[:-1] * x_norm[1:]))
        
        # Mixed polynomial-sinusoidal interaction terms
        mixed_term = 0.15 * np.sum((x_norm[:-1] ** 2 + x_norm[1:] ** 2) * 
                                 np.cos(3 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Combined function with different weights
        result = 1.8 * sin_term + 1.2 * poly_radial + 0.8 * cross_term + 0.4 * mixed_term
        
        return result