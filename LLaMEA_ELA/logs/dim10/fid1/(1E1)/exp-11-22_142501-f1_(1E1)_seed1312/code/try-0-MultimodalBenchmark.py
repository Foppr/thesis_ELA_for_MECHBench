import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of squared terms with different frequencies
        f1 = np.sum(x_normalized**2)
        
        # High-frequency oscillatory component
        f2 = np.sum(np.sin(10 * np.pi * x_normalized) * np.exp(-0.5 * x_normalized**2))
        
        # Product of cosine terms creating multiple local minima
        f3 = np.prod(np.cos(x_normalized / 2.0))
        
        # Combined function with different weights
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 1.0