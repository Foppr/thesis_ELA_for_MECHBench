import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute grid points for global minima
        grid_points = np.linspace(-4.5, 4.5, 5)
        self.global_minima = []
        # Create all combinations of grid points
        if dim == 1:
            for point in grid_points:
                self.global_minima.append([point])
        else:
            grid_mesh = np.meshgrid(*[grid_points] * dim, indexing='ij')
            for i in range(len(grid_mesh[0].flat)):
                coords = [grid_mesh[j].flat[i] for j in range(dim)]
                self.global_minima.append(coords)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Convert to numpy array for easier computation
        x = np.array(x)
        
        # Quadratic basin term that makes the search space deceptive
        basin_term = 0.1 * np.sum((x - 2.5)**2)
        
        # Grid of global minima with varying heights
        minima_term = float('inf')
        for i, min_point in enumerate(self.global_minima):
            dist = np.sqrt(np.sum((x - np.array(min_point))**2))
            # Varying heights for different minima
            height = 0.5 * (i % 3) + 1.0
            minima_term = min(minima_term, dist * height)
        
        # Add some noise to make it more challenging
        noise = 0.01 * np.sum(np.sin(x))
        
        return basin_term + minima_term + noise