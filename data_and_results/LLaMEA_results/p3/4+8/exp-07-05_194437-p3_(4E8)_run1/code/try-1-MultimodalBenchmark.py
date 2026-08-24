import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Sum of sine terms with different frequencies
        f2 = np.sum(np.sin(5 * np.pi * x_norm)**2)
        
        # Product of cosine terms creating multimodal structure
        f3 = np.prod(np.cos(2 * np.pi * x_norm) + 1)
        
        # Add a small noise term to make it non-trivial
        noise = 0.1 * np.random.random()
        
        # Combine terms with different weights
        result = 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + noise
        
        return result