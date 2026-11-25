import numpy as np

class MultimodalHexGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        
        # Generate hexagonal grid of global minima
        num_rows = 5
        spacing = 2.0
        for i in range(num_rows):
            for j in range(num_rows):
                if i == 0 and j == 0:
                    continue  # Skip the center point
                x_pos = (j - num_rows//2) * spacing
                y_pos = (i - num_rows//2) * spacing * np.sqrt(3)/2
                if i % 2 == 1:
                    x_pos += spacing/2
                self.global_minima.append([x_pos, y_pos])
        
        # Add center minimum
        self.global_minima.append([0.0, 0.0])
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Quadratic basin term - encourages convergence to center
        basin_term = np.sum(x**2) * 0.05
        
        # Multimodal terms - multiple global minima
        multimodal_term = 0.0
        for i in range(len(self.global_minima)):
            min_point = self.global_minima[i]
            if len(min_point) != min(2, self.dim):
                continue
                
            # Use first two dimensions for the hex grid pattern
            distance = (x[0] - min_point[0])**2 + (x[1] - min_point[1])**2
            # Add contribution from this minimum
            multimodal_term += 1.0 / (1.0 + distance)
        
        # Add sinusoidal perturbations to make it non-trivial
        perturbation = np.sum(np.sin(x * 0.5) * 0.1)
        
        return basin_term - multimodal_term + perturbation