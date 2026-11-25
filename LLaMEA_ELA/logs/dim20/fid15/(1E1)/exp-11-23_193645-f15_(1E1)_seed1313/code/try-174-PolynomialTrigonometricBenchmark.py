import numpy as np

class PolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial interaction terms with varying degrees
        poly_term = np.sum(x_norm ** 4 + 0.8 * x_norm ** 3 + 0.5 * x_norm ** 2 + 0.2 * x_norm)
        
        # Trigonometric coupling between dimensions with varying frequencies
        trig_coupling = np.sum(np.sin(3 * np.pi * x_norm[:-1]) * np.cos(2 * np.pi * x_norm[1:]) + 
                              0.7 * np.sin(5 * np.pi * x_norm[:-1]) * np.cos(4 * np.pi * x_norm[1:]))
        
        # Adaptive noise component that varies based on position
        noise = 0.3 * np.sum(np.sin(x_norm ** 2) * np.cos(x_norm ** 3))
        
        # Cross-dimensional polynomial interactions with varying weights
        cross_poly = 0.5 * np.sum((x_norm[:-1] ** 2 + x_norm[1:] ** 2) * 
                                (x_norm[:-1] + x_norm[1:]) ** 2)
        
        # Exponential modulation based on distance from center
        exp_modulation = np.exp(-0.5 * np.sum(x_norm ** 2))
        
        # Combined function with different weights and scaling factors
        result = 2.0 * poly_term + 1.5 * trig_coupling + 0.8 * noise + 0.6 * cross_poly + 0.3 * exp_modulation
        
        return result