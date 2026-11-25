import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Combine exponential decay terms with trigonometric peaks
        result = np.sum(np.exp(-x**2 / 2.0)) + 2.0 * np.sum(np.cos(3 * x) * np.sin(7 * x)) + 0.1 * np.sum(x**6)
        
        return result