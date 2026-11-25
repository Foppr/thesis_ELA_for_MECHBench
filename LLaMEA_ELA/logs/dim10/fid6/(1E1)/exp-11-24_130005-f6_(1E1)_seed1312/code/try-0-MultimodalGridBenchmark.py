import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate global minima positions in a grid pattern
        grid_size = 3
        for i in range(grid_size):
            for j in range(grid_size):
                x = np.zeros(dim)
                for k in range(min(dim, 2)):
                    if k == 0:
                        x[k] = -3 + i * 3 / (grid_size - 1) if grid_size > 1 else 0
                    elif k == 1:
                        x[k] = -3 + j * 3 / (grid_size - 1) if grid_size > 1 else 0
                self.global_minima.append(x)
    
    def f(self, x):
        # Normalize input to [-1, 1] range for easier computation
        x_norm = x / 5.0
        
        # Calculate distance to each global minimum
        distances = []
        for minima in self.global_minima:
            dist = np.linalg.norm(x_norm - minima)
            distances.append(dist)
        
        # Find the minimum distance to any global minimum
        min_dist = min(distances)
        
        # Add a valley term that makes the center more attractive
        valley_term = 0.1 * np.sum(x_norm**2)
        
        # Add a sinusoidal component to increase complexity
        sin_term = 0.5 * np.sin(2 * np.pi * np.sum(x_norm))
        
        return min_dist + valley_term + sin_term