import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        # Global minimum at origin with multiple local minima
        term1 = np.sum(x**2)
        term2 = np.sum(np.sin(np.sqrt(np.abs(x)))**2)
        term3 = 0.1 * np.sum(x**4)
        
        # Add some correlation between dimensions
        correlation = np.sum(x[:-1] * x[1:]) * 0.01
        
        return term1 + term2 + term3 + correlation