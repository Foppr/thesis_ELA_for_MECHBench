import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate global minima positions in a grid pattern
        grid_size = int(np.ceil(np.power(2, dim/2)))
        if grid_size < 2: grid_size = 2
        positions = np.linspace(-4.5, 4.5, grid_size)
        for i in range(grid_size):
            for j in range(grid_size):
                if self.dim >= 2:
                    self.global_minima.append([positions[i], positions[j]] + [0.0]*(self.dim-2))
        
        # Ensure we have enough global minima
        while len(self.global_minima) < 10:
            self.global_minima.append([np.random.uniform(-4.5, 4.5)] * self.dim)
        
        self.global_minima = np.array(self.global_minima)
    
    def f(self, x):
        # Base quadratic term
        result = np.sum(x**2) / 100.0
        
        # Add multiple global minima with different strengths
        for i, min_point in enumerate(self.global_minima[:10]):
            dist = np.linalg.norm(x - min_point)
            # Create attractive wells around each minimum
            result += 1.0 / (1.0 + dist**2) * np.exp(-dist/5.0)
        
        # Add a deceptive basin to make optimization harder
        basin_center = np.zeros(self.dim)
        basin_radius = 2.0
        basin_strength = 0.5
        
        dist_from_center = np.linalg.norm(x - basin_center)
        if dist_from_center < basin_radius:
            result += basin_strength * (basin_radius - dist_from_center)**2
        
        return result