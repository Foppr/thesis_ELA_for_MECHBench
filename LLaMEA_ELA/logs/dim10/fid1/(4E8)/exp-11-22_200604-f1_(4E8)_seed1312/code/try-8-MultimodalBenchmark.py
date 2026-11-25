import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal modulations with exponential scaling
        f2 = np.sum(np.sin(10 * np.pi * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Polynomial interaction terms creating complex landscape
        f3 = np.sum((x_norm**4 - 2 * x_norm**2 + 1)**2)
        
        # Exponentially decaying harmonic terms
        f4 = np.sum(np.exp(-2 * np.abs(x_norm)) * np.cos(8 * np.pi * x_norm))
        
        # Cross-term interactions creating intricate valleys
        f5 = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(3 * np.pi * (x_norm[:-1] + x_norm[1:])))
        
        # Combine all terms with varying weights
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4 + 0.05 * f5