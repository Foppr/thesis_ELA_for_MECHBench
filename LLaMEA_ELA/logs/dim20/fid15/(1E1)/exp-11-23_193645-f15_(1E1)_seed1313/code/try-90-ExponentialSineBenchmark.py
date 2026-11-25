import numpy as np

class ExponentialSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Multiple sine wave modulation components with varying frequencies and amplitudes
        sine_term = np.sum(0.5 * np.sin(2 * np.pi * x_norm) + 
                          0.3 * np.sin(5 * np.pi * x_norm) + 
                          0.2 * np.sin(8 * np.pi * x_norm) + 
                          0.4 * np.sin(12 * np.pi * x_norm) + 
                          0.1 * np.sin(15 * np.pi * x_norm))
        
        # Enhanced exponential decay radial component with multiple decay rates
        exp_radial_term = np.sum(0.8 * np.exp(-0.5 * x_norm ** 2) + 
                               0.3 * np.exp(-0.3 * x_norm ** 4) + 
                               0.2 * np.exp(-0.1 * x_norm ** 6) + 
                               0.1 * np.exp(-0.7 * x_norm ** 3))
        
        # Asymmetric cross-dimensional coupling with multiple interaction types
        asym_coupling_term = 0.3 * np.sum(np.exp(-0.5 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
                                         (x_norm[:-1] ** 2 + 0.5 * x_norm[1:] ** 2)) + \
                           0.2 * np.sum(np.exp(-0.3 * (x_norm[:-1] + x_norm[1:]) ** 2) * 
                                       (x_norm[:-1] ** 3 + 0.3 * x_norm[1:] ** 3))
        
        # Nonlinear interaction terms with sine modulation and varying amplitudes
        sine_interaction_term = 0.4 * np.sum(np.sin(3 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                           (x_norm[:-1] ** 2 + x_norm[1:] ** 2)) + \
                              0.2 * np.sum(np.cos(2 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                                         (x_norm[:-1] ** 3 + x_norm[1:] ** 3))
        
        # Additional polynomial interaction terms
        poly_interaction_term = 0.1 * np.sum(x_norm[:-1] ** 4 + x_norm[1:] ** 4) + \
                              0.15 * np.sum(x_norm[:-1] ** 2 * x_norm[1:] ** 2)
        
        # Gaussian interaction terms for increased landscape complexity
        gaussian_term = 0.25 * np.sum(np.exp(-0.5 * (x_norm[:-1] - x_norm[1:]) ** 4) + 
                                    0.3 * np.exp(-0.2 * (x_norm[:-1] + x_norm[1:]) ** 4))
        
        # Combined function with different weights and asymmetric scaling
        result = 2.5 * sine_term + 0.9 * exp_radial_term + 0.6 * asym_coupling_term + \
                 0.5 * sine_interaction_term + 0.3 * poly_interaction_term + 0.4 * gaussian_term
        
        return result