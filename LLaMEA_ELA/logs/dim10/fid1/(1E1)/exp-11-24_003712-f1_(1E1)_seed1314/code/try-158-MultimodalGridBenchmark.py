import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        
        # Generate grid of global minima
        num_minima_per_dim = 3
        minima_positions = np.linspace(-4.0, 4.0, num_minima_per_dim)
        
        # Create all combinations properly
        grid_points = np.array(np.meshgrid(*[minima_positions] * dim, indexing='ij'))
        grid_points = grid_points.reshape(dim, -1).T
        
        # Add central minimum
        center_point = np.zeros(dim)
        
        # Combine all minima
        self.global_minima = np.vstack([grid_points, center_point])
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Quadratic basin term
        basin_term = 0.1 * np.sum(x**2, axis=1)
        
        # Multimodal term with multiple global minima
        multimodal_term = np.zeros(x.shape[0])
        
        for i in range(len(self.global_minima)):
            center = self.global_minima[i]
            dist = np.sum((x - center)**2, axis=1)
            # Add a Gaussian-like attraction to each minimum
            multimodal_term += np.exp(-dist / 2.0) * (1.0 + 0.5 * np.sin(i))
        
        # Combine terms with different weights
        return basin_term + 0.5 * multimodal_term