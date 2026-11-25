import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # High-dimensional multimodal function with exponential oscillations
        result = np.sum(x**2) + 0.5 * np.sum(np.exp(2 * np.sin(10 * x))) + 0.001 * np.sum(x**6) + 0.3 * np.sum(np.cos(15 * x))
        
        return result