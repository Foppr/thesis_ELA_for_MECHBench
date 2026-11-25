import numpy as np

class CosineRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Periodic cosine wave component with varying frequencies and amplitudes
        cosine_term = np.sum(np.cos(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * 
                            np.cos(11 * np.pi * x_norm) + 0.4 * np.cos(5 * np.pi * x_norm))
        
        # Radial component with cubic and quintic terms
        radial_term = np.sum(x_norm ** 3 + 0.15 * (x_norm ** 5))
        
        # Cross-dimensional coupling with Gaussian decay
        coupling_term = 0.15 * np.sum(np.exp(-0.5 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
                                    (x_norm[:-1] ** 2 + x_norm[1:] ** 2))
        
        # Nonlinear interaction terms with cosine modulation
        interaction_term = 0.25 * np.sum(np.cos(2 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                       (x_norm[:-1] ** 3 + x_norm[1:] ** 3))
        
        # Combined function with different weights
        result = 2.5 * cosine_term + 0.9 * radial_term + 0.6 * coupling_term + 0.35 * interaction_term
        
        return result