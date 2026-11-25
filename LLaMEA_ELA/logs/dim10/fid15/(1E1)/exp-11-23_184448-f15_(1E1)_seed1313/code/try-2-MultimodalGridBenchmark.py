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
            # Add penalty based on distance to nearest grid minimum with exponential decay
            grid_minima += (min_distance ** 2) * np.exp(-0.2 * min_distance)
        
        # Add sinusoidal oscillations around the center to increase complexity
        oscillation_term = 0.0
        for i in range(self.dim):
            oscillation_term += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Add a strong central attraction with quartic penalty
        center_penalty = 0.0
        for i in range(self.dim):
            center_penalty += (x[i] - 1.0)**4 + (x[i] + 1.0)**4
        
        return base_term + 0.5 * grid_minima + 0.3 * oscillation_term + 0.1 * center_penalty