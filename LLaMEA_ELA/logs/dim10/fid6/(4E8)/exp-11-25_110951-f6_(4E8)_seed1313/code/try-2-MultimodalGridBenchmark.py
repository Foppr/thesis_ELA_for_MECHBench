import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic basin term - global minimum at origin
        basin = np.sum(x_norm**2)
        
        # Multimodal grid terms - create multiple local minima in a grid pattern
        grid_terms = 0.0
        for i in range(self.dim):
            # Create grid of local minima along each dimension
            grid_terms += 10 * np.sin(2 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i])
        
        # Additional harmonic terms to increase complexity
        harmonic_terms = 0.0
        for i in range(self.dim):
            harmonic_terms += 5 * np.sin(4 * np.pi * x_norm[i])**2
        
        return basin + grid_terms + harmonic_terms