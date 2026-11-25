import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-5, 5] domain
        x = np.array(x)
        
        # Shift variables to center the function
        shifted_x = x - 1.0
        
        # Compute multiple sinusoidal components with different frequencies
        term1 = np.sum(shifted_x**2) / self.dim
        term2 = np.sum(np.cos(4 * np.pi * shifted_x)) / self.dim
        term3 = np.sum(shifted_x**5) / (5 * self.dim)
        term4 = 0.7 * np.sum(np.sin(2.0 * np.pi * shifted_x)) / self.dim
        
        # Add interaction terms between dimensions
        interaction = 0.1 * np.sum(shifted_x[:-1] * shifted_x[1:]) / (self.dim - 1) if self.dim > 1 else 0
        
        # Add multiple local minima by combining different functions
        result = term1 - term2 + term3 + term4 + interaction
        
        return float(result)