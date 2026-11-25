import numpy as np

class PolynomialRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial interaction terms with varying degrees
        poly_term = np.sum(x_norm ** 4 + 0.8 * x_norm ** 3 + 0.5 * x_norm ** 2 + 0.2 * x_norm)
        
        # Radial basis function component with multiple centers
        rbfs = []
        centers = np.linspace(-1, 1, min(5, self.dim))
        for center in centers:
            rbf = np.exp(-5.0 * np.sum((x_norm - center) ** 2))
            rbfs.append(rbf)
        radial_term = np.sum(rbfs)
        
        # Asymmetric gradient-based coupling between dimensions
        grad_coupling = 0.0
        for i in range(self.dim - 1):
            diff = x_norm[i] - x_norm[i+1]
            grad_coupling += (diff ** 2) * np.exp(-0.5 * (x_norm[i] ** 2 + x_norm[i+1] ** 2))
        
        # Cross-dimensional polynomial interactions with varying weights
        cross_poly = 0.0
        for i in range(self.dim - 2):
            cross_poly += (x_norm[i] ** 3) * (x_norm[i+1] ** 2) * (x_norm[i+2] ** 1)
        
        # Sine modulation of the radial component for additional complexity
        sine_mod = np.sin(3.0 * np.sum(x_norm ** 2))
        
        # Combined function with different weights
        result = 2.5 * poly_term + 1.8 * radial_term + 0.7 * grad_coupling + 0.4 * cross_poly + 0.3 * sine_mod
        
        return result