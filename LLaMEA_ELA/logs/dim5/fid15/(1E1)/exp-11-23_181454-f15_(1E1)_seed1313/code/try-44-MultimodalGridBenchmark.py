import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima
        grid_points = np.linspace(-4.5, 4.5, 5)
        minima_coords = np.array(np.meshgrid(*[grid_points] * dim, indexing='ij'))
        for i in range(minima_coords.shape[1]):
            coords = [minima_coords[j, i] for j in range(dim)]
            self.global_minima.append(coords)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Quadratic basin term that makes the search space deceptive
        basin_term = 0.1 * np.sum((x - 2.5)**2)
        
        # Grid of global minima with varying heights
        minima_term = float('inf')
        for i, coords in enumerate(self.global_minima):
            dist = np.sqrt(sum((x[j] - coords[j])**2 for j in range(self.dim)))
            # Varying heights for different minima
            height = 0.5 * (i % 3) + 1.0
            if dist < minima_term:
                minima_term = dist * height
        
        # Add some noise to make it more challenging
        noise = 0.01 * np.sum(np.sin(x))
        
        return basin_term + minima_term + noise