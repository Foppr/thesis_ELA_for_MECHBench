import numpy as np

class MultimodalHexGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Define hexagonal grid parameters
        self.grid_spacing = 2.0
        self.grid_radius = 1.0
        # Generate hexagonal grid of global minima
        self.global_minima = []
        # Hexagonal grid points in 2D
        if self.dim >= 2:
            # Generate points in hexagonal pattern
            rows = 3
            cols = 3
            for i in range(rows):
                for j in range(cols):
                    # Offset every other row
                    x = (j + 0.5 * (i % 2)) * self.grid_spacing - (cols - 1) * self.grid_spacing / 2
                    y = i * self.grid_spacing * np.sqrt(3) / 2 - (rows - 1) * self.grid_spacing * np.sqrt(3) / 4
                    self.global_minima.append([x, y] + [0.0] * (self.dim - 2))
        
        self.global_minima = np.array(self.global_minima)
        # Ensure we're within bounds
        self.global_minima = self.global_minima[
            np.all((self.global_minima >= -5.0) & (self.global_minima <= 5.0), axis=1)
        ]

    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match initialized dimension")
        
        # Calculate distance to each global minimum
        distances = np.sqrt(np.sum((self.global_minima - x)**2, axis=1))
        
        # Find the minimum distance
        min_distance = np.min(distances)
        
        # Add a rugged landscape with multiple local minima
        rugged_term = 0.0
        for i in range(self.dim):
            rugged_term += 0.1 * np.sin(2 * np.pi * x[i] / self.grid_spacing) * np.cos(3 * np.pi * x[i] / self.grid_spacing)
        
        # Add a periodic modulation to increase complexity
        periodic_term = 0.2 * np.sin(0.5 * np.sum(x)) * np.cos(0.3 * np.sum(x))
        
        # Add a quadratic basin term to create a deceptive landscape
        basin_term = 0.05 * np.sum(x**2)
        
        # Combine all terms
        return min_distance + rugged_term + periodic_term + basin_term