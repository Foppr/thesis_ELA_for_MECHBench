import numpy as np

class ExponentialSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial interaction component with varying degrees
        poly_term = np.sum(x_norm ** 4 + 0.5 * x_norm ** 3 + 0.2 * x_norm ** 2)
        
        # Gaussian radial basis function with asymmetric variances
        gaussian_radial_term = np.sum(np.exp(-0.5 * x_norm ** 2) + 0.3 * np.exp(-0.2 * x_norm ** 4))
        
        # Asymmetric cross-dimensional coupling with polynomial weights
        asym_coupling_term = 0.3 * np.sum((x_norm[:-1] ** 2 + 0.5 * x_norm[1:] ** 2) * 
                                         np.exp(-0.3 * (x_norm[:-1] - x_norm[1:]) ** 2))
        
        # Nonlinear interaction terms with polynomial modulation and varying amplitudes
        poly_interaction_term = 0.4 * np.sum((x_norm[:-1] + x_norm[1:]) ** 3 * 
                                           (x_norm[:-1] ** 2 + x_norm[1:] ** 2))
        
        # Combined function with different weights and asymmetric scaling
        result = 2.5 * poly_term + 0.9 * gaussian_radial_term + 0.6 * asym_coupling_term + 0.3 * poly_interaction_term
        
        return result