import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Precompute global minima positions for 2D case (extendable to higher dimensions)
        if dim == 2:
            # Create a 3x3 grid of global minima
            grid_positions = np.linspace(-4.0, 4.0, 3)
            for x in grid_positions:
                for y in grid_positions:
                    self.global_minima.append([x, y])
        else:
            # For higher dimensions, create a simple grid structure
            grid_positions = np.linspace(-4.0, 4.0, 3)
            self.global_minima = []
            # Generate all combinations of grid positions
            from itertools import product
            for combo in product(grid_positions, repeat=dim):
                self.global_minima.append(list(combo))
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Normalize to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Base quadratic term (creates a bowl shape)
        base_term = np.sum(x_norm**2)
        
        # Add multiple local minima terms
        penalty = 0.0
        for min_pos in self.global_minima:
            dist = np.sum((x_norm - np.array(min_pos)/5.0)**2)
            penalty += np.exp(-dist * 10) * 0.5  # Scale down the contribution
            
        # Add a sinusoidal component to increase complexity
        sin_term = np.sin(3 * np.sum(x_norm)) * 0.3
        
        return base_term + penalty + sin_term