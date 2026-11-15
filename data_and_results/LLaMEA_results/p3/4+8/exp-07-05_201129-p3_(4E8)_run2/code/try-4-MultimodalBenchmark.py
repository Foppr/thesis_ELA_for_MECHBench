import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms (central valley)
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms (multimodal landscape)
        f2 = np.sum(np.sin(5.0 * np.pi * x_norm)**6)
        
        # Product of cosine terms (additional complexity)
        f3 = np.prod(np.cos(2.0 * np.pi * x_norm))
        
        # Combine terms with different weights
        result = 0.5 * f1 + 0.3 * f2 + 0.2 * f3
        
        # Add a small constant to ensure the global minimum is not at exactly zero
        return result + 0.1 * np.sum(np.abs(x_norm))