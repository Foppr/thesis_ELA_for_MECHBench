import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Normalize input to [-1, 1] for chaotic behavior
        x_norm = x / 5.0
        
        # Chaotic sine wave component
        chaotic_term = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Polynomial term with varying coefficients
        poly_term = np.sum((x_norm ** (2 + np.arange(self.dim))) / (2 + np.arange(self.dim)))
        
        # Distance from origin squared
        distance_term = np.sum(x_norm ** 2)
        
        # Dimensionality-dependent scaling
        dim_scaling = self.dim * 0.1
        
        # Combine all terms with different weights
        result = 0.5 * chaotic_term + 0.3 * poly_term + 0.2 * distance_term + dim_scaling
        
        return result