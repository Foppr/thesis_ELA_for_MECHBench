import numpy as np

class PolynomialGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial interaction terms with varying degrees
        poly_term = np.sum(x_norm ** 4 + 0.5 * x_norm ** 3 - 0.3 * x_norm ** 2 + 0.1 * x_norm)
        
        # Gaussian radial basis function component with adaptive variances
        gauss_radial_term = np.sum(np.exp(-0.5 * (x_norm ** 2) / 0.8) + 
                                  0.3 * np.exp(-0.5 * (x_norm ** 2) / 0.3) + 
                                  0.1 * np.exp(-0.5 * (x_norm ** 2) / 1.2))
        
        # Directional asymmetry through weighted cross-terms
        asym_term = 0.4 * np.sum((x_norm[:-1] ** 2) * np.abs(x_norm[1:]) + 
                               0.3 * (x_norm[1:] ** 2) * np.abs(x_norm[:-1]))
        
        # Coupling between adjacent dimensions with sinusoidal modulation
        coupling_term = 0.5 * np.sum(np.sin(3 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                                   (x_norm[:-1] ** 2 + x_norm[1:] ** 2))
        
        # Combined function with different weights and directional bias
        result = 2.0 * poly_term + 0.7 * gauss_radial_term + 0.6 * asym_term + 0.3 * coupling_term
        
        return result