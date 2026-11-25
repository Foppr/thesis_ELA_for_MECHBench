import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        
        # Generate grid of global minima with shifted positions
        num_minima_per_dim = 3
        minima_positions = np.linspace(-4.0, 4.0, num_minima_per_dim)
        # Shift the grid by 0.5 in each dimension for complexity
        shifted_positions = minima_positions + 0.5 * np.sin(np.arange(num_minima_per_dim))
        
        # Create meshgrid and flatten for proper iteration
        grids = [shifted_positions] * dim
        mesh = np.meshgrid(*grids, indexing='ij')
        
        # Flatten and stack to create coordinate pairs
        flat_coords = [g.flatten() for g in mesh]
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
            # Add a Gaussian-like attraction to each minimum with varying amplitude
            amplitude = 1.0 + 0.3 * np.sin(i * 0.5)
            multimodal_term += np.exp(-dist / 1.5) * amplitude
        
        # Combine terms with different weights
        return basin_term + 0.7 * multimodal_term