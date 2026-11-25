import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function with improved structure
        # Global minimum at origin with multiple local minima
        term1 = np.sum(x**2) / self.dim
        term2 = 15 * np.exp(-0.2 * np.sum((x - 1)**2))
        term3 = 7.5 * np.exp(-0.1 * np.sum((x + 1)**2))
        term4 = 5 * np.sin(0.5 * np.sum(x**2))
        term5 = 2.5 * np.cos(0.3 * np.sum(x**2))
        
        return term1 + term2 + term3 + term4 + term5 - 25