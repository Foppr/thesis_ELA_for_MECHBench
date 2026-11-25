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
        term2 = 20 * np.exp(-0.3 * np.sum((x - 1)**2))
        term3 = 15 * np.exp(-0.15 * np.sum((x + 1)**2))
        term4 = 12 * np.exp(-0.08 * np.sum((x - 2)**2))
        term5 = 10 * np.exp(-0.04 * np.sum((x + 2)**2))
        term6 = 8 * np.exp(-0.02 * np.sum((x - 3)**2))
        term7 = 6 * np.exp(-0.01 * np.sum((x + 3)**2))
        term8 = 4 * np.exp(-0.005 * np.sum((x - 4)**2))
        term9 = 2 * np.exp(-0.002 * np.sum((x + 4)**2))
        
        return term1 + term2 + term3 + term4 + term5 + term6 + term7 + term8 + term9 - 60