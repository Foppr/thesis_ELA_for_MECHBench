import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sine terms with different frequencies
        f2 = np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        # Product term creating complex landscape
        f3 = np.prod(np.cos(np.pi * x_norm / 2.0))
        
        # Combined function with multiple local minima
        return f1 + 0.1 * f2 - 0.05 * f3 + 0.01 * np.sum(x_norm**4)