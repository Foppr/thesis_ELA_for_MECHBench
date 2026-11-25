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
        
        # Radial basis function component with varying widths and centers
        rbfs = []
        for i in range(self.dim):
            center = np.sin(i * np.pi / self.dim)  # Varying centers
            width = 0.5 + 0.5 * np.cos(i * np.pi / self.dim)  # Varying widths
            rbfs.append(np.exp(-width * (x_norm[i] - center) ** 2))
        rbf_term = np.sum(rbfs)
        
        # Asymmetric gradient-based coupling with exponential decay
        grad_coupling = 0.0
        for i in range(self.dim - 1):
            diff = x_norm[i] - x_norm[i+1]
            weight = np.exp(-0.5 * (i / self.dim) ** 2)  # Asymmetric weighting
            grad_coupling += weight * diff ** 2 * np.sin(3 * np.pi * diff)
        
        # Cross-dimensional nonlinear interaction with polynomial coupling
        cross_term = 0.0
        for i in range(self.dim - 2):
            cross_term += (x_norm[i] ** 2 + x_norm[i+1] ** 2) * np.sin(2 * np.pi * x_norm[i+2])
        
        # Combined function with different weights
        result = 2.0 * poly_term + 1.5 * rbf_term + 0.8 * grad_coupling + 0.6 * cross_term
        
        return result