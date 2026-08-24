import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Create a highly multimodal landscape with exponential terms
        term1 = np.sum(x**2) / self.dim
        term2 = np.sum(np.sin(5 * np.pi * x)**2)
        term3 = np.sum(np.exp(-x**2) * np.sin(10 * np.pi * x))
        term4 = np.prod(np.sin(np.pi * x / 2.0) + 0.1 * np.cos(10 * np.pi * x))
        term5 = np.sum(np.log(1 + x**2) * np.sin(3 * np.pi * x))
        
        # Combine terms with varying weights to create complex landscape
        return term1 + 0.5 * term2 + 0.3 * term3 + 0.2 * term4 + 0.1 * term5 + 2.0