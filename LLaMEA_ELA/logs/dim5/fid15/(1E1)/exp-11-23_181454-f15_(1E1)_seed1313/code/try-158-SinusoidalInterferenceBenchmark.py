import numpy as np

class SinusoidalInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Define positions of global minima in a structured pattern
        self.global_minima_positions = []
        grid_size = max(2, int(np.ceil(np.sqrt(self.dim))))
        for i in range(grid_size):
            for j in range(grid_size):
                if len(self.global_minima_positions) < self.dim:
                    self.global_minima_positions.append([(-4.0 + 8.0 * i / (grid_size - 1)), (-4.0 + 8.0 * j / (grid_size - 1))])
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Quadratic radial penalty to guide search towards feasible region
        radial_penalty = 0.5 * np.sum((x / 5.0)**2)
        
        # Global minima with sinusoidal interference terms
        min_value = float('inf')
        for i, pos in enumerate(self.global_minima_positions):
            if i >= self.dim:
                break
            # Base distance to global minimum
            dist = np.sqrt(np.sum((x - np.array(pos))**2))
            
            # Add sinusoidal interference that creates local minima around each global optimum
            interference = 2.0 * np.sin(3.0 * dist) * np.cos(2.0 * dist)
            
            # Combine with base distance and interference
            total_value = dist + interference
            
            if total_value < min_value:
                min_value = total_value
        
        # Add a small random noise term to increase robustness
        noise = 0.01 * np.sum(np.sin(x))
        
        return radial_penalty + min_value + noise