import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial shaping terms with varying degrees
        poly_term = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.1 * x_norm**2)
        
        # Periodic components with multiple frequencies and amplitudes
        periodic_term = 10 * np.sum(np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Asymmetric conditioning: different treatment for positive and negative values
        asym_term = np.sum(np.where(x_norm >= 0, 2 * x_norm**2, 0.5 * x_norm**2))
        
        # Cross-terms with exponential weighting to increase non-separability
        cross_term = 0.5 * np.sum(np.exp(np.abs(x_norm[:-1] * x_norm[1:])) - 1)
        
        # Global minimum at origin with additional scaling
        return 0.1 * poly_term + periodic_term + asym_term + cross_term