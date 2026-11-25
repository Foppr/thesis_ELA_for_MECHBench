import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial term with mixed degrees
        poly_term = np.sum(x_scaled**4 + 0.5 * x_scaled**3 + 0.1 * x_scaled**2)
        
        # Logarithmic barrier terms to create sharp constraints
        barrier_terms = np.sum(-np.log(1.0 - x_scaled**2 + 1e-8))
        
        # Trigonometric wave interactions with varying frequencies
        wave_term = np.sum(np.sin(5 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Coupling between adjacent dimensions with sine interaction
        coupling = 0.3 * np.sum(np.sin(2 * np.pi * (x_scaled[:-1] + x_scaled[1:])))
        
        # Additional polynomial coupling term
        poly_coupling = 0.2 * np.sum(x_scaled[:-1] * x_scaled[1:])
        
        # Combined function with multiple conflicting objectives
        return poly_term + barrier_terms + wave_term + coupling + poly_coupling