import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima
        grid_points = np.linspace(-4.5, 4.5, 5)
        # Create meshgrid properly for all dimensions
        if self.dim == 1:
            self.global_minima = [[x] for x in grid_points]
        else:
            mesh = np.meshgrid(*[grid_points] * self.dim, indexing='ij')
            self.global_minima = [list(point.flatten()) for point in zip(*[m.ravel() for m in mesh])]
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Quadratic basin term that makes the search space deceptive
        basin_term = 0.1 * np.sum((x - 2.5)**2)
        
        # Grid of global minima with varying heights
        minima_term = float('inf')
        for i, minimum in enumerate(self.global_minima):
            dist = np.sqrt(np.sum((np.array(x) - np.array(minimum))**2))
            # Varying heights for different minima
            height = 0.5 * (i % 3) + 1.0
            minima_term = min(minima_term, dist * height)
        
        # Add some noise to make it more challenging
        noise = 0.01 * np.sum(np.sin(x))
        
        return basin_term + minima_term + noise