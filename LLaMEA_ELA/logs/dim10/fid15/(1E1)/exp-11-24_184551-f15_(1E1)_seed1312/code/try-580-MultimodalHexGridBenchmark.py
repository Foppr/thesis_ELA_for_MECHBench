import numpy as np

class MultimodalHexGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        
        # Generate hexagonal grid of global minima
        num_minima_per_side = 5
        spacing = 2.0
        hex_points = []
        
        # Create hexagonal pattern in 2D
        for i in range(num_minima_per_side):
            for j in range(num_minima_per_side):
                if i == 0 and j == 0:
                    continue  # Skip the center point
                x = (i - num_minima_per_side//2) * spacing
                y = (j - num_minima_per_side//2) * spacing * np.sqrt(3)/2
                if i % 2 == 1:  # Offset every other row
                    x += spacing/2
                hex_points.append([x, y])
        
        # Add center minimum
        hex_points.append([0.0, 0.0])
        
        # Store global minima
        self.global_minima = hex_points
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Quadratic basin term - encourages convergence to center
        basin_term = np.sum(x**2) * 0.05
        
        # Multimodal terms - multiple global minima with hexagonal pattern
        multimodal_term = 0.0
        for i in range(len(self.global_minima)):
            min_point = self.global_minima[i]
            if len(min_point) != min(2, self.dim):
                continue
                
            # Use first two dimensions for the grid pattern, rest are zero
            distance = 0.0
            for j in range(min(2, self.dim)):
                distance += (x[j] - min_point[j])**2
            
            # Add contribution from this minimum
            multimodal_term += 1.0 / (1.0 + distance)
        
        # Add saddle points in higher dimensions to increase difficulty
        saddle_term = 0.0
        for i in range(min(4, self.dim)):
            saddle_term += x[i]**4 - 2*x[i]**2
        
        # Add a small noise term to make it non-trivial
        noise = np.sum(np.sin(x) * 0.01)
        
        return basin_term - multimodal_term + saddle_term + noise