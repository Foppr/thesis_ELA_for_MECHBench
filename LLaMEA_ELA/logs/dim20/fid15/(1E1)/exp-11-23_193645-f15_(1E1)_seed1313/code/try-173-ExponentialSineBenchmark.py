import numpy as np

class ExponentialSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sine wave modulation component with varying frequencies
        sine_term = np.sum(np.sin(2 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm) * 
                          np.sin(8 * np.pi * x_norm) + 0.3 * np.sin(4 * np.pi * x_norm))
        
        # Enhanced exponential decay radial component with asymmetric weights
        exp_radial_term = np.sum(np.exp(-0.7 * x_norm ** 2) + 0.3 * np.exp(-0.4 * x_norm ** 4))
        
        # Stronger asymmetric cross-dimensional coupling with exponential decay
        asym_coupling_term = 0.3 * np.sum(np.exp(-0.6 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
                                         (x_norm[:-1] ** 2 + 0.7 * x_norm[1:] ** 2))
        
        # Modified nonlinear interaction terms with sine modulation and varying amplitudes
        sine_interaction_term = 0.4 * np.sum(np.sin(3.5 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                           (x_norm[:-1] ** 2 + x_norm[1:] ** 2))
        
        # Additional quadratic cross-term for increased complexity
        quad_cross_term = 0.1 * np.sum((x_norm[:-1] + x_norm[1:]) ** 2)
        
        # Combined function with different weights and asymmetric scaling
        result = 3.5 * sine_term + 0.9 * exp_radial_term + 0.6 * asym_coupling_term + 0.45 * sine_interaction_term + 0.2 * quad_cross_term
        
        return result