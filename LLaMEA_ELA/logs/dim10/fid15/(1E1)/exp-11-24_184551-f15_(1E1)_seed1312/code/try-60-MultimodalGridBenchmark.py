import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Quadratic basin term - encourages convergence to center
        basin_term = np.sum(x**2) * 0.1
        
        # Multimodal terms - multiple global minima arranged in a grid
        multimodal_term = 0.0
        
        # Create grid of global minima in first two dimensions
        num_minima_per_dim = 5
        grid_points = np.linspace(-4.0, 4.0, num_minima_per_dim)
        
        for i in range(num_minima_per_dim):
            for j in range(num_minima_per_dim):
                # Skip center point to avoid singularities
                if i == 2 and j == 2:
                    continue
                    
                # Only use first two dimensions for grid pattern
                min_x = grid_points[i]
                min_y = grid_points[j]
                
                # Calculate distance in first two dimensions only
                dist_sq = (x[0] - min_x)**2 + (x[1] - min_y)**2
                
                # Add contribution from this minimum
                multimodal_term += 1.0 / (1.0 + dist_sq)
        
        # Add a small noise term to make it non-trivial
        noise = np.sum(np.sin(x) * 0.01)
        
        return basin_term - multimodal_term + noise