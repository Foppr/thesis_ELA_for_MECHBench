import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Quadratic basin term - encourages convergence to center
        basin_term = 0.1 * np.sum(x**2)
        
        # Multimodal terms with periodic pattern
        multimodal_term = 0.0
        grid_size = 5
        grid_points = np.linspace(-4.0, 4.0, grid_size)
        
        for i in range(grid_size):
            for j in range(grid_size):
                if i == 2 and j == 2:  # Skip center point to avoid trivial solution
                    continue
                # Use first two dimensions for the grid pattern
                if self.dim >= 2:
                    distance = (x[0] - grid_points[i])**2 + (x[1] - grid_points[j])**2
                    multimodal_term += 1.0 / (1.0 + distance)
        
        # Add harmonic terms for additional complexity
        harmonic_term = 0.0
        for k in range(min(3, self.dim)):  # Use first few dimensions for harmonics
            harmonic_term += np.sin(2 * np.pi * x[k]) * np.cos(3 * np.pi * x[k])
        
        # Add noise term
        noise = 0.01 * np.sum(np.sin(x))
        
        return basin_term - multimodal_term + harmonic_term + noise