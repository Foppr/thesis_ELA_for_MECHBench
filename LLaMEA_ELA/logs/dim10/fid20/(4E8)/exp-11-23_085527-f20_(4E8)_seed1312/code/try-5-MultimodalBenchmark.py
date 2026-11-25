import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Sum of squared terms with different frequencies
        f1 = np.sum(x_normalized**2)
        
        # High-frequency oscillations creating many local minima
        f2 = 10 * np.sum(np.sin(5 * np.pi * x_normalized)**2)
        
        # Additional quadratic terms with different scales
        f3 = 0.1 * np.sum((x_normalized - 0.5)**2)
        
        # Combine all terms with different weights
        return f1 + f2 + f3