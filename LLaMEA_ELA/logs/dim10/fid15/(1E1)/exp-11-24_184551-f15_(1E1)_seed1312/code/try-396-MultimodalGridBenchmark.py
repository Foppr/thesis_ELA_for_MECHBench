import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        
        # Generate grid of global minima with shifts
        num_minima = 5
        grid_points = np.linspace(-4.0, 4.0, num_minima)
        for i in range(num_minima):
            for j in range(num_minima):
                if i == 2 and j == 2:  # Skip center point
                    continue
                # Shift some minima to create more challenging landscape
                shift_x = np.random.uniform(-0.5, 0.5) if (i+j)%3 == 0 else 0.0
                shift_y = np.random.uniform(-0.5, 0.5) if (i+j)%3 == 0 else 0.0
                self.global_minima.append([grid_points[i] + shift_x, grid_points[j] + shift_y])
        
        # Add center minimum
        self.global_minima.append([0.0, 0.0])
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Quadratic basin term - encourages convergence to center
        basin_term = np.sum(x**2) * 0.1
        
        # Multimodal terms - multiple global minima
        multimodal_term = 0.0
        for i in range(len(self.global_minima)):
            min_point = self.global_minima[i]
            if len(min_point) != self.dim:
                continue
                
            # Use first two dimensions for the grid pattern, rest are zero
            distance = 0.0
            for j in range(min(2, self.dim)):
                distance += (x[j] - min_point[j])**2
            
            # Add contribution from this minimum with modified strength
            multimodal_term += 1.0 / (1.0 + 0.5 * distance)
        
        # Add a small noise term to make it non-trivial
        noise = np.sum(np.sin(x) * 0.01)
        
        return basin_term - multimodal_term + noise