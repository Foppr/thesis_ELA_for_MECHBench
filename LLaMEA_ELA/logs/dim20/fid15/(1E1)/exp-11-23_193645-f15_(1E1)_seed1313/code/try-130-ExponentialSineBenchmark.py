import numpy as np

class ExponentialSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Multi-frequency sine wave modulation with varying amplitudes and phases
        sine_term = np.sum(
            0.5 * np.sin(2 * np.pi * x_norm) * 
            np.sin(5 * np.pi * x_norm) * 
            np.sin(8 * np.pi * x_norm) + 
            0.3 * np.sin(4 * np.pi * x_norm) +
            0.2 * np.sin(7 * np.pi * x_norm) *
            np.cos(3 * np.pi * x_norm) +
            0.1 * np.sin(10 * np.pi * x_norm)
        )
        
        # Enhanced exponential decay radial component with higher-order terms
        exp_radial_term = np.sum(
            np.exp(-0.5 * x_norm ** 2) + 
            0.2 * np.exp(-0.3 * x_norm ** 4) +
            0.1 * np.exp(-0.1 * x_norm ** 6) +
            0.05 * np.exp(-0.05 * x_norm ** 8)
        )
        
        # Asymmetric cross-dimensional coupling with polynomial interactions
        asym_coupling_term = 0.2 * np.sum(
            np.exp(-0.5 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
            (x_norm[:-1] ** 2 + 0.5 * x_norm[1:] ** 2) +
            0.1 * (x_norm[:-1] ** 3 + x_norm[1:] ** 3)
        )
        
        # Nonlinear interaction terms with sine modulation and varying amplitudes
        sine_interaction_term = 0.3 * np.sum(
            np.sin(3 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
            (x_norm[:-1] ** 2 + x_norm[1:] ** 2) +
            0.2 * np.cos(2 * np.pi * (x_norm[:-1] + x_norm[1:])) *
            (x_norm[:-1] ** 3 + x_norm[1:] ** 3)
        )
        
        # Additional higher-order polynomial terms for increased complexity
        poly_term = 0.1 * np.sum(x_norm ** 4 + 0.5 * x_norm ** 6 + 0.05 * x_norm ** 8)
        
        # Combined function with different weights and asymmetric scaling
        result = 3.0 * sine_term + 0.8 * exp_radial_term + 0.5 * asym_coupling_term + 0.4 * sine_interaction_term + 0.2 * poly_term
        
        return result