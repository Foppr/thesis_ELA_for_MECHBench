import numpy as np

class ExponentialSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Multiple sine wave modulation components with varying frequencies and amplitudes
        sine_term_1 = np.sum(np.sin(2 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm) * 
                           np.sin(8 * np.pi * x_norm) + 0.3 * np.sin(4 * np.pi * x_norm))
        
        sine_term_2 = np.sum(np.cos(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * 
                           np.cos(10 * np.pi * x_norm) + 0.2 * np.cos(6 * np.pi * x_norm))
        
        # Enhanced exponential decay radial component with multiple decay rates
        exp_radial_term = np.sum(np.exp(-0.5 * x_norm ** 2) + 
                                0.2 * np.exp(-0.3 * x_norm ** 4) + 
                                0.1 * np.exp(-0.7 * x_norm ** 6))
        
        # Asymmetric cross-dimensional coupling with higher-order interactions
        asym_coupling_term = 0.2 * np.sum(np.exp(-0.5 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
                                         (x_norm[:-1] ** 2 + 0.5 * x_norm[1:] ** 2) + 
                                         0.3 * np.exp(-0.2 * (x_norm[:-2] - x_norm[2:]) ** 2) * 
                                         (x_norm[:-2] ** 3 + 0.3 * x_norm[2:] ** 3))
        
        # Nonlinear interaction terms with sine modulation and varying amplitudes
        sine_interaction_term = 0.3 * np.sum(np.sin(3 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                           (x_norm[:-1] ** 2 + x_norm[1:] ** 2) + 
                                           0.2 * np.sin(5 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                           (x_norm[:-1] ** 3 + x_norm[1:] ** 3))
        
        # Additional quadratic and cubic correlation terms for increased complexity
        quad_term = 0.1 * np.sum(x_norm[:-1] ** 2 * x_norm[1:] ** 2)
        cubic_term = 0.05 * np.sum(x_norm[:-1] ** 3 * x_norm[1:] ** 3)
        
        # Combined function with different weights and asymmetric scaling
        result = 3.0 * sine_term_1 + 0.8 * sine_term_2 + 0.8 * exp_radial_term + 0.5 * asym_coupling_term + \
                0.4 * sine_interaction_term + 0.2 * quad_term + 0.1 * cubic_term
        
        return result