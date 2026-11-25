import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term with conditioning
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms with exponential scaling
        f2 = np.sum(np.sin(10 * np.pi * x_norm) ** 2 * np.exp(2 * np.abs(x_norm)))
        
        # Polynomial interaction terms creating complex valleys
        f3 = np.sum((x_norm**4 + 0.1 * x_norm**3 - 0.5 * x_norm**2) * np.exp(-0.5 * x_norm**2))
        
        # Cross-terms with varying weights to create intricate landscape
        f4 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * 
                   np.exp(-0.1 * np.sum(x_norm**2)))
        
        # Combine all terms with different weights and add constant offset
        return 0.05 * f1 + 0.4 * f2 + 0.3 * f3 + 0.25 * f4 + 2.0