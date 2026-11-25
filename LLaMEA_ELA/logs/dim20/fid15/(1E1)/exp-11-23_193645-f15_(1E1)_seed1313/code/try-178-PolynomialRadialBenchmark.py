import numpy as np

class PolynomialRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial interaction terms with varying degrees
        poly_term = np.sum(x_norm ** 4 + 0.5 * x_norm ** 3 + 0.2 * x_norm ** 2)
        
        # Radial basis function component with multiple centers
        rbfs = []
        centers = np.linspace(-1, 1, 5)
        for center in centers:
            rbfs.append(np.exp(-5.0 * (x_norm - center) ** 2))
        rbf_term = np.sum(rbfs)
        
        # Asymmetric gradient field with directional bias
        grad_field = np.sum((x_norm[:-1] ** 3 + 0.5 * x_norm[1:] ** 3) * 
                           np.exp(-0.5 * (x_norm[:-1] ** 2 + x_norm[1:] ** 2)))
        
        # Cross-dimensional coupling with cosine modulation
        coupling_term = 0.7 * np.sum(np.cos(3 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                   (x_norm[:-1] ** 2 + x_norm[1:] ** 2))
        
        # Nonlinear transformation with sigmoid-like behavior
        sigmoid_term = np.sum(1.0 / (1.0 + np.exp(-3.0 * x_norm)))
        
        # Combined function with different weights and asymmetric scaling
        result = 2.0 * poly_term + 1.5 * rbf_term + 0.8 * grad_field + 0.6 * coupling_term + 0.3 * sigmoid_term
        
        return result