import numpy as np

class CosineRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced periodic cosine wave component with higher frequencies and amplitudes
        cosine_term = np.sum(np.cos(5 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                            np.cos(13 * np.pi * x_norm) + 0.6 * np.cos(7 * np.pi * x_norm))
        
        # Modified radial component with quartic and septic terms
        radial_term = np.sum(x_norm ** 4 + 0.2 * (x_norm ** 7))
        
        # Enhanced cross-dimensional coupling with exponential decay
        coupling_term = 0.25 * np.sum(np.exp(-0.3 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
                                    (x_norm[:-1] ** 3 + x_norm[1:] ** 3))
        
        # Additional nonlinear interaction terms with sine modulation
        interaction_term = 0.35 * np.sum(np.sin(3 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                       (x_norm[:-1] ** 4 + x_norm[1:] ** 4))
        
        # Additional quadratic cross-term with cosine modulation
        quadratic_coupling = 0.18 * np.sum(np.cos(4 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                                          (x_norm[:-1] ** 2 + x_norm[1:] ** 2))
        
        # Combined function with different weights
        result = 3.0 * cosine_term + 1.1 * radial_term + 0.8 * coupling_term + 0.5 * interaction_term + 0.4 * quadratic_coupling
        
        return result