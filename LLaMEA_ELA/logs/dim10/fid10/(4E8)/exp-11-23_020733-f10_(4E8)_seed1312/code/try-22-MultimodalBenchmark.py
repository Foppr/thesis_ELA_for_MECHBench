import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with multiple local minima and varying frequencies
        f2 = np.sum(np.sin(3 * np.pi * x_norm)**2 + 0.5 * np.sin(7 * np.pi * x_norm)**2)
        
        # Product term creating complex landscape with multiple peaks and valleys
        f3 = np.prod(np.cos(2 * np.pi * x_norm) + 0.5 * np.cos(4 * np.pi * x_norm))
        
        # Higher-order polynomial interactions for increased complexity
        f4 = np.sum(x_norm**4 + 0.3 * x_norm**6)
        
        # Combined function with multiple competing terms and modified global minimum
        return 0.8 * f1 + 0.2 * f2 - 0.1 * f3 + 0.1 * f4