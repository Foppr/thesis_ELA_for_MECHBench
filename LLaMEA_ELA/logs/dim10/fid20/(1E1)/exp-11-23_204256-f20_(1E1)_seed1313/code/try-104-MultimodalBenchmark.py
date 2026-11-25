import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_normalized**2)
        
        # High-frequency sinusoidal terms with varying amplitudes
        f2 = 0.8 * np.sum(np.sin(25 * x_normalized) ** 2)
        f3 = 0.6 * np.sum(np.cos(18 * x_normalized) ** 2)
        
        # Cross-dimensional polynomial interactions
        f4 = 0.2 * np.sum(x_normalized[:-1] ** 2 * x_normalized[1:] ** 2)
        f5 = 0.15 * np.sum(x_normalized[:-2] ** 3 * x_normalized[1:-1] * x_normalized[2:] ** 2)
        
        # Exponential conditioning factor based on dimensionality
        cond_factor = 1.0 + 0.5 * (self.dim / 10.0) * np.exp(0.1 * self.dim)
        
        # Add a modified exponential term to increase difficulty
        f6 = 0.3 * np.sum(np.exp(0.5 * x_normalized**2) - 1)
        
        # Cubic and higher-order terms for added complexity
        f7 = 0.1 * np.sum(x_normalized**4)
        f8 = 0.08 * np.sum(x_normalized**6)
        
        return cond_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)