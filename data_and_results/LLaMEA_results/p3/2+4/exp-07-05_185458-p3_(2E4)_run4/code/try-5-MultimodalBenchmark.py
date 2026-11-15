import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        # Combines quadratic, sinusoidal, and exponential components with modified parameters
        term1 = np.sum(x**2) / self.dim
        term2 = np.sum(np.sin(7.0 * np.pi * x)**2) / self.dim
        term3 = np.exp(-0.3 * np.sum(x**2) / self.dim)
        term4 = 0.1 * np.sum(x**4) / self.dim  # Added quartic term for increased complexity
        
        # Combine terms with different weights
        result = term1 + 0.7 * term2 + 0.15 * term3 + 0.05 * term4
        
        return result