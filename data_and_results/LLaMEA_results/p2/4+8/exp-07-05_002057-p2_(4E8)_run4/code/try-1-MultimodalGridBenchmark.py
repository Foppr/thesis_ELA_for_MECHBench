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
                if i == 0 and j == 0:
                    continue  # Skip the center point which will be the basin
                self.global_minima.append([minima_positions[i], minima_positions[j]])
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension does not match the function dimension")
        
        # Quadratic basin term (global minimum at origin)
        basin = np.sum(x**2) * 0.1
        
        # Multimodal terms (global minima at grid points)
        multimodal = 0.0
        for min_pos in self.global_minima:
            if len(min_pos) == self.dim:
                dist = np.sum((x - np.array(min_pos))**2)
                multimodal += 10.0 * np.exp(-dist / 2.0)
        
        # Add some noise to make it more challenging
        noise = 0.1 * np.random.random()
        
        return basin + multimodal + noise