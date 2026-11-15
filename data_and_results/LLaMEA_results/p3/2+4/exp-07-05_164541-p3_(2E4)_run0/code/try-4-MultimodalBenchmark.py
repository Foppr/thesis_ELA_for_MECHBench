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
        term3 = np.prod(np.cos(x / np.sqrt(np.arange(1, self.dim + 1))))
        term4 = 0.1 * np.sum(np.sin(0.5 * x**2))
        term5 = 0.05 * np.sum(np.abs(x) ** 1.5)
        
        # Combine terms to create challenging landscape
        return term1 - 0.1 * term2 + 0.01 * term3 + term4 + term5 + 1.0