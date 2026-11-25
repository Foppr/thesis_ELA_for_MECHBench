import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal modulation with exponential growth
        frequencies = np.arange(1, self.dim + 1) * np.exp(np.arange(1, self.dim + 1) * 0.5)
        f2 = np.sum(np.sin(frequencies * np.pi * x_norm) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Quartic interaction terms between dimensions
        f3 = 0.05 * np.sum((x_norm**4) * np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Add a global scaling factor and offset for better conditioning
        return f1 + f2 + f3 + 0.01 * np.sum(x_norm**6)