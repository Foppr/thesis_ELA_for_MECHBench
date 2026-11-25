import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Create a grid of local minima
        grid_size = 3
        grid_points = np.linspace(-4, 4, grid_size)
        
        # Calculate distance to all grid points
        distances = np.sqrt(np.sum((x[:, None] - grid_points[None, :])**2, axis=0))
        
        # Find minimum distance to any grid point
        min_distances = np.min(distances.reshape(-1, grid_size), axis=1)
        
        # Sum of distances to all grid points (penalize being far from grid)
        grid_penalty = np.sum(min_distances)
        
        # Add quadratic basin term to create a global minimum at origin
        basin_term = 0.1 * np.sum(x**2)
        
        # Add enhanced sine modulation with multiple frequencies to create additional local optima
        sine_term = 0.3 * np.sum(np.sin(0.3 * x) ** 2 + 0.7 * np.sin(1.5 * x) ** 2)
        
        # Add Gaussian noise term to increase landscape complexity
        noise_term = 0.05 * np.sum(np.exp(-0.1 * (x**2)))
        
        return grid_penalty + basin_term + sine_term + noise_term