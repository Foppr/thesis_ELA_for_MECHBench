import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Quadratic basin term - global minimum at origin
        basin = np.sum(x_norm**2)
        
        # Multimodal grid terms - multiple local minima in a grid pattern
        grid_terms = 0.0
        for i in range(self.dim):
            # Create periodic peaks in each dimension
            peak_term = np.cos(2 * np.pi * x_norm[i]) * np.exp(-0.5 * (x_norm[i] - 0.5)**2)
            grid_terms += peak_term
            
        # Combine terms with different weights to create a challenging landscape
        return 10.0 * basin + 5.0 * grid_terms + 1.0