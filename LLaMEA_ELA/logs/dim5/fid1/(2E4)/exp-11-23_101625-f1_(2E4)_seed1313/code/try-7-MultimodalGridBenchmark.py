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
            # Create periodic peaks in each dimension with varying frequencies
            peak_term = np.cos(3 * np.pi * x_norm[i]) * np.exp(-0.5 * (x_norm[i] - 0.3)**2) + \
                       0.5 * np.sin(4 * np.pi * x_norm[i]) * np.exp(-0.3 * (x_norm[i] + 0.4)**2)
            grid_terms += peak_term
            
        # Add cross-dimensional interaction terms for increased complexity
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.3 * np.sin(np.pi * (x_norm[i] + x_norm[j])) * np.exp(-0.2 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Combine terms with different weights to create a challenging landscape
        return 15.0 * basin + 8.0 * grid_terms + 3.0 * interaction + 2.0