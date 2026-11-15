import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial conditioning term with increasing powers
        poly_term = np.sum((x_norm ** (2 + np.arange(self.dim))) ** 2)
        
        # High-frequency sinusoidal terms with exponentially increasing frequencies
        freqs = np.exp(np.arange(self.dim) * np.log(10))  # Frequencies: 1, 10, 100, ...
        sin_term = np.sum(np.sin(freqs * np.pi * x_norm) ** 2)
        
        # Add cosine interactions between dimensions
        cos_interaction = np.sum(np.cos(freqs * np.pi * x_norm) * np.sin(freqs * np.pi * x_norm))
        
        # Shift the global minimum to a non-zero location
        shift = 0.5 * np.ones(self.dim)
        shifted_term = np.sum((x_norm - shift) ** 2)
        
        # Add a dynamic noise component that depends on the function value
        noise = 0.2 * np.random.random() * (1 + np.abs(poly_term + sin_term))
        
        # Combine terms with different weights to create a complex landscape
        return 0.5 * poly_term + 0.3 * sin_term + 0.2 * cos_interaction + 0.1 * shifted_term + noise