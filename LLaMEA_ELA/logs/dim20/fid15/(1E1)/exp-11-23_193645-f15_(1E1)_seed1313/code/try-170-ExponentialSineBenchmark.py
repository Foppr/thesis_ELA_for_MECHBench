import numpy as np

class ExponentialSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sine wave modulation component with varying frequencies and amplitudes
        sine_term = np.sum(0.5 * np.sin(2 * np.pi * x_norm) + 0.3 * np.sin(5 * np.pi * x_norm) + 
                          0.2 * np.sin(8 * np.pi * x_norm) + 0.1 * np.sin(12 * np.pi * x_norm))
        
        # Enhanced exponential decay radial component with asymmetric weights and higher order terms
        exp_radial_term = np.sum(0.7 * np.exp(-0.5 * x_norm ** 2) + 0.2 * np.exp(-0.3 * x_norm ** 4) + 
                               0.1 * np.exp(-0.2 * x_norm ** 6))
        
        # Stronger asymmetric cross-dimensional coupling with exponential decay and additional interaction
        asym_coupling_term = 0.4 * np.sum(np.exp(-0.5 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
                                         (x_norm[:-1] ** 2 + 0.6 * x_norm[1:] ** 2) + 
                                         0.2 * np.exp(-0.3 * (x_norm[:-1] + x_norm[1:]) ** 2) * 
                                         (x_norm[:-1] ** 3 + 0.4 * x_norm[1:] ** 3))
        
        # Modified nonlinear interaction terms with sine modulation, varying amplitudes and additional coupling
        sine_interaction_term = 0.5 * np.sum(np.sin(4 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                           (x_norm[:-1] ** 2 + x_norm[1:] ** 2) + 
                                           0.3 * np.sin(6 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                                           (x_norm[:-1] ** 3 + x_norm[1:] ** 3))
        
        # Additional quadratic cross-term with asymmetric scaling for increased complexity
        quad_cross_term = 0.2 * np.sum((x_norm[:-1] + 0.7 * x_norm[1:]) ** 2 + 
                                     0.1 * (x_norm[:-1] - 0.5 * x_norm[1:]) ** 4)
        
        # Additional cubic term for increased nonlinearity
        cubic_term = 0.1 * np.sum(x_norm ** 3)
        
        # Combined function with different weights and asymmetric scaling
        result = 4.0 * sine_term + 1.2 * exp_radial_term + 0.7 * asym_coupling_term + 0.5 * sine_interaction_term + 0.3 * quad_cross_term + 0.15 * cubic_term
        
        return result