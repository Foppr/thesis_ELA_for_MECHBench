import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Grid of global minima at positions (±2, ±2, ±2, ...)
        grid_minima = []
        for i in range(self.dim):
            if i % 2 == 0:
                grid_minima.append([-2, 2])
            else:
                grid_minima.append([-2, 2])
        
        # Calculate distance to nearest grid minimum
        min_dist = float('inf')
        for i in range(len(grid_minima[0])):
            dist = np.sqrt(np.sum((x - np.array([grid_minima[j][i] for j in range(self.dim)]))**2))
            if dist < min_dist:
                min_dist = dist
                
        # Add deceptive quadratic basin term that pulls towards origin
        basin_term = 0.1 * np.sum(x**2)
        
        # Add sine modulation to increase landscape complexity
        sine_term = 0.5 * np.sin(0.5 * np.sum(x))
        
        # Combine terms with a scaling factor
        return min_dist + basin_term + sine_term