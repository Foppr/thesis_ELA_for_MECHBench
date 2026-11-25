import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Quadratic basin term - encourages convergence to center
        basin_term = np.sum(x**2) * 0.1
        
        # Multimodal terms - multiple global minima in a grid pattern
        multimodal_term = 0.0
        grid_size = 5
        grid_points = np.linspace(-4.0, 4.0, grid_size)
        
        for i in range(grid_size):
            for j in range(grid_size):
                # Skip the center point to avoid trivial solution
                if i == 2 and j == 2:
                    continue
                    
                # Calculate distance using only first two dimensions for grid pattern
                if self.dim >= 2:
                    distance = (x[0] - grid_points[i])**2 + (x[1] - grid_points[j])**2
                    multimodal_term += 1.0 / (1.0 + distance)
        
        # Add a small noise term to make it non-trivial
        noise = np.sum(np.sin(x) * 0.01)
        
        return basin_term - multimodal_term + noise