import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Multiple quadratic terms with varying coefficients
        term1 = np.sum(x_norm**2 * (1 + 0.5 * np.sin(3 * x_norm)))
        
        # High-frequency sinusoidal components with varying amplitudes
        frequencies = np.arange(1, self.dim + 1)
        term2 = np.sum(np.sin(frequencies * np.pi * x_norm)**2 * np.exp(-0.1 * np.abs(x_norm)))
        
        # Polynomial barrier terms to create complex landscape
        term3 = np.sum((x_norm**4 - 2 * x_norm**2 + 1) * np.cos(2 * np.pi * x_norm))
        
        # Dynamic scaling factor based on dimensionality
        scale_factor = 1.0 + 0.1 * np.sin(self.dim)
        
        # Add interaction terms between dimensions
        interaction = np.sum(np.sin(x_norm[:-1] - x_norm[1:]) * np.cos(x_norm[:-1] + x_norm[1:]))
        
        # Global minimum is at origin, so add a penalty for deviation from zero
        penalty = 0.5 * np.sum(x_norm**6)
        
        return scale_factor * (term1 + term2 + 0.3 * term3 + 0.1 * interaction + penalty)