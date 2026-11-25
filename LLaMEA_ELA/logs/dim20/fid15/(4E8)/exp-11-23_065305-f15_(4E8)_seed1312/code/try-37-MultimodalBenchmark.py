import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Base quadratic term
        term1 = np.sum(x_norm**2)
        
        # Chaotic sine components with varying frequencies and amplitudes
        term2 = 0.3 * np.sum(np.sin(11 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Higher-order polynomial with sinusoidal modulation
        term3 = 0.15 * np.sum((x_norm**8) * np.sin(4 * np.pi * x_norm))
        
        # Cross-dimensional interaction with exponential decay
        term4 = 0.08 * np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Adaptive scaling based on dimension
        adaptive_scale = 0.1 * (self.dim / 10.0)
        term5 = adaptive_scale * np.sum((x_norm - 0.15)**4)
        
        # Additional noise-like term for increased complexity
        term6 = 0.05 * np.sum(np.sin(13 * x_norm) * np.cos(9 * x_norm))
        
        # Combine all terms
        result = term1 + term2 + term3 + term4 + term5 + term6
        
        return result