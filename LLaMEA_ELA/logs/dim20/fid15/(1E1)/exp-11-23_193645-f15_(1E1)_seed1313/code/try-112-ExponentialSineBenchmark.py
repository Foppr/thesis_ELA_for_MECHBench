import numpy as np

class ExponentialSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced sine wave modulation with multiple frequencies and amplitudes
        sine_term = np.sum(
            0.5 * np.sin(2 * np.pi * x_norm) + 
            0.3 * np.sin(5 * np.pi * x_norm) + 
            0.2 * np.sin(8 * np.pi * x_norm) + 
            0.4 * np.sin(10 * np.pi * x_norm) + 
            0.1 * np.sin(15 * np.pi * x_norm)
        )
        
        # Enhanced exponential decay radial component with multiple terms and asymmetric weights
        exp_radial_term = np.sum(
            np.exp(-0.5 * x_norm ** 2) + 
            0.3 * np.exp(-0.3 * x_norm ** 4) + 
            0.2 * np.exp(-0.1 * x_norm ** 6) + 
            0.1 * np.exp(-0.7 * x_norm ** 3)
        )
        
        # Enhanced asymmetric cross-dimensional coupling with multiple interaction terms
        asym_coupling_term = 0.3 * np.sum(
            np.exp(-0.5 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
            (x_norm[:-1] ** 2 + 0.5 * x_norm[1:] ** 2) +
            0.5 * np.exp(-0.3 * (x_norm[:-1] + x_norm[1:]) ** 2) * 
            (x_norm[:-1] ** 3 + 0.3 * x_norm[1:] ** 3)
        )
        
        # Additional nonlinear interaction terms with polynomial and Gaussian components
        poly_interaction_term = 0.2 * np.sum(
            (x_norm[:-1] - x_norm[1:]) ** 4 + 
            0.5 * (x_norm[:-1] + x_norm[1:]) ** 2
        )
        
        gaussian_interaction_term = 0.1 * np.sum(
            np.exp(-0.5 * (x_norm[:-1] - x_norm[1:]) ** 4) + 
            0.3 * np.exp(-0.2 * (x_norm[:-1] + x_norm[1:]) ** 6)
        )
        
        # Combined function with increased complexity and varied weights
        result = 2.5 * sine_term + 1.0 * exp_radial_term + 0.7 * asym_coupling_term + 0.3 * poly_interaction_term + 0.2 * gaussian_interaction_term
        
        return result