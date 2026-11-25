import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Grid of global minima locations
        grid_size = 3
        minima_positions = np.linspace(-4.5, 4.5, grid_size)
        grid_points = np.array(np.meshgrid(minima_positions, minima_positions, indexing='ij')).T.reshape(-1, 2)
        
        # Add extra dimensions with zero contribution for higher dimensions
        if self.dim > 2:
            grid_points = np.hstack([grid_points, np.zeros((grid_points.shape[0], self.dim - 2))])
        
        # Calculate distance to nearest minimum
        distances = np.sqrt(np.sum((x - grid_points)**2, axis=1))
        min_distance = np.min(distances)
        
        # Base function with quadratic basin
        quadratic_term = 0.1 * np.sum(x**2)
        
        # Add penalty for being far from minima
        penalty = 10 * np.exp(-min_distance**2 / 2.0)
        
        return quadratic_term + penalty