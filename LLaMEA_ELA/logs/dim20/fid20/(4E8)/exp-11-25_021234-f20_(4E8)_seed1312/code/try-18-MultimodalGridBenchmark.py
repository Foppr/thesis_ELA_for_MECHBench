import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Create grid of global minima at positions (±2, ±2, ±2, ...)
        grid_minima = []
        for i in range(self.dim):
            if i % 2 == 0:
                grid_minima.append([-2, 2])
            else:
                grid_minima.append([-2, 2])
        
        # Calculate distance to nearest grid minimum
        min_dist = float('inf')
        for i in range(len(grid_minima)):
            for j in range(len(grid_minima[i])):
                if i < len(x):
                    dist = abs(x[i] - grid_minima[i][j])
                    if dist < min_dist:
                        min_dist = dist
        
        # Add deceptive quadratic basin term that pulls towards origin
        basin_term = 0.1 * np.sum(x**2)
        
        # Combine terms with a scaling factor
        return min_dist + basin_term