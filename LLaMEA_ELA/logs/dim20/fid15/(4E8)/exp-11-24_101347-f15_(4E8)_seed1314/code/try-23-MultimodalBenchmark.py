import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with varying frequencies and amplitudes
        frequencies = np.arange(1, self.dim + 1)
        amplitudes = 1.0 / (1.0 + 0.5 * frequencies)
        f2 = np.sum(amplitudes * np.sin(frequencies * np.pi * x_norm))
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        f3 = np.exp(-r) * np.cos(2 * np.pi * r)
        
        # Product term to create complex landscape with multiple basins
        f4 = np.prod(np.cos(0.5 * np.pi * x_norm) + 0.1 * np.sin(3 * np.pi * x_norm))
        
        # Combine all terms with different weights and add noise-like perturbations
        result = 0.8 * f1 + 0.3 * f2 + 0.4 * f3 + 0.6 * f4
        
        return result