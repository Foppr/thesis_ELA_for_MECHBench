import numpy as np

class PolynomialGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial interaction terms with varying degrees
        poly_term = np.sum(x_norm ** 4 + 0.8 * x_norm ** 3 + 0.5 * x_norm ** 2)
        
        # Gaussian hill structures with varying centers and widths
        gaussian_hills = np.sum(np.exp(-2.0 * (x_norm - 0.3) ** 2) + 
                               0.7 * np.exp(-1.5 * (x_norm + 0.4) ** 2) + 
                               0.5 * np.exp(-3.0 * x_norm ** 2))
        
        # Gradient-based asymmetry with directional weighting
        grad_asym = np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * (x_norm[:-1] ** 2 + 0.3 * x_norm[1:] ** 2))
        
        # Cross-dimensional quadratic coupling with varying weights
        quad_coupling = 0.6 * np.sum((x_norm[:-1] ** 2 + x_norm[1:] ** 2) * 
                                   np.exp(-0.5 * (x_norm[:-1] - x_norm[1:]) ** 2))
        
        # Additional cubic interaction terms for increased complexity
        cubic_term = 0.3 * np.sum((x_norm[:-1] + x_norm[1:]) ** 3)
        
        # Combined function with different weights and asymmetric scaling
        result = 2.5 * poly_term + 1.2 * gaussian_hills + 0.7 * grad_asym + 0.5 * quad_coupling + 0.3 * cubic_term
        
        return result