import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        
        # Generate grid of global minima
        num_minima = 5
        grid_points = np.linspace(-4.0, 4.0, num_minima)
        for i in range(num_minima):
            for j in range(num_minima):
                if i == 2 and j == 2:  # Skip the center point (index 2,2)
                    continue
                self.global_minima.append([grid_points[i], grid_points[j]])
        
        # Add center minimum at (0,0) - this will be the primary global optimum
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
            if len(min_point) != min(2, self.dim):  # Ensure we only use the first two dimensions
                continue
                
            # Use first two dimensions for the grid pattern, rest are zero
            distance = 0.0
            for j in range(min(2, self.dim)):
                distance += (x[j] - min_point[j])**2
            
            # Add contribution from this minimum - avoid division by zero
            if distance < 1e-10:
                multimodal_term += 100.0  # Large value at exact minima
            else:
                multimodal_term += 1.0 / (1.0 + distance)
        
        # Add a small noise term to make it non-trivial and prevent trivial solutions
        noise = np.sum(np.sin(x) * 0.01)
        
        # Return the combined function value
        return basin_term - multimodal_term + noise