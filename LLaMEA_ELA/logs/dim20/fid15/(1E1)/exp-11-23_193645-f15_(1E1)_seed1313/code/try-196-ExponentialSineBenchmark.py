import numpy as np

class ExponentialSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine wave modulation with fractal-like frequency variations
        sine_term = np.sum(np.sin(2 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm) * 
                          np.sin(8 * np.pi * x_norm) * np.sin(13 * np.pi * x_norm) + 
                          0.3 * np.sin(4 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm))
        
        # Enhanced exponential decay with chaotic weights and multiple decay rates
        exp_radial_term = np.sum(np.exp(-0.7 * x_norm ** 2) + 
                                0.3 * np.exp(-0.4 * x_norm ** 4) + 
                                0.1 * np.exp(-0.9 * x_norm ** 6) + 
                                0.2 * np.exp(-0.5 * np.abs(x_norm) ** 3))
        
        # Hyper-asymmetric cross-dimensional coupling with chaotic scaling factors
        asym_coupling_term = 0.5 * np.sum(np.exp(-0.6 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
                                         (x_norm[:-1] ** 2 + 0.7 * x_norm[1:] ** 2 + 
                                          0.3 * np.abs(x_norm[:-1]) * np.abs(x_norm[1:])) +
                                         0.2 * np.exp(-0.3 * (x_norm[:-1] + x_norm[1:]) ** 2) * 
                                         (x_norm[:-1] ** 3 + 0.5 * x_norm[1:] ** 3))
        
        # Modified nonlinear interaction terms with chaotic sine modulation and varying amplitudes
        sine_interaction_term = 0.5 * np.sum(np.sin(3.5 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                           (x_norm[:-1] ** 2 + x_norm[1:] ** 2) * 
                                           np.cos(2.0 * np.pi * x_norm[:-1]) * 
                                           np.sin(1.5 * np.pi * x_norm[1:]))
        
        # Additional quadratic cross-term with chaotic coefficients
        quad_cross_term = 0.2 * np.sum((x_norm[:-1] + x_norm[1:]) ** 2 * 
                                     (1 + 0.3 * np.sin(6 * np.pi * x_norm[:-1])) * 
                                     (1 + 0.2 * np.cos(4 * np.pi * x_norm[1:])))
        
        # Fractal-like polynomial interaction with high-order terms
        poly_interaction_term = 0.15 * np.sum((x_norm[:-1] ** 3 + x_norm[1:] ** 3) * 
                                            (x_norm[:-1] ** 2 + x_norm[1:] ** 2))
        
        # Combined function with different weights and hyper-asymmetric scaling
        result = 4.0 * sine_term + 1.1 * exp_radial_term + 0.8 * asym_coupling_term + 0.5 * sine_interaction_term + 0.3 * quad_cross_term + 0.25 * poly_interaction_term
        
        return result