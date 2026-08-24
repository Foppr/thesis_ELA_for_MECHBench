import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function
        # Combines quadratic, sinusoidal, and exponential terms
        term1 = np.sum(x**2) / self.dim
        term2 = np.sum(np.sin(5.0 * np.pi * x)**2) / self.dim
        term3 = np.exp(-0.5 * np.sum(x**2) / self.dim)
        
        # Combine terms with different weights
        result = term1 + 0.5 * term2 + 0.1 * term3
        
        return result