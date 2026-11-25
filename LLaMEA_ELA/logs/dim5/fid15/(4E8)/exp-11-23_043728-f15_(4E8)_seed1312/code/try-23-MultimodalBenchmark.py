import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term for global convergence
        quadratic_term = np.sum(x_norm**2)
        
        # Coupled sinusoidal oscillations creating complex landscape
        sin_term = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Higher-order polynomial for increased complexity
        poly_term = np.sum(x_norm**4) + 0.05 * np.sum(x_norm**6)
        
        # Cross-terms to create dependency between dimensions with varying weights
        cross_term = 0.1 * np.sum(x_norm[:-1] * x_norm[1:] * (1 + 0.1 * np.arange(self.dim - 1)))
        
        # Adaptive scaling based on dimensionality
        scale_factor = 1.0 + 0.1 * (self.dim - 1) / self.dim
        
        # Additional harmonic component for enhanced multimodality
        harmonic_term = 0.2 * np.sum(np.sin(5 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm))
        
        return scale_factor * (quadratic_term + 0.3 * sin_term + 0.005 * poly_term + cross_term + harmonic_term)