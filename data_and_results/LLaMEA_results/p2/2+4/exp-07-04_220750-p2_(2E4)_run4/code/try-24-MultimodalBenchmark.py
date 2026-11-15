import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of squares term
        sum_squares = np.sum(x_norm**2)
        
        # Exponentially weighted product of cosines with varying frequencies
        freqs = np.arange(1, self.dim + 1)
        product_term = np.prod(np.cos(freqs * x_norm))
        
        # Chaotic sine-wave interaction term with enhanced nonlinearity
        chaotic_term = np.sum(np.sin(np.exp(2 * x_norm) * np.pi))
        
        # Polynomial interaction with mixed exponents and additional coupling
        poly_term = np.sum(x_norm**4 + 0.3 * x_norm**6 + 0.1 * np.prod(x_norm.reshape(-1, 1) @ x_norm.reshape(1, -1), axis=1))
        
        # Additional high-frequency oscillation with quadratic modulation
        high_freq = np.sum(np.sin(15 * x_norm**2) * np.exp(-x_norm**2))
        
        # Combine all terms with varying weights to create complex landscape
        return sum_squares + 0.3 * product_term + 0.08 * chaotic_term + 0.05 * poly_term + 0.15 * high_freq