import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function
        # Global minimum at origin with multiple local minima
        term1 = np.sum(x**2) / self.dim
        term2 = np.sum(np.sin(7 * np.pi * x)**2) / self.dim
        term3 = np.sum(x**4) / (self.dim * 100)
        term4 = np.sum(x[:-1] * x[1:]) / (self.dim - 1) if self.dim > 1 else 0
        
        return term1 + term2 + term3 + term4