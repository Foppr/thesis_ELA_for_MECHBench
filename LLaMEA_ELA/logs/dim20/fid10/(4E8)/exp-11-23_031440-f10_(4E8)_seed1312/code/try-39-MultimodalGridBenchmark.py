import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for easier computation
        x_norm = x / 5.0
        
        # Create a grid of global minima at positions that are multiples of 0.5
        grid_positions = np.arange(-1, 1.1, 0.5)
        
        # Calculate distance to nearest grid point for each dimension
        distances = np.zeros_like(x_norm)
        for i in range(self.dim):
            # Find minimum distance to any grid point in that dimension
            min_dist = np.min(np.abs(x_norm[i] - grid_positions))
            distances[i] = min_dist
        
        # Base quadratic term that creates a basin around the origin
        quadratic_term = 0.1 * np.sum(x_norm**2)
        
        # Add multiple local minima using enhanced sinusoidal terms with varying frequencies
        sine_term = 0.1 * np.sum(np.sin(5 * np.pi * x_norm) ** 2 + 0.5 * np.sin(10 * np.pi * x_norm) ** 2)
        
        # Add a penalty for being far from the grid points to encourage convergence
        grid_penalty = 15 * np.sum(distances**3)
        
        # Add a complex interaction term between dimensions to increase conditioning
        interaction_term = 0.05 * np.sum((x_norm[:-1] - x_norm[1:])**4)
        
        # Add a new term that creates additional complexity with higher-order interactions
        high_order_term = 0.2 * np.sum(np.sin(3 * np.pi * x_norm) ** 4 + np.cos(7 * np.pi * x_norm) ** 4)
        
        # Add a radial component to create nested basins of varying depths
        radial_term = 0.15 * (np.sum(x_norm**2) ** 1.5)
        
        # Combine all terms
        result = quadratic_term + sine_term + grid_penalty + interaction_term + high_order_term + radial_term
        
        return result