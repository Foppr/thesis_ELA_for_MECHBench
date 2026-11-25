import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with multiple peaks
        r = np.sqrt(np.sum(x_norm**2))
        
        # Cosine-based periodic terms with varying frequencies and amplitudes
        cos_terms = np.sum(np.cos(2 * np.pi * (r + 0.1)) * np.cos(5 * np.pi * r) * 
                          (1 + 0.3 * np.sin(7 * np.pi * r)))
        
        # Asymmetric scaling in different dimensions
        asym_scale = np.sum((np.abs(x_norm) ** 1.5) * (1 + 0.2 * np.sin(np.arange(self.dim))))
        
        # Additional saddle-like structure
        saddle = np.sum(x_norm**2 * np.cos(3 * np.pi * x_norm))
        
        # Combine all terms with different weights
        return 2.0 * r**2 + 0.5 * cos_terms + 0.1 * asym_scale - 0.3 * saddle