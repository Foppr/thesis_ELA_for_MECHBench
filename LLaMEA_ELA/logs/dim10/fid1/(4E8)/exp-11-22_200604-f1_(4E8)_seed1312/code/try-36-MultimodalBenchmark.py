import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal components with varying amplitudes
        f2 = 0.3 * np.sum(np.sin(12 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Exponential penalty terms to create sharp ridges and deep valleys
        f3 = 0.1 * np.sum(np.exp(2 * np.abs(x_norm)) - 1)
        
        # Octic polynomial term for extreme nonlinearity
        f4 = 0.05 * np.sum(x_norm**8)
        
        # Cross-terms with sine and cosine interactions between all dimensions
        f5 = 0.04 * np.sum(np.sin(x_norm[:-1] + x_norm[1:]) * np.cos(x_norm[:-1] - x_norm[1:]))
        
        # Nested trigonometric term for increased complexity
        f6 = 0.2 * np.sum(np.sin(3 * np.pi * np.sin(2 * np.pi * x_norm)))
        
        # Mixed polynomial and exponential interaction terms
        f7 = 0.03 * np.sum((x_norm[:-1]**2 + x_norm[1:]**2) * np.exp(-0.5 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7
        
        return result