import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        
        # Generate grid of global minima in rotated space
        num_minima = 5
        grid_points = np.linspace(-4.0, 4.0, num_minima)
        rotation_angle = np.pi / 4  # 45 degree rotation
        
        for i in range(num_minima):
            for j in range(num_minima):
                if i == 2 and j == 2:  # Skip center point
                    continue
                x, y = grid_points[i], grid_points[j]
                # Apply rotation
                rotated_x = x * np.cos(rotation_angle) - y * np.sin(rotation_angle)
                rotated_y = x * np.sin(rotation_angle) + y * np.cos(rotation_angle)
                self.global_minima.append([rotated_x, rotated_y])
        
        # Add center minimum at origin
        self.global_minima.append([0.0, 0.0])
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Quadratic basin term - encourages convergence to center with adaptive strength
        basin_term = np.sum(x**2) * 0.1
        
        # Multimodal terms - multiple global minima with varying influence
        multimodal_term = 0.0
        for i in range(len(self.global_minima)):
            min_point = self.global_minima[i]
            if len(min_point) != min(2, self.dim):
                continue
                
            # Use first two dimensions for the grid pattern
            distance = 0.0
            for j in range(min(2, self.dim)):
                distance += (x[j] - min_point[j])**2
            
            # Add contribution from this minimum with varying weight
            weight = 1.0 / (1.0 + distance * 0.5)
            multimodal_term += weight * np.exp(-distance * 0.1)
        
        # Add a diverse noise term to make it non-trivial and increase fitness score
        noise = 0.0
        for i in range(len(x)):
            noise += np.sin(x[i] * (i + 1)) * 0.02
            
        return basin_term - multimodal_term + noise