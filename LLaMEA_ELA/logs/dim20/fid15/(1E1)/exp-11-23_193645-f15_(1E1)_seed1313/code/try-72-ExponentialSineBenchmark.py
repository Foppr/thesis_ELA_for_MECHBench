import numpy as np

class ExponentialSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced sine wave modulation component with multiple frequencies
        sine_term = np.sum(
            np.sin(2 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm) * 
            np.sin(8 * np.pi * x_norm) + 
            0.3 * np.sin(4 * np.pi * x_norm) + 
            0.2 * np.sin(7 * np.pi * x_norm) + 
            0.1 * np.sin(10 * np.pi * x_norm)
        )
        
        # Enhanced exponential decay radial component with multiple decay rates
        exp_radial_term = np.sum(
            np.exp(-0.5 * x_norm ** 2) + 
            0.2 * np.exp(-0.3 * x_norm ** 4) + 
            0.1 * np.exp(-0.7 * x_norm ** 6) + 
            0.05 * np.exp(-0.1 * x_norm ** 8)
        )
        
        # Asymmetric cross-dimensional coupling with multiple coupling strengths
        asym_coupling_term = 0.2 * np.sum(
            np.exp(-0.5 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
            (x_norm[:-1] ** 2 + 0.5 * x_norm[1:] ** 2) +
            0.3 * np.exp(-0.3 * (x_norm[:-1] + x_norm[1:]) ** 2) * 
            (x_norm[:-1] ** 3 + 0.3 * x_norm[1:] ** 3)
        )
        
        # Additional nonlinear interaction terms with higher order polynomials
        nonlinear_interaction_term = 0.4 * np.sum(
            (x_norm[:-1] - x_norm[1:]) ** 4 + 
            0.5 * (x_norm[:-1] + x_norm[1:]) ** 3 +
            0.2 * (x_norm[:-1] * x_norm[1:]) ** 2
        )
        
        # Cross-dimensional polynomial interactions with sine modulation
        poly_sine_interaction = 0.3 * np.sum(
            np.sin(2 * np.pi * (x_norm[:-1] ** 2 + x_norm[1:] ** 2)) * 
            (x_norm[:-1] ** 2 + x_norm[1:] ** 2)
        )
        
        # Combined function with adjusted weights and additional complexity
        result = 3.5 * sine_term + 1.0 * exp_radial_term + 0.6 * asym_coupling_term + 0.5 * nonlinear_interaction_term + 0.3 * poly_sine_interaction
        
        return result