import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Cubic basin term - global minimum at origin with steeper gradient
        basin = np.sum(x_norm**3)
        
        # Multimodal grid terms - multiple local minima in a grid pattern with exponential decay
        grid_terms = 0.0
        for i in range(self.dim):
            # Create exponentially decaying peaks in each dimension
            peak_term = np.exp(-2.0 * np.abs(x_norm[i])) * np.cos(3 * np.pi * x_norm[i]) * np.sin(2 * np.pi * x_norm[i])
            grid_terms += peak_term
            
        # Combine terms with different weights to create a challenging landscape
        return 8.0 * basin + 7.0 * grid_terms + 2.0