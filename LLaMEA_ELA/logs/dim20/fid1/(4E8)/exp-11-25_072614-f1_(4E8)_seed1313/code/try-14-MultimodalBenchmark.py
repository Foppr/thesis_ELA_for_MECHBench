import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function with enhanced complexity
        term1 = np.sum(x**2) / self.dim
        term2 = np.sum(np.sin(5 * np.pi * x)**4) / self.dim
        term3 = np.sum(x**6) / (self.dim * 1000)
        term4 = np.sum(np.cos(3 * np.pi * x) * np.sin(7 * np.pi * x)) / self.dim
        term5 = np.sum((x**2 + x**4) / (self.dim * 10))
        
        return term1 + term2 + term3 + term4 + term5