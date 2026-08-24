import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        # Global minimum at origin, multiple local minima
        term1 = np.sum(x**2) / self.dim
        term2 = np.sum(np.sin(5 * np.pi * x)**2)
        term3 = np.sum(np.exp(-0.5 * x**2) * np.cos(3 * np.pi * x))
        term4 = np.prod(np.sin(0.5 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Combine terms to create challenging landscape
        return term1 + 0.5 * term2 - 0.3 * term3 + 0.1 * term4 + 2.0