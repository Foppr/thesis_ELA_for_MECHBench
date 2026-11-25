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
        term2 = np.sum(np.cos(3 * np.pi * x))
        # Use log-sum-exp trick to avoid numerical issues in product
        term3 = np.exp(np.sum(np.log(np.abs(np.sin(x)) + 1e-10)) / self.dim)
        
        # Combine terms to create a challenging landscape
        return term1 - 0.15 * term2 + 0.02 * term3 + 1.0