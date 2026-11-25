import numpy as np

class PolynomialRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial interaction terms with varying degrees
        poly_term = np.sum(x_norm ** 4 + 0.5 * x_norm ** 3 - 0.3 * x_norm ** 2 + 0.1 * x_norm)
        
        # Radial basis function component with multiple centers
        rbfs = []
        centers = np.linspace(-1, 1, 5)
        for center in centers:
            rbf = np.exp(-2.0 * np.sum((x_norm - center) ** 2))
            rbfs.append(rbf)
        radial_term = np.sum(rbfs)
        
        # Directional asymmetry with exponential weighting
        asym_term = 0.3 * np.sum(np.exp(2 * x_norm[:-1]) * x_norm[1:] ** 2 + 
                                np.exp(-x_norm[1:]) * x_norm[:-1] ** 2)
        
        # Cross-dimensional coupling with cosine modulation
        coupling_term = 0.4 * np.sum(np.cos(3 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                                   (x_norm[:-1] ** 2 + x_norm[1:] ** 2))
        
        # Combined function with different weights and non-linear scaling
        result = 2.0 * poly_term + 0.7 * radial_term + 0.6 * asym_term + 0.5 * coupling_term
        
        return result