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
        minima_term = float('inf')
        for i, gm in enumerate(self.global_minima):
            dist = np.linalg.norm(x - gm)
            # Varying heights for different minima
            height = 0.5 * (i % 3) + 1.0
            if dist < minima_term:
                minima_term = dist * height
        
        # Add some noise to make it more challenging
        noise = 0.01 * np.sum(np.sin(x))
        
        return basin_term + minima_term + noise