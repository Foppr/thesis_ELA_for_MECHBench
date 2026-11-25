import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial correlation term with varying exponents
        poly_term = np.sum((x_norm ** 3 + 0.5 * x_norm ** 2 - 0.3 * x_norm) ** 2)
        
        # Logarithmic barrier component creating narrow fitness valleys
        log_barrier = np.sum(np.log(1 + 0.1 * np.abs(x_norm)) * np.sin(5 * np.pi * x_norm))
        
        # Fractal-like self-similarity using recursive trigonometric modulation
        fractal_term = 0.05 * np.sum(np.sin(2 ** (np.arange(self.dim) + 1) * np.pi * x_norm) ** 2)
        
        # Cross-dimensional interaction with exponential decay
        cross_interaction = 0.02 * np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * 
                                         (x_norm[:-1] ** 2 + x_norm[1:] ** 2))
        
        # Add a global scaling factor based on the norm
        scale_factor = 1.0 + 0.2 * np.sin(3 * np.sqrt(np.sum(x_norm**2)))
        
        return scale_factor * (poly_term + log_barrier + fractal_term + cross_interaction)