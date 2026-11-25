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
        term2 = np.sum(np.cos(3 * np.pi * shifted_x)) / self.dim
        term3 = np.sum(shifted_x**4) / (4 * self.dim)
        term4 = 0.5 * np.sum(np.sin(1.5 * np.pi * shifted_x)) / self.dim
        
        # Add multiple local minima by combining different functions
        result = term1 - term2 + term3 + term4
        
        return float(result)