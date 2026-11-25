import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Base quadratic term
        base_term = np.sum(x**2)
        
        # Add multiple global minima in a grid pattern
        grid_minima = 0.0
        for i in range(self.dim):
            # Create grid of minima at positions -4, -2, 0, 2, 4
            grid_positions = np.array([-4.0, -2.0, 0.0, 2.0, 4.0])
            distances = np.abs(x[i] - grid_positions)
            # Find minimum distance to any grid point
            min_distance = np.min(distances)
            # Add penalty based on distance to nearest grid minimum
            grid_minima += (min_distance ** 2) * np.exp(-0.1 * min_distance)
        
        # Add a few local minima around the center
        center_penalty = 0.0
        for i in range(self.dim):
            center_penalty += (x[i] - 1.0)**4 + (x[i] + 1.0)**4
        
        return base_term + 0.5 * grid_minima + 0.1 * center_penalty