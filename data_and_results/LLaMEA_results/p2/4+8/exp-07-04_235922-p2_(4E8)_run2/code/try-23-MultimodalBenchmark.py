import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced multimodal function with increased complexity
        result = np.sum(x**2) + 0.2 * np.sum(np.sin(7 * x)) + 0.02 * np.sum(x**6) + 0.1 * np.sum(np.cos(3 * x**2))
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result