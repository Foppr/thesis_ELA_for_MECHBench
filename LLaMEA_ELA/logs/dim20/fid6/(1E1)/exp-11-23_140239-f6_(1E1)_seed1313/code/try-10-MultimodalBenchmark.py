import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the highly multimodal function
        # Global minimum at origin with exponentially increasing local minima
        term1 = np.sum(x**2) / self.dim
        term2 = 20 * np.exp(-0.3 * np.sum((x - 1.5)**2))
        term3 = 12 * np.exp(-0.15 * np.sum((x + 1.5)**2))
        term4 = 8 * np.exp(-0.08 * np.sum((x - 2.5)**2))
        term5 = 10 * np.exp(-0.03 * np.sum((x + 2.5)**2))
        term6 = 4 * np.exp(-0.015 * np.sum((x - 3.5)**2))
        term7 = 7 * np.exp(-0.008 * np.sum((x + 3.5)**2))
        
        return term1 + term2 + term3 + term4 + term5 + term6 + term7 - 60