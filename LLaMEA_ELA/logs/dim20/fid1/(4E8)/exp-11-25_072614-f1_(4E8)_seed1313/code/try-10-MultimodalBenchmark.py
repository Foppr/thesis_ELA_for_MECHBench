import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # High-dimensional multimodal function with chaotic interference
        result = np.sum(x**2) + 0.5 * np.sum(np.sin(10 * x)) + 0.3 * np.sum(np.cos(7 * x)) + \
                 0.1 * np.sum(np.sin(3 * x) * np.cos(5 * x)) + 0.05 * np.sum(x**6) + \
                 0.2 * np.sum(np.sin(x**3)) + 0.15 * np.sum(np.exp(-x**2) * np.sin(8 * x))
        
        return result