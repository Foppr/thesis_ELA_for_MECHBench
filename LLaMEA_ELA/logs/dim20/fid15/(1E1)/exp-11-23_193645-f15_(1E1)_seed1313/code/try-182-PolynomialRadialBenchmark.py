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
            rbf = np.exp(-5.0 * (x_norm - center) ** 2) + 0.3 * np.exp(-2.0 * (x_norm - center) ** 4)
            rbfs.append(rbf)
        radial_term = np.sum(np.array(rbfs))
        
        # Asymmetric cross-dimensional correlations with polynomial weights
        asym_corr_term = 0.4 * np.sum((x_norm[:-1] ** 3 + 0.5 * x_norm[1:] ** 2) * 
                                    np.exp(-0.5 * (x_norm[:-1] - x_norm[1:]) ** 2))
        
        # Coupled sine-cosine interactions with varying frequencies
        trig_term = 0.3 * np.sum(np.sin(3 * np.pi * x_norm[:-1]) * np.cos(2 * np.pi * x_norm[1:]) + 
                               0.5 * np.sin(4 * np.pi * x_norm[:-1]) * np.cos(3 * np.pi * x_norm[1:]))
        
        # Higher-order polynomial cross-terms for increased complexity
        high_order_term = 0.2 * np.sum((x_norm[:-1] ** 2 + x_norm[1:] ** 2) ** 2)
        
        # Combined function with different weights and asymmetric scaling
        result = 2.5 * poly_term + 1.2 * radial_term + 0.7 * asym_corr_term + 0.5 * trig_term + 0.3 * high_order_term
        
        return result