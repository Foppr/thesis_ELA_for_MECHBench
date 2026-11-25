import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        
        # Generate grid of global minima
        num_minima_per_dim = 3
        minima_positions = np.linspace(-4.0, 4.0, num_minima_per_dim)
        grid_points = np.array(np.meshgrid(*[minima_positions] * dim, indexing='ij'))
        
        # Flatten and stack grid points correctly
        flat_points = grid_points.reshape(dim, -1).T
        for point in flat_points:
            self.global_minima.append(point)
        
        # Add central minimum
        self.global_minima.append(np.zeros(dim))
        self.global_minima = np.array(self.global_minima)

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
            # Modified Gaussian-like attraction with varying amplitudes
            amplitude = 1.0 + 0.3 * np.sin(i * 0.5)
            multimodal_term += amplitude * np.exp(-dist / 3.0) * (1.0 + 0.4 * np.cos(i * 0.3))
        
        # Add cosine interaction term between dimensions
        cos_interaction = np.sum(np.cos(0.5 * x), axis=1)
        
        # Combine terms with different weights
        return basin_term + 0.6 * multimodal_term + 0.2 * cos_interaction