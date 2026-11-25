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
        basin_term = 0.2 * np.sum((x - 1.5)**2)
        
        # Grid of global minima with varying heights and distances
        minima_term = float('inf')
        for i, min_point in enumerate(self.global_minima):
            dist = np.sum(np.abs(x - np.array(min_point)))
            # Varying heights and scaling factors
            height = 0.3 * (i % 4) + 1.2
            scale = 0.8 + 0.4 * np.sin(i)
            if dist < minima_term:
                minima_term = dist * height * scale
        
        # Add a sinusoidal noise term with varying frequency
        noise = 0.02 * np.sum(np.sin(3 * x))
        
        return basin_term + minima_term + noise