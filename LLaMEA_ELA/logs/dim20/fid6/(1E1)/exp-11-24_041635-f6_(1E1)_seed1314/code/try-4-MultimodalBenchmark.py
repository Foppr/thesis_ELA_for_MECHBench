import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Mutated multimodal function with altered coefficients and added cubic terms
        result = np.sum(x**2) + 0.3 * np.sum(np.sin(12.0 * x)) + 0.4 * np.sum(np.exp(0.3 * np.abs(x))) + 0.03 * np.sum(x**3) + 0.05 * np.sum(x**6)
        
        return result