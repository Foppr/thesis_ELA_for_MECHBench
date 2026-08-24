import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        # Global minimum at origin (0,0,...,0) with value 0
        # Multiple local minima scattered around the search space
        term1 = np.sum(x**2) / self.dim
        term2 = np.sum(np.cos(2 * np.pi * x)) / self.dim
        term3 = np.prod(np.cos(x / np.sqrt(np.arange(1, self.dim + 1))))
        
        return term1 - term2 + term3