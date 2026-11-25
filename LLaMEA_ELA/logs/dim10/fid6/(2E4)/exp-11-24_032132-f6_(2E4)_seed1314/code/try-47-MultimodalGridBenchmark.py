import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate global minima positions in a grid pattern
        grid_size = int(np.ceil(np.power(2, dim/2)))
        if grid_size > 10: 
            grid_size = 10  # Prevent excessive computation
        positions = np.linspace(-4.5, 4.5, grid_size)
        for i in range(grid_size):
            for j in range(grid_size):
                if self.dim >= 2:
                    self.global_minima.append([positions[i], positions[j]] + [0.0] * (self.dim - 2))
                else:
                    self.global_minima.append([positions[i]] + [0.0] * (self.dim - 1))

    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Quadratic basin term
        basin = np.sum((x - 0.5)**2)
        
        # Multimodal terms with global minima
        min_distance = float('inf')
        for min_pos in self.global_minima:
            distance = np.sum((x - np.array(min_pos))**2)
            if distance < min_distance:
                min_distance = distance
        
        # Add a sinusoidal component to create more complex landscape
        sin_term = 0.5 * np.sin(0.5 * np.sum(x**2))
        
        # Add a cosine term for additional complexity
        cos_term = 0.3 * np.cos(0.3 * np.sum(x**2))
        
        return basin + min_distance + sin_term + cos_term