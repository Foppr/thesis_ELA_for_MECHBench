import numpy as np

class PolynomialRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial interaction terms with mixed degrees
        poly_term = np.sum(x_norm ** 4 + 0.5 * x_norm ** 3 - 0.3 * x_norm ** 2 + 0.1 * x_norm)
        
        # Radial basis function component with varying widths and centers
        rbfs = []
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i, center in enumerate(centers):
            width = 0.5 + 0.3 * (i % 2)
            rbf = np.exp(-0.5 * ((x_norm - center) / width) ** 2)
            rbfs.append(rbf)
        radial_term = np.sum(np.array(rbfs))
        
        # Asymmetric gradient-based coupling
        grad_coupling = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                diff = x_norm[i] - x_norm[i+1]
                grad_coupling += (diff ** 2) * np.exp(-0.1 * np.abs(diff)) * (1 + 0.5 * (i % 3))
        
        # Cross-dimensional nonlinear interaction with sinusoidal modulation
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += np.sin(2 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i+1])
            cross_term += 0.3 * (x_norm[i] ** 2) * np.exp(-0.5 * x_norm[i+1] ** 2)
        
        # Combined function with different weights
        result = 2.0 * poly_term + 1.5 * radial_term + 0.8 * grad_coupling + 0.6 * cross_term
        
        return result