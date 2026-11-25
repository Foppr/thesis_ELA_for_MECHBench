import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        
        # Generate grid of global minima with shifted positions
        num_minima_per_dim = 3
        minima_positions = np.linspace(-4.5, 4.5, num_minima_per_dim)
        # Create meshgrid for all dimensions
        grids = [minima_positions] * dim
        mesh = np.meshgrid(*grids, indexing='ij')
        
        # Flatten and stack the meshgrid arrays to create coordinate combinations
        flat_coords = [np.ravel(grid) for grid in mesh]
        self.global_minima = np.column_stack(flat_coords)
        
        # Add central minimum
        self.global_minima = np.vstack([self.global_minima, np.zeros(dim)])
        
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
            # Add a Gaussian-like attraction to each minimum with modified frequency
            multimodal_term += np.exp(-dist / 1.5) * (1.0 + 0.3 * np.sin(i * 1.7))
        
        # Combine terms with different weights
        return basin_term + 0.4 * multimodal_term