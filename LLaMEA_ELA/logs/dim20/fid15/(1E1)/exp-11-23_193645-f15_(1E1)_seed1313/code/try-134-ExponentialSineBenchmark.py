import numpy as np

class ExponentialSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Cosine wave modulation component with varying frequencies
        cosine_term = np.sum(np.cos(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * 
                            np.cos(11 * np.pi * x_norm) + 0.4 * np.cos(5 * np.pi * x_norm))
        
        # Polynomial decay radial component with asymmetric weights
        poly_radial_term = np.sum(x_norm ** 4 + 0.3 * x_norm ** 6)
        
        # Asymmetric cross-dimensional coupling with polynomial decay
        asym_coupling_term = 0.3 * np.sum((x_norm[:-1] - x_norm[1:]) ** 4 + 0.5 * (x_norm[:-1] ** 2 + 0.3 * x_norm[1:] ** 2))
        
        # Nonlinear interaction terms with cosine modulation and varying amplitudes
        cosine_interaction_term = 0.4 * np.sum(np.cos(2 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                                             (x_norm[:-1] ** 3 + x_norm[1:] ** 3))
        
        # Combined function with different weights and asymmetric scaling
        result = 2.5 * cosine_term + 0.9 * poly_radial_term + 0.6 * asym_coupling_term + 0.3 * cosine_interaction_term
        
        return result