import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima with shifts
        grid_points = np.linspace(-4.0, 4.0, 5)
        for point in np.nditer(np.meshgrid(*[grid_points] * dim, indexing='ij')):
            self.global_minima.append(point.tolist())
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Modified deceptive quadratic basin
        basin_term = 0.2 * np.sum((x + 1.0)**2)
        
        # Grid of global minima with varying heights and distances
        minima_term = float('inf')
        for i, min_point in enumerate(self.global_minima):
            dist = np.sum((x - np.array(min_point))**2)
            # Varying heights and distances for different minima
            height = 0.3 * (i % 4) + 1.5
            if dist < minima_term:
                minima_term = np.sqrt(dist) * height
        
        # Add sinusoidal noise with varying frequency
        noise = 0.02 * np.sum(np.sin(2.0 * x))
        
        return basin_term + minima_term + noise