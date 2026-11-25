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
                if i == 2 and j == 2:  # Skip center point to avoid trivial solution
                    continue
                # Calculate distance to grid point
                dist = (x[0] - grid_points[i])**2 + (x[1] - grid_points[j])**2
                # Add periodic contribution with harmonic components
                multimodal_term += np.exp(-dist/2.0) * np.sin(2.0 * np.pi * (x[0] - grid_points[i])) * np.cos(2.0 * np.pi * (x[1] - grid_points[j]))
        
        # Add higher dimensional harmonic components
        harmonic_term = 0.0
        for k in range(min(4, self.dim)):
            harmonic_term += np.sin(3.0 * x[k]) * np.cos(2.0 * x[k])
        
        # Combine all terms with appropriate scaling
        return basin_term - 2.0 * multimodal_term + 0.1 * harmonic_term