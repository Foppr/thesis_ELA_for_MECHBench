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
        
        # Chaotic sine-wave interaction term with adaptive frequencies
        adaptive_freqs = np.exp(np.abs(x_norm)) * np.pi
        chaotic_term = np.sum(np.sin(adaptive_freqs))
        
        # Polynomial interaction with mixed exponents
        poly_term = np.sum(x_norm**3 + 0.5 * x_norm**5)
        
        # Additional high-frequency oscillation with cross-dimension coupling
        cross_term = np.sum(np.sin(10 * np.sum(x_norm**2)))
        
        # Combine all terms with varying weights to create complex landscape
        return sum_squares + 0.2 * product_term + 0.05 * chaotic_term + 0.03 * poly_term + 0.1 * cross_term