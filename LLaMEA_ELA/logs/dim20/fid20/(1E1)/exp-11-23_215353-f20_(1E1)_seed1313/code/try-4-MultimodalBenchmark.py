import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function
        # Global minimum at origin with multiple local minima
        term1 = np.sum(x**2) / self.dim
        term2 = np.sum(np.cos(2 * np.pi * x))
        term3 = np.prod(np.cos(x / np.sqrt(np.arange(1, self.dim + 1))))
        
        # Add a new term to increase complexity and avoid broadcasting issues
        term4 = np.sum(np.sin(0.5 * x) * np.exp(-x**2 / 10.0))
        
        # Combine terms to create a challenging landscape
        return term1 - 0.1 * term2 + 0.01 * term3 + 0.001 * term4 + 1.0