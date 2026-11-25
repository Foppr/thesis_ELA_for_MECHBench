import numpy as np

class ChaoticSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine wave component with varying frequencies and amplitudes
        chaotic_term = np.sum(np.sin(2 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm) * 
                             np.sin(10 * np.pi * x_norm) + 0.3 * np.sin(7 * np.pi * x_norm))
        
        # Radial component with quadratic and quartic terms
        radial_term = np.sum(x_norm ** 2 + 0.2 * (x_norm ** 4))
        
        # Cross-dimensional coupling with exponential decay
        coupling_term = 0.1 * np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * 
                                   (x_norm[:-1] ** 2 + x_norm[1:] ** 2))
        
        # Nonlinear interaction terms with sinusoidal modulation
        interaction_term = 0.3 * np.sum(np.sin(3 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                                      (x_norm[:-1] ** 2 + x_norm[1:] ** 2))
        
        # Combined function with different weights
        result = 3.0 * chaotic_term + 0.8 * radial_term + 0.5 * coupling_term + 0.4 * interaction_term
        
        return result