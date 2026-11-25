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
        term2 = 15 * np.exp(-0.2 * np.sum((x - 1)**2))
        term3 = 10 * np.exp(-0.1 * np.sum((x + 1)**2))
        term4 = 5 * np.exp(-0.05 * np.sum((x - 2)**2))
        term5 = 8 * np.exp(-0.02 * np.sum((x + 2)**2))
        term6 = 3 * np.exp(-0.01 * np.sum((x - 3)**2))
        term7 = 6 * np.exp(-0.005 * np.sum((x + 3)**2))
        
        return term1 + term2 + term3 + term4 + term5 + term6 + term7 - 50