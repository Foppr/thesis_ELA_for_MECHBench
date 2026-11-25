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
                if i == 0 and j == 0:
                    continue  # Skip the center point
                self.global_minima.append([grid_points[i], grid_points[j]])
        
        # Add center minimum
        self.global_minima.append([0.0, 0.0])
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Quadratic basin term - encourages convergence to center, scaled by dimension
        basin_term = np.sum(x**2) * 0.05
        
        # Multimodal terms - multiple global minima with adaptive scaling
        multimodal_term = 0.0
        for i in range(len(self.global_minima)):
            min_point = self.global_minima[i]
            if len(min_point) != min(2, self.dim):
                continue
                
            # Use first two dimensions for the grid pattern, rest are zero
            distance = 0.0
            for j in range(min(2, self.dim)):
                distance += (x[j] - min_point[j])**2
            
            # Add contribution from this minimum with inverse square decay
            multimodal_term += 1.0 / (1.0 + distance**2)
        
        # Add periodic components to increase landscape complexity
        periodic_term = np.sum(np.sin(x * 2.0 * np.pi) * 0.1)
        
        # Add a small noise term to make it non-trivial
        noise = np.sum(np.random.normal(0, 0.001, len(x)))
        
        return basin_term - multimodal_term + periodic_term + noise