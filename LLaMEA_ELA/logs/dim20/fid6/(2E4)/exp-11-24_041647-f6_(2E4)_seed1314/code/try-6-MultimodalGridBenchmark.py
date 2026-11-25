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
                if i == 1 and j == 1:  # Skip the center point to create a more challenging landscape
                    continue
                self.global_minima.append([minima_positions[i], minima_positions[j]])
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Quadratic basin term - pulls towards origin
        basin = 0.1 * np.sum(x**2)
        
        # Multimodal terms - multiple global minima
        multimodal = 0
        for min_pos in self.global_minima:
            if len(min_pos) == 2:  # Only consider 2D case for simplicity
                dist = np.sqrt((x[0] - min_pos[0])**2 + (x[1] - min_pos[1])**2)
                multimodal += 5.0 * np.exp(-dist**2 / 2.0)
        
        # Add some additional noise to make it more challenging
        noise = 0.01 * np.sum(np.sin(x))
        
        return basin + multimodal + noise