import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute grid points for global minima
        grid_points = np.linspace(-4.5, 4.5, 5)
        # Create all combinations of grid points
        self.global_minima = np.array(np.meshgrid(*[grid_points] * dim, indexing='ij')).T.reshape(-1, dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Quadratic basin term that makes the search space deceptive
        basin_term = 0.1 * np.sum((x - 2.5)**2)
        
        # Grid of global minima with varying heights
        minima_term = np.inf
        
        # Compute distances to all minima at once for efficiency
        distances = np.sqrt(np.sum((self.global_minima - x)**2, axis=1))
        
        # Find minimum distance and apply varying heights
        min_idx = np.argmin(distances)
        min_dist = distances[min_idx]
        
        # Varying heights for different minima based on position
        height = 0.5 * (min_idx % 3) + 1.0
        minima_term = min_dist * height
        
        # Add some noise to make it more challenging
        noise = 0.01 * np.sum(np.sin(x))
        
        return basin_term + minima_term + noise