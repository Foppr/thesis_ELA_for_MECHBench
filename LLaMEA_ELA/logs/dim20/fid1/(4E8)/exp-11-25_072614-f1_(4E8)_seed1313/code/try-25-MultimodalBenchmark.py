import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # High-dimensional multimodal function with enhanced chaotic interference
        result = np.sum(x**2) + 0.8 * np.sum(np.sin(12 * x)) + 0.6 * np.sum(np.cos(9 * x)) + \
                 0.4 * np.sum(np.sin(5 * x) * np.cos(8 * x)) + 0.2 * np.sum(x**6) + \
                 0.3 * np.sum(np.sin(x**3)) + 0.25 * np.sum(np.exp(-x**2) * np.sin(10 * x)) + \
                 0.1 * np.sum(np.sin(4 * x) * np.cos(6 * x) * np.sin(2 * x)) + \
                 0.15 * np.sum(np.abs(x) * np.sin(3 * x**2))
        
        return result