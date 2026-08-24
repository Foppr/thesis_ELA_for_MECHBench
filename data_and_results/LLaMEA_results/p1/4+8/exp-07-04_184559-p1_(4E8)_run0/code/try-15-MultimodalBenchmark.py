import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with higher frequency to increase local minima
        f2 = np.sum(np.sin(7 * np.pi * x_norm)**2)
        
        # Additional quadratic term with different scaling and shift
        f3 = 0.1 * np.sum((x_norm - 0.3)**2)
        
        # Cross-terms to introduce interactions between dimensions
        f4 = 0.05 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Combine terms to create a challenging landscape
        return f1 + 0.5 * f2 + f3 + f4