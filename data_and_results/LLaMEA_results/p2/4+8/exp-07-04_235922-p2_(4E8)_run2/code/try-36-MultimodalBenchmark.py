import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced multimodal function with increased complexity
        result = np.sum(x**2) + 0.3 * np.sum(np.sin(5 * x)) + 0.01 * np.sum(x**6) + 0.15 * np.sum(np.cos(4 * x**2)) + 0.2 * np.sum(x**3 * np.sin(2 * x))
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result