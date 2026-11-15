import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with higher frequency and different amplitude to create more local minima
        f2 = np.sum(np.sin(8 * np.pi * x_norm) ** 2)
        
        # Additional cubic terms for non-convexity
        f3 = np.sum(x_norm**3)
        
        # Cross-terms to increase complexity and interaction between dimensions
        f4 = np.sum(x_norm[:-1] * x_norm[1:])
        
        # Combine terms with different weights
        return f1 + 0.15 * f2 + 0.02 * f3 + 0.05 * f4