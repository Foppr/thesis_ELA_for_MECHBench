import numpy as np

class PolynomialRadialAsymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial interaction terms with varying degrees
        poly_term = np.sum(x_norm ** 4 + 0.5 * x_norm ** 3 + 0.2 * x_norm ** 2)
        
        # Radial basis function component with multiple centers
        rbf_term = np.sum(np.exp(-np.sum((x_norm.reshape(-1, 1) - np.linspace(-1, 1, 5)) ** 2, axis=0)))
        
        # Directional asymmetry with cosine modulation
        asym_term = np.sum(np.cos(3 * np.pi * x_norm) * np.abs(x_norm) ** 1.5)
        
        # Cross-dimensional coupling with quadratic interactions
        cross_coupling = 0.3 * np.sum((x_norm[:-1] ** 2 + x_norm[1:] ** 2) * 
                                    np.exp(-0.5 * (x_norm[:-1] - x_norm[1:]) ** 2))
        
        # Saddle point structure with mixed concave-convex behavior
        saddle_term = np.sum(x_norm ** 2 * np.sin(2 * np.pi * x_norm) + 
                           0.5 * x_norm ** 4 * np.cos(3 * np.pi * x_norm))
        
        # Combined function with different weights and asymmetric scaling
        result = 2.0 * poly_term + 1.2 * rbf_term + 0.8 * asym_term + 0.6 * cross_coupling + 0.4 * saddle_term
        
        return result