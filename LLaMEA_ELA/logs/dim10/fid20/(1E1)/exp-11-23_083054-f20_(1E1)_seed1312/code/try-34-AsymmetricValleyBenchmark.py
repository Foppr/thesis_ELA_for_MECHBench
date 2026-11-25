import numpy as np

class AsymmetricValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial terms with different exponents to create varied curvature
        f1 = np.sum(0.5 * x_norm**2 + 0.3 * x_norm**4 + 0.1 * x_norm**6)
        
        # Trigonometric terms creating oscillating valleys
        f2 = np.sum(np.sin(3 * np.pi * x_norm) ** 2 + 0.7 * np.sin(6 * np.pi * x_norm) ** 2)
        
        # Exponential barrier terms to create steep gradients
        f3 = np.sum(np.exp(2 * np.abs(x_norm)) - 1 + 0.5 * np.exp(-2 * np.abs(x_norm)))
        
        # Asymmetric interaction terms using piecewise functions
        asymmetric_term = np.sum((x_norm + 0.5) ** 2 * (x_norm > -0.5) + (x_norm - 0.5) ** 2 * (x_norm <= -0.5))
        
        # Cross-terms creating complex ridges and valleys
        f4 = np.sum(x_norm[:-1] * x_norm[1:] * np.cos(2 * np.pi * x_norm[:-1]))
        
        # Combine all terms with different weights
        return 0.7 * f1 + 0.2 * f2 + 0.08 * f3 + 0.02 * f4 + 0.05 * asymmetric_term