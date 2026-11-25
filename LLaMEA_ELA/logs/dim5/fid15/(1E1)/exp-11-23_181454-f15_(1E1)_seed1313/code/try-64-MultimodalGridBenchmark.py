import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        # Generate grid of global minima with shift
        grid_points = np.linspace(-4.0, 4.0, 5)
        for point in np.nditer(np.meshgrid(*[grid_points] * dim, indexing='ij')):
            self.global_minima.append(point.tolist())
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Modified quadratic basin term with different scaling
        basin_term = 0.3 * np.sum((x + 1.5)**2)
        
        # Grid of global minima with varying heights and distances
        minima_term = float('inf')
        for i, coords in enumerate(self.global_minima):
            dist = np.sum((x - np.array(coords))**2)
            # Varying heights and distances for different minima
            height = 0.3 * (i % 4) + 1.2
            if dist < minima_term:
                minima_term = np.sqrt(dist) * height
        
        # Add a sinusoidal noise term with higher frequency
        noise = 0.02 * np.sum(np.sin(3 * x))
        
        return basin_term + minima_term + noise