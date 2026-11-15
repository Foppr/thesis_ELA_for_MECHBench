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
        product_term = np.prod(np.cos(freqs * x_norm * np.exp(-0.1 * np.sum(x_norm**2))))
        
        # Chaotic sine-wave interaction term with dynamic frequency modulation
        chaotic_term = np.sum(np.sin(np.exp(x_norm) * np.pi * (1 + 0.1 * np.sin(np.sum(x_norm**2)))))
        
        # Polynomial interaction with mixed exponents and adaptive weights
        poly_term = np.sum(0.5 * x_norm**3 + 0.3 * x_norm**5 + 0.1 * x_norm**7)
        
        # Additional high-frequency oscillation with dynamic amplitude
        high_freq = np.sum(np.sin(15 * x_norm**2) * (1 + 0.2 * np.cos(np.sum(x_norm**2))))
        
        # Cross-term coupling with exponential decay
        cross_term = np.sum(np.exp(-0.5 * np.sum((x_norm[:, None] - x_norm[None, :])**2)) * np.sin(x_norm))
        
        # Combine all terms with optimized weights to create complex landscape
        return sum_squares + 0.3 * product_term + 0.08 * chaotic_term + 0.04 * poly_term + 0.15 * high_freq + 0.02 * cross_term