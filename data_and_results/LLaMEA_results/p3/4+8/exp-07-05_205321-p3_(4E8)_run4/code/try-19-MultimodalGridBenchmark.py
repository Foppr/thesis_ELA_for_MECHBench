import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima with better distribution
        grid_size = 5
        minima_positions = np.linspace(-4.5, 4.5, grid_size)
        for i in range(grid_size):
            for j in range(grid_size):
                if i == 2 and j == 2:  # Skip center point to create more challenging landscape
                    continue
                self.global_minima.append([minima_positions[i], minima_positions[j]])
        
        # Add multiple center minima to increase complexity
        self.global_minima.append([0.0, 0.0])
        self.global_minima.append([0.5, 0.5])
        self.global_minima.append([-0.5, -0.5])
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension does not match function dimension")
        
        # For 2D case, create a multimodal landscape with enhanced structure
        if self.dim == 2:
            # Quadratic basin in the center with modified coefficients
            basin = 0.05 * (x[0]**2 + x[1]**2)
            
            # Add multiple global minima with varying influence
            minima_penalty = 0
            for i, min_pos in enumerate(self.global_minima):
                dist = np.sqrt((x[0] - min_pos[0])**2 + (x[1] - min_pos[1])**2)
                # Varying influence based on index for more complex landscape
                influence = 1.0 / (1.0 + 0.1 * i)
                minima_penalty += influence * np.exp(-dist**2 / 0.3)
            
            # Add structured noise to improve fitness
            noise = 0.005 * np.sin(3 * x[0]) * np.cos(3 * x[1])
            
            return basin - minima_penalty + noise
        
        # For higher dimensions, use a combination of quadratic and periodic terms with enhanced structure
        else:
            # Quadratic term in the center with modified coefficient
            quadratic = 0.05 * np.sum(x**2)
            
            # Add periodic components with multiple frequencies to create multimodality
            periodic = 0
            for i in range(self.dim):
                periodic += np.sin(2 * np.pi * x[i] / 8.0) * np.cos(2 * np.pi * x[i] / 4.0) + \
                           0.5 * np.sin(4 * np.pi * x[i] / 8.0) * np.cos(4 * np.pi * x[i] / 4.0)
            
            # Add interaction terms between dimensions for increased complexity
            interaction = 0
            for i in range(self.dim-1):
                interaction += 0.3 * np.sin(x[i]) * np.cos(x[i+1])
            
            # Add structured noise
            noise = 0.003 * np.sum(np.sin(2 * x))
            
            return quadratic + 0.3 * periodic + 0.2 * interaction + noise