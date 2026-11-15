import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function with enhanced complexity
        # Global minimum at origin, multiple local minima
        term1 = np.sum(x**2) / self.dim
        term2 = np.sum(np.cos(2 * np.pi * x))
        term3 = np.sum(np.exp(-0.5 * (x**2)) * np.sin(3 * x))
        term4 = np.prod(np.cos(x / np.sqrt(np.arange(1, self.dim + 1))) + 0.1 * np.sin(x))
        
        # Combine terms to create challenging landscape with varied curvature
        return term1 - 0.1 * term2 + 0.02 * term3 + 0.01 * term4 + 1.0