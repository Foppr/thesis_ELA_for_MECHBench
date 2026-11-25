import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate global minima points in a grid pattern
        num_per_dim = 3
        grid_points = np.linspace(-4.0, 4.0, num_per_dim)
        for point in np.nditer(np.meshgrid(*[grid_points] * dim, indexing='ij')):
            self.global_minima.append(np.array(point).flatten())
        
    def f(self, x):
        # Validate input dimension
        if len(x) != self.dim:
            raise ValueError(f"Input dimension {len(x)} does not match expected dimension {self.dim}")
            
        # Base quadratic term
        base = np.sum(x**2)
        
        # Add multiple global minima with different basins
        minima_penalty = 0.0
        for min_point in self.global_minima:
            distance = np.sum((x - min_point)**2)
            # Create a penalty that decreases with distance from global minimum
            minima_penalty += 1.0 / (1.0 + distance * 0.5)
        
        # Add a deceptive quadratic basin term
        basin_term = 0.1 * np.sum((x - 2.0)**2)
        
        return base + minima_penalty - basin_term