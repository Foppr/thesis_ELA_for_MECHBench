import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base with varying weights per dimension
        f1 = np.sum((x_norm ** 2) * (np.arange(1, self.dim + 1) / self.dim))
        
        # Nested sinusoidal terms with increasing frequency and phase shift
        f2 = np.sum(np.sin(10 * np.pi * x_norm + np.pi/4) ** 2)
        
        # Product of cosines with varying frequencies and phase shifts
        f3 = np.prod(np.cos(2 * np.pi * (x_norm + 0.2)) ** 2)
        
        # Exponential interaction term to increase complexity
        f4 = np.sum(np.exp(-x_norm**2) * np.sin(3 * np.pi * x_norm))
        
        # Fourth-order polynomial for higher nonlinearity
        f5 = np.sum(x_norm**4)
        
        # Combine all terms with adaptive weights based on dimensionality
        weights = [0.25, 0.20, 0.25, 0.20, 0.10]
        result = weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4 + weights[4] * f5
        
        return result