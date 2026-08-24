import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function
        # Global minimum at origin, multiple local minima
        term1 = np.sum(x**2)
        term2 = 0.1 * np.sum(np.sin(5 * x))
        term3 = 0.01 * np.sum(x**4)
        
        # Add some interaction terms between dimensions
        interaction = 0.05 * np.sum(x[:-1] * x[1:])
        
        return term1 + term2 + term3 + interaction