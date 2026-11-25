import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Add sinusoidal oscillations with higher frequency and amplitude to create more local minima
        f2 = 0.2 * np.sum(np.sin(8 * np.pi * x_norm**3))
        
        # Add a cubic term to increase complexity and create sharper gradients
        f3 = 0.05 * np.sum(x_norm**3)
        
        # Combine terms with different weights
        result = f1 + f2 + f3
        
        return result