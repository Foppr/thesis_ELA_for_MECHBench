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
        
        # Sum of sinusoidal terms with varying frequencies (multimodal landscape)
        f2 = np.sum(np.sin(3.0 * np.pi * x_norm)**4 + 0.5 * np.sin(6.0 * np.pi * x_norm)**4)
        
        # Product of cosine terms with polynomial decay (additional complexity)
        f3 = np.prod(np.cos(1.5 * np.pi * x_norm) * (1.0 + 0.1 * np.abs(x_norm)))
        
        # Polynomial correlation terms
        f4 = np.sum(x_norm**4)
        
        # Combine terms with different weights
        result = 0.3 * f1 + 0.4 * f2 + 0.2 * f3 + 0.1 * f4
        
        # Add a small constant to ensure the global minimum is not at exactly zero
        return result + 0.05 * np.sum(np.abs(x_norm))