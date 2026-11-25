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
        
        # Quadratic basin term that makes the search space deceptive
        basin_term = 0.2 * np.sum((x - 1.5)**2)
        
        # Grid of global minima with varying heights and sine modulation
        minima_term = float('inf')
        for i, coords in enumerate(self.global_minima):
            dist = np.sqrt(sum((x[j] - coords[j])**2 for j in range(self.dim)))
            # Varying heights and sine modulation
            height = 0.3 * (i % 4) + 1.2
            modulation = 0.5 * np.sin(0.5 * i)
            if dist < minima_term:
                minima_term = dist * (height + modulation)
        
        # Add noise and nonlinear interactions
        noise = 0.02 * np.sum(np.sin(x) * np.cos(0.3 * x))
        
        return basin_term + minima_term + noise