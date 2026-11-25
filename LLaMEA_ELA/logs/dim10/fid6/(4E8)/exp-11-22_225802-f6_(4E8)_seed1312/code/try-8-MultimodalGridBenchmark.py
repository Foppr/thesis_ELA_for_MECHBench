import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima
        grid_points = 5
        x_vals = np.linspace(-4.0, 4.0, grid_points)
        for i in range(grid_points):
            for j in range(grid_points):
                if i == 0 and j == 0:
                    continue  # Skip the center point which will be handled separately
                min_point = [x_vals[i], x_vals[j]] + [0.0] * (dim - 2) if dim > 2 else [x_vals[i], x_vals[j]]
                self.global_minima.append(np.array(min_point))
        
        # Add central valley minimum
        self.global_minima.append(np.zeros(dim))
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Central valley function (low values in center)
        valley_term = 0.1 * np.sum(x**2)
        
        # Global minima terms (high values at global minima locations)
        minima_term = 0.0
        for min_point in self.global_minima:
            dist = np.sum((x - min_point)**2)
            # Use a Gaussian-like function centered at each minimum
            minima_term += np.exp(-dist / 0.5)
        
        # Combine terms with different weights to create challenging landscape
        return valley_term + 10 * (1 - minima_term) + 0.01 * np.sum(np.abs(x))