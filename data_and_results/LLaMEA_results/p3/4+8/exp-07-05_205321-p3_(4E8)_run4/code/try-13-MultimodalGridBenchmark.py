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
                    continue  # Skip the center point
                self.global_minima.append([minima_positions[i], minima_positions[j]])
        
        # Add center minimum
        self.global_minima.append([0.0, 0.0])
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension does not match function dimension")
        
        # For 2D case, create a multimodal landscape
        if self.dim == 2:
            # Quadratic basin in the center with modified coefficients
            basin = 0.2 * (x[0]**2 + x[1]**2)
            
            # Add multiple global minima with enhanced attraction
            minima_penalty = 0
            for min_pos in self.global_minima:
                dist = np.sqrt((x[0] - min_pos[0])**2 + (x[1] - min_pos[1])**2)
                minima_penalty += 2.0 * np.exp(-dist**2 / 0.3)
            
            # Add structured noise to improve fitness
            noise = 0.02 * np.sin(x[0]) * np.cos(x[1])
            
            return basin - minima_penalty + noise
        
        # For higher dimensions, use enhanced multimodal components
        else:
            # Quadratic term in the center with increased influence
            quadratic = 0.2 * np.sum(x**2)
            
            # Add enhanced periodic components with varied frequencies
            periodic = 0
            for i in range(self.dim):
                freq1 = 2 * np.pi * (i + 1) / 8.0
                freq2 = 2 * np.pi * (i + 1) / 4.0
                periodic += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
            
            # Add cross-dimensional interaction terms
            interaction = 0
            for i in range(self.dim - 1):
                interaction += 0.1 * x[i] * x[i+1]
            
            # Add controlled noise
            noise = 0.01 * np.random.random()
            
            return quadratic + 0.3 * periodic + 0.1 * interaction + noise