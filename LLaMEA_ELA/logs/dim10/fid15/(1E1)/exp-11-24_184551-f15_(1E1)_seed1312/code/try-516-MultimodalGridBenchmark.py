import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Quadratic basin term - encourages convergence to center
        basin_term = 0.1 * np.sum(x**2)
        
        # Multimodal terms with periodic structure
        multimodal_term = 0.0
        grid_size = 5
        grid_points = np.linspace(-4.0, 4.0, grid_size)
        
        for i in range(grid_size):
            for j in range(grid_size):
                if i == 2 and j == 2:  # Skip center point
                    continue
                min_point = [grid_points[i], grid_points[j]]
                
                # Use first two dimensions for the grid pattern
                distance = (x[0] - min_point[0])**2 + (x[1] - min_point[1])**2
                
                # Add contribution from this minimum with periodic behavior
                multimodal_term += 1.0 / (1.0 + distance) * np.sin(0.5 * distance)
        
        # Add harmonic terms to increase landscape complexity
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += np.sin(2.0 * x[i]) * np.cos(0.5 * x[i])
            
        # Add noise term
        noise = 0.01 * np.sum(np.sin(x))
        
        return basin_term - multimodal_term + harmonic_term + noise