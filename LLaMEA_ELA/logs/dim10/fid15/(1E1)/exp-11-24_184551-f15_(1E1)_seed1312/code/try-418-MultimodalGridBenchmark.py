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
        
        # Add center minimum at (0,0) for 2D case, or appropriate center for higher dimensions
        if self.dim >= 2:
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
            
            # Use only the first two dimensions for grid pattern, rest are zero for higher dims
            distance = 0.0
            for j in range(min(2, self.dim)):
                distance += (x[j] - min_point[j])**2
            
            # Add contribution from this minimum with a more complex weighting
            multimodal_term += 1.0 / (1.0 + distance * 0.5)
        
        # Add a sinusoidal noise term to make it non-trivial and increase complexity
        noise = np.sum(np.sin(x * 2.0) * 0.05)
        
        # Add a penalty term for out-of-bounds evaluation
        penalty = 0.0
        for i in range(self.dim):
            if x[i] < -5.0 or x[i] > 5.0:
                penalty += 100.0
                
        return basin_term - multimodal_term + noise + penalty