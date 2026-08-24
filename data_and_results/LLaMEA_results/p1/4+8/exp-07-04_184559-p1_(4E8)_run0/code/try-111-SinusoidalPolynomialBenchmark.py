import numpy as np

class SinusoidalPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency components for sinusoidal terms
        self.frequencies = np.arange(1, dim + 1)
        # Precompute polynomial chaos coefficients
        self.poly_coeffs = np.random.uniform(-1, 1, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal wave component with varying frequencies
        sin_term = np.sum(np.sin(self.frequencies * x_norm) * np.cos(self.frequencies * x_norm))
        
        # Polynomial chaos expansion component
        poly_expansion = np.sum(self.poly_coeffs * np.polyval([1, 0, -1], x_norm))  # x^2 - 1
        
        # Coupled polynomial interaction terms
        poly_interaction = np.sum(x_norm[:-1]**2 * x_norm[1:]**3)
        
        # Adaptive conditioning based on local gradient
        grad_magnitude = np.abs(np.gradient(x_norm))
        conditioning = 1 + 0.5 * np.exp(-grad_magnitude)
        cond_term = np.sum(conditioning * x_norm**6)
        
        # Multi-scale sinusoidal modulation
        modulated_term = np.sum(np.sin(5 * x_norm + np.sin(3 * x_norm)) * 
                               np.cos(2 * x_norm + np.sin(4 * x_norm)))
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * 
                               (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Combine all components with dynamic weights
        return 2.0 * sin_term + 1.5 * poly_expansion + 0.8 * poly_interaction + \
               1.2 * cond_term + 1.0 * modulated_term + 0.6 * cross_coupling