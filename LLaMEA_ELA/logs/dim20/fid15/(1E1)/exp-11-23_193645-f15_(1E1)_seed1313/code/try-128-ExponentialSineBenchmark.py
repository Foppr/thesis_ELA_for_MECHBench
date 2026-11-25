import numpy as np

class ExponentialSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced sine wave modulation component with higher frequency interactions
        sine_term = np.sum(np.sin(3 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm) * 
                          np.sin(11 * np.pi * x_norm) + 0.4 * np.sin(6 * np.pi * x_norm))
        
        # Enhanced exponential decay radial component with stronger nonlinearity
        exp_radial_term = np.sum(np.exp(-0.3 * x_norm ** 2) + 0.3 * np.exp(-0.5 * x_norm ** 4) + 
                                0.1 * np.exp(-0.7 * x_norm ** 6))
        
        # Stronger asymmetric cross-dimensional coupling with modified weights
        asym_coupling_term = 0.3 * np.sum(np.exp(-0.4 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
                                         (x_norm[:-1] ** 3 + 0.6 * x_norm[1:] ** 3))
        
        # Enhanced nonlinear interaction terms with increased sine modulation
        sine_interaction_term = 0.5 * np.sum(np.sin(4 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                           (x_norm[:-1] ** 3 + x_norm[1:] ** 3))
        
        # Additional quadratic cross-term for increased complexity
        quad_cross_term = 0.2 * np.sum((x_norm[:-1] + x_norm[1:]) ** 2)
        
        # Combined function with adjusted weights and enhanced nonlinearity
        result = 4.0 * sine_term + 1.0 * exp_radial_term + 0.7 * asym_coupling_term + 0.6 * sine_interaction_term + 0.3 * quad_cross_term
        
        return result