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
        centers = np.linspace(-1, 1, min(5, self.dim))
        for center in centers:
            rbf = np.exp(-2.0 * np.sum((x_norm - center) ** 2))
            rbfs.append(rbf)
        radial_term = np.sum(rbfs)
        
        # Gradient-based asymmetry with directional weighting
        grad_asymmetry = 0.0
        for i in range(self.dim - 1):
            diff = x_norm[i] - x_norm[i+1]
            weight = (i + 1) / self.dim
            grad_asymmetry += weight * np.abs(diff) ** 1.5
        
        # Cross-dimensional coupling with polynomial weights
        coupling_term = 0.0
        for i in range(self.dim - 2):
            coupling = (x_norm[i] ** 2 + x_norm[i+1] ** 2) * (x_norm[i+2] ** 3)
            coupling_term += coupling
        
        # Combined function with different weights and scaling factors
        result = 2.0 * poly_term + 0.7 * radial_term + 0.4 * grad_asymmetry + 0.3 * coupling_term
        
        return result