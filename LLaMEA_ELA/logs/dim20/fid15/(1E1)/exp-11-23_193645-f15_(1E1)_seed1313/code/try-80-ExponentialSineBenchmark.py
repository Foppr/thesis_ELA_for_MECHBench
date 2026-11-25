import numpy as np

class ExponentialSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial interaction terms with varying degrees
        poly_term = np.sum(x_norm ** 4 + 0.5 * x_norm ** 3 + 0.2 * x_norm ** 2 + 0.1 * x_norm)
        
        # Radial basis function component with multiple centers
        rbf_term = np.sum(np.exp(-0.5 * (x_norm - 0.3) ** 2) + 
                         0.5 * np.exp(-0.3 * (x_norm + 0.4) ** 2) + 
                         0.3 * np.exp(-0.7 * (x_norm - 0.1) ** 2))
        
        # Asymmetric cross-dimensional coupling with polynomial weights
        asym_coupling_term = 0.3 * np.sum((x_norm[:-1] ** 3 + 0.5 * x_norm[1:] ** 3) * 
                                         np.exp(-0.5 * (x_norm[:-1] - x_norm[1:]) ** 2))
        
        # Sine wave modulation with varying frequencies and amplitudes
        sine_modulation = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) + 
                               0.4 * np.sin(5 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Mixed polynomial and exponential interaction terms
        mixed_term = 0.2 * np.sum((x_norm[:-1] ** 2 + x_norm[1:] ** 2) * 
                                np.exp(-0.3 * (x_norm[:-1] - x_norm[1:]) ** 2))
        
        # Combined function with different weights and asymmetric scaling
        result = 2.5 * poly_term + 0.7 * rbf_term + 0.6 * asym_coupling_term + 0.5 * sine_modulation + 0.3 * mixed_term
        
        return result