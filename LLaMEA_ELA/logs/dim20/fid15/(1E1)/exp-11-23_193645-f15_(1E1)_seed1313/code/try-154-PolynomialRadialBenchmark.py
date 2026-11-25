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
        
        # Radial basis function component with different centers and widths
        rbfs = []
        centers = np.linspace(-1, 1, 5)
        widths = np.logspace(-2, 0, 5)
        for i, (center, width) in enumerate(zip(centers, widths)):
            rbf = np.exp(-0.5 * ((x_norm - center) ** 2) / (width ** 2))
            rbfs.append(rbf)
        radial_term = np.sum(np.array(rbfs).T, axis=1)
        
        # Cross-dimensional asymmetric coupling with polynomial weights
        asym_coupling = 0.3 * np.sum((x_norm[:-1] ** 2 + 0.5 * x_norm[1:] ** 3) * 
                                   np.exp(-0.1 * (x_norm[:-1] - x_norm[1:]) ** 2))
        
        # Mixed sine-cosine modulation with polynomial scaling
        modulated_term = 0.4 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm) + 
                                    0.3 * np.sin(5 * np.pi * x_norm))
        
        # Combined function with different weights and asymmetric scaling
        result = 2.0 * poly_term + 1.5 * np.sum(radial_term) + 0.6 * asym_coupling + 0.3 * modulated_term
        
        return result