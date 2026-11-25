import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base with conditioning
        f1 = np.sum(x_norm**2)
        
        # Nested sinusoidal terms with varying frequencies and amplitudes
        f2 = 0.3 * np.sum(np.sin(8 * x_norm) ** 2)
        f3 = 0.2 * np.sum(np.sin(12 * x_norm) ** 2)
        f4 = 0.15 * np.sum(np.sin(20 * x_norm) ** 2)
        
        # Asymmetric polynomial terms
        f5 = 0.1 * np.sum(np.abs(x_norm)**3)
        f6 = 0.05 * np.sum(np.abs(x_norm)**4)
        
        # Cross-dimensional interactions with asymmetric weights
        f7 = 0.1 * np.sum(x_norm[:-1] ** 2 * x_norm[1:] ** 3)
        f8 = 0.08 * np.sum(x_norm[:-2] * x_norm[1:-1] ** 2 * x_norm[2:] ** 2)
        
        # Exponentially increasing difficulty with dimensionality
        scale_factor = 1.0 + 0.3 * np.exp(0.08 * self.dim)
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)