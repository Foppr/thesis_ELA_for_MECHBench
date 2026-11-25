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
        term2 = 10 * np.exp(-0.1 * np.sum((x - 1)**2))
        term3 = 5 * np.exp(-0.05 * np.sum((x + 1)**2))
        
        return term1 + term2 + term3 - 15