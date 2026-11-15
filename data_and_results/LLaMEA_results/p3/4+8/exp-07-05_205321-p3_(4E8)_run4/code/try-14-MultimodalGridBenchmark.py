import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima with shifted positions
        grid_size = 3
        minima_positions = np.linspace(-4.5, 4.5, grid_size)
        for i in range(grid_size):
            for j in range(grid_size):
                if i == 1 and j == 1:  # Skip the center point
                    continue
                self.global_minima.append([minima_positions[i], minima_positions[j]])
        
        # Add shifted center minimum
        self.global_minima.append([0.5, 0.5])
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension does not match function dimension")
        
        # For 2D case, create a multimodal landscape
        if self.dim == 2:
            # Quadratic basin in the center
            basin = 0.15 * (x[0]**2 + x[1]**2)
            
            # Add multiple global minima with modified distances
            minima_penalty = 0
            for min_pos in self.global_minima:
                dist = np.sqrt((x[0] - min_pos[0])**2 + (x[1] - min_pos[1])**2)
                minima_penalty += np.exp(-dist**2 / 0.3)
            
            # Add some noise to make it more challenging
            noise = 0.02 * np.random.random()
            
            return basin - minima_penalty + noise
        
        # For higher dimensions, use a combination of quadratic and periodic terms
        else:
            # Quadratic term in the center
            quadratic = 0.15 * np.sum(x**2)
            
            # Add periodic components with different frequencies to create multimodality
            periodic = 0
            for i in range(self.dim):
                periodic += np.sin(3 * np.pi * x[i] / 10.0) * np.cos(4 * np.pi * x[i] / 5.0)
            
            # Add some noise
            noise = 0.02 * np.random.random()
            
            return quadratic + 0.6 * periodic + noise