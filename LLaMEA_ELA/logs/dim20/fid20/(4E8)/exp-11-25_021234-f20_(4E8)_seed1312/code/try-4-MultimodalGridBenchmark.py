import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Grid of global minima at positions (±2, ±2, ±2, ...)
        grid_positions = np.array([[-2, 2]] * (self.dim // 2) + [[-2, 2]] * (self.dim - self.dim // 2)) if self.dim % 2 == 0 else np.array([[-2, 2]] * (self.dim // 2) + [[-2, 2]] * (self.dim - self.dim // 2) + [[0]])
        
        # Calculate distance to nearest grid minimum
        distances = []
        for i in range(0, len(grid_positions), 2):
            dist = np.sqrt(np.sum((x - grid_positions[i//2])**2))
            distances.append(dist)
            
        # Find minimum distance to any grid point
        min_dist = min(distances) if distances else 0
        
        # Add deceptive quadratic basin term that pulls towards origin
        basin_term = 0.1 * np.sum(x**2)
        
        # Combine terms with a scaling factor
        return min_dist + basin_term