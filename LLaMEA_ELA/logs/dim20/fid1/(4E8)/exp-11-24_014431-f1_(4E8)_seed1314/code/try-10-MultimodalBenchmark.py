import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function
        # Modified combination of polynomial and trigonometric terms
        result = np.sum(x**2) + 0.15 * np.sum(np.sin(7 * x)) + 0.02 * np.sum(x**4) + 0.05 * np.sum(np.cos(3 * x))
        
        return result