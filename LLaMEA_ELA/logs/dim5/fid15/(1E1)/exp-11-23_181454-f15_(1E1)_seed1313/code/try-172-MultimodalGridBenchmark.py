import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima with shift
        grid_points = np.linspace(-4.0, 4.0, 5)
        for point in np.nditer(np.meshgrid(*[grid_points] * dim, indexing='ij')):
            self.global_minima.append(point.tolist())
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Quadratic basin term that makes the search space deceptive
        basin_term = 0.2 * np.sum((x + 1.5)**2)
        
        # Grid of global minima with varying heights and shifted positions
        minima_term = float('inf')
        for i, min_point in enumerate(self.global_minima):
            dist = np.sum((x - np.array(min_point))**2)
            # Varying heights for different minima
            height = 0.3 * (i % 4) + 1.2
            if dist < minima_term:
                minima_term = dist * height
        
        # Add some noise to make it more challenging
        noise = 0.02 * np.sum(np.cos(2 * x))
        
        return basin_term + minima_term + noise