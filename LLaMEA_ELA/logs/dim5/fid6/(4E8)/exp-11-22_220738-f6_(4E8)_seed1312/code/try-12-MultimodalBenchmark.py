import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_norm**2)
        
        # Enhanced sinusoidal terms with multiple local minima and interference patterns
        f2 = np.sum(np.sin(3 * np.pi * x_norm) ** 2 + 0.5 * np.sin(6 * np.pi * x_norm) ** 2)
        
        # Additional cubic terms for non-convexity with adaptive scaling
        f3 = np.sum(np.abs(x_norm)**3)
        
        # Add a Gaussian-like attractor term to create more complex landscape
        gaussian_term = np.exp(-np.sum(x_norm**2) / 2.0)
        
        # Combine terms with different weights to create a challenging landscape
        return f1 + 0.2 * f2 + 0.02 * f3 - 0.5 * gaussian_term