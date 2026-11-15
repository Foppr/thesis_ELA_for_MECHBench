import numpy as np

class PolynomialSpiralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients for different dimensions
        self.coeffs = np.random.randn(dim, 5) * 0.5
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component
        poly_chaos = 0.0
        for i in range(self.dim):
            for j in range(5):
                poly_chaos += self.coeffs[i, j] * np.polynomial.hermite.hermval(x_norm[i], [0]*j + [1])
        
        # Radial basis functions with adaptive conditioning
        rbfs = 0.0
        centers = np.random.randn(10, self.dim) * 0.5
        for center in centers:
            distance = np.sqrt(np.sum((x_norm - center)**2))
            rbfs += np.exp(-10 * distance**2) * np.sin(5 * distance)
        
        # Global spiral gradient field
        if self.dim >= 2:
            r = np.sqrt(x_norm[0]**2 + x_norm[1]**2)
            theta = np.arctan2(x_norm[1], x_norm[0])
            spiral_field = r * np.sin(3 * theta + 2 * r) * np.cos(2 * theta - r)
        else:
            spiral_field = 0.0
            
        # High-frequency oscillatory component
        oscillatory = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm))
        
        # Adaptive conditioning term
        conditioning = np.sum((x_norm**2) * (1 + 0.1 * np.abs(x_norm)))
        
        # Combine all components with different weights
        return 1.5 * poly_chaos + 2.0 * rbfs + 1.2 * spiral_field + 0.8 * oscillatory + 0.3 * conditioning