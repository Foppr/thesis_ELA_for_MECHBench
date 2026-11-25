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
                if i == 0 and j == 0:
                    continue  # Skip the center point
                # Add small random shifts to minima positions
                shift_x = np.random.uniform(-0.2, 0.2)
                shift_y = np.random.uniform(-0.2, 0.2)
                self.global_minima.append([grid_points[i] + shift_x, grid_points[j] + shift_y])
        
        # Add center minimum with shift
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
            if len(min_point) != min(2, self.dim):
                continue
                
            # Use first two dimensions for the grid pattern, rest are zero
            distance = 0.0
            for j in range(min(2, self.dim)):
                distance += (x[j] - min_point[j])**2
            
            # Add contribution from this minimum
            multimodal_term += 1.0 / (1.0 + distance)
        
        # Add sinusoidal perturbations to increase landscape complexity
        perturbation = np.sum(np.sin(x * 2.0) * 0.05)
        
        return basin_term - multimodal_term + perturbation