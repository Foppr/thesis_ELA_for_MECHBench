import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Add high-frequency sinusoidal oscillations to create multiple local minima
        f2 = 0.2 * np.sum(np.sin(10 * np.pi * x_norm))
        
        # Add cubic and quartic terms to increase complexity
        f3 = 0.05 * np.sum(x_norm**3)
        f4 = 0.02 * np.sum(x_norm**4)
        
        # Add cross-terms to create interactions between dimensions
        f5 = 0.01 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Shift global minimum to (0.5, 0.5, ..., 0.5) to increase challenge
        shift = np.full(self.dim, 0.5)
        f6 = 0.1 * np.sum((x_norm - shift)**2)
        
        # Combine all terms
        result = f1 + f2 + f3 + f4 + f5 + f6
        
        return result