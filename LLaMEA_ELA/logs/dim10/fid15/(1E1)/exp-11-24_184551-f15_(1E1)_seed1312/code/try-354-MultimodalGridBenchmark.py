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
        
        # Define grid points for global minima
        grid_points = np.linspace(-4.0, 4.0, 5)
        
        # Create all combinations of grid points (only for first two dimensions)
        for i in range(len(grid_points)):
            for j in range(len(grid_points)):
                if i == 2 and j == 2:  # Skip center point to avoid trivial solution
                    continue
                    
                # Only use first two dimensions for grid pattern
                if self.dim >= 2:
                    distance = (x[0] - grid_points[i])**2 + (x[1] - grid_points[j])**2
                    multimodal_term += 1.0 / (1.0 + distance)
        
        # Add center minimum contribution
        if self.dim >= 2:
            distance = x[0]**2 + x[1]**2
            multimodal_term += 1.0 / (1.0 + distance)
        
        # Add a small noise term to make it non-trivial
        noise = np.sum(np.sin(x) * 0.01)
        
        return basin_term - multimodal_term + noise