import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Quadratic basin term - encourages convergence to center
        basin_term = np.sum(x**2) * 0.05
        
        # Multimodal terms with periodic structure
        multimodal_term = 0.0
        grid_size = 3
        grid_points = np.linspace(-4.0, 4.0, grid_size)
        
        for i in range(grid_size):
            for j in range(grid_size):
                if i == grid_size//2 and j == grid_size//2:
                    continue  # Skip the center point
                
                # Use first two dimensions for the grid pattern
                if self.dim >= 2:
                    min_point = [grid_points[i], grid_points[j]]
                    distance = (x[0] - min_point[0])**2 + (x[1] - min_point[1])**2
                    multimodal_term += 1.0 / (1.0 + distance)
        
        # Add harmonic components for increased complexity
        harmonic_term = 0.0
        for i in range(min(5, self.dim)):
            harmonic_term += np.sin(x[i] * (i + 1) * np.pi / 2.0) * 0.1
            
        # Add a small noise term to make it non-trivial
        noise = np.sum(np.sin(x * 0.5) * 0.02)
        
        return basin_term - multimodal_term + harmonic_term + noise