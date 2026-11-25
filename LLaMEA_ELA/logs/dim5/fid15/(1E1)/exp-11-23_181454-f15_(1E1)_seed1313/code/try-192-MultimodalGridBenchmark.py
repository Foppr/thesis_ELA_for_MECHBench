import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima
        grid_points = np.linspace(-4.5, 4.5, 5)
        # Create all combinations of grid points for each dimension
        grid_combinations = np.array(np.meshgrid(*[grid_points] * dim, indexing='ij')).T
        # Flatten and store as list of lists
        for combo in grid_combinations.reshape(-1, dim):
            self.global_minima.append(combo.tolist())
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Quadratic basin term that makes the search space deceptive
        basin_term = 0.1 * np.sum((x - 2.5)**2)
        
        # Grid of global minima with varying heights
        minima_term = float('inf')
        for min_point in self.global_minima:
            dist = np.sqrt(np.sum((np.array(x) - np.array(min_point))**2))
            # Varying heights for different minima based on position
            height = 0.5 * (self.global_minima.index(min_point) % 3) + 1.0
            if dist < minima_term:
                minima_term = dist * height
        
        # Add some noise to make it more challenging
        noise = 0.01 * np.sum(np.sin(x))
        
        return basin_term + minima_term + noise