import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima
        grid_size = 3
        minima_positions = np.linspace(-4.0, 4.0, grid_size)
        for i in range(grid_size):
            for j in range(grid_size):
                if self.dim >= 2:
                    self.global_minima.append([minima_positions[i], minima_positions[j]] + [0.0] * (self.dim - 2))
        
        self.global_minima = np.array(self.global_minima)
        self.global_minima = self.global_minima[:min(9, len(self.global_minima))]  # Limit to 9 minima max

    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match initialized dimension")
        
        # Calculate distance to each global minimum
        distances = np.sqrt(np.sum((self.global_minima - x)**2, axis=1))
        
        # Find the minimum distance
        min_distance = np.min(distances)
        
        # Add a parabolic basin that deceives the optimizer
        basin_term = 0.1 * np.sum(x**2)
        
        # Add a sine modulation to create additional complexity
        sine_term = 0.5 * np.sin(0.5 * np.sum(x))
        
        # Combine terms
        return min_distance + basin_term + sine_term