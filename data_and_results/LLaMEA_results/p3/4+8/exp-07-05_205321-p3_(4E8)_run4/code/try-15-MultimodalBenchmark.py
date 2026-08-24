import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function with nested structure
        # Base quadratic term
        quadratic = np.sum(x**2) / self.dim
        
        # Sinusoidal modulations creating multiple local minima
        sinusoidal = np.sum(np.sin(3.0 * x)**2) / self.dim
        
        # Exponential decay term creating nested valleys
        exponential = np.exp(-0.1 * np.sum(np.abs(x)) / self.dim)
        
        # Additional saddle point term
        saddle = np.sum(x**4) / self.dim**2
        
        # Combine all terms with different weights
        result = 0.5 * quadratic + 0.3 * sinusoidal + 0.2 * exponential + 0.1 * saddle
        
        return result