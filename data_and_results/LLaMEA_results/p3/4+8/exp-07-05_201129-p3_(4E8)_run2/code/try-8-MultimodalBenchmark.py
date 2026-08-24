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
        
        # Sum of sinusoidal terms (multimodal landscape) with increased frequency and amplitude
        f2 = np.sum((np.sin(7.0 * np.pi * x_norm))**4)
        
        # Product of cosine terms with different frequency (additional complexity)
        f3 = np.prod(np.cos(3.0 * np.pi * x_norm))
        
        # Add a small quadratic shift to move the global minimum away from origin
        shift = 0.1 * np.sum((x_norm - 0.2)**2)
        
        # Combine terms with different weights
        result = 0.4 * f1 + 0.35 * f2 + 0.25 * f3 + shift
        
        return result