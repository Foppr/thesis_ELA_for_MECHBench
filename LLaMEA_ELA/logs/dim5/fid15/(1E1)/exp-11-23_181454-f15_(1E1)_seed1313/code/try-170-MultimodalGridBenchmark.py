import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima
        grid_points = np.linspace(-4.5, 4.5, 5)
        for point in np.nditer(np.meshgrid(*[grid_points] * dim, indexing='ij')):
            self.global_minima.append(list(point))
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Quadratic basin term that makes the search space deceptive
        basin_term = 0.1 * np.sum((x - 2.5)**2)
        
        # Grid of global minima with varying heights
        minima_term = float('inf')
        for i, min_point in enumerate(self.global_minima):
            # Calculate distance properly for all dimensions
            dist = np.sqrt(sum((x[j] - min_point[j])**2 for j in range(self.dim)))
            # Use fixed height values to avoid complex calculations
            height = 1.0 if i % 3 == 0 else (1.5 if i % 3 == 1 else 2.0)
            contribution = dist * height
            if contribution < minima_term:
                minima_term = contribution
        
        # Add some noise to make it more challenging
        noise = 0.01 * np.sum(np.sin(x))
        
        return basin_term + minima_term + noise