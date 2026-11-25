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
        f2 = 15 * np.sum(np.sin(7 * np.pi * x_normalized)**2)
        
        # Additional cubic terms with different scales
        f3 = 0.2 * np.sum((x_normalized - 0.3)**3)
        
        # Quadratic terms with shift to create more complex landscape
        f4 = 0.1 * np.sum((x_normalized + 0.4)**2)
        
        # Combine all terms with different weights
        return f1 + f2 + f3 + f4