import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        
        # Generate grid of global minima with periodic pattern
        num_minima = 5
        grid_points = np.linspace(-4.0, 4.0, num_minima)
        for i in range(num_minima):
            for j in range(num_minima):
                if i == 2 and j == 2:  # Skip center point to create more challenging landscape
                    continue
                self.global_minima.append([grid_points[i], grid_points[j]])
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Quadratic basin term - encourages convergence to center
        basin_term = np.sum(x**2) * 0.05
        
        # Multimodal terms - multiple global minima with periodic pattern
        multimodal_term = 0.0
        for i in range(len(self.global_minima)):
            min_point = self.global_minima[i]
            if len(min_point) != 2:  # Only use first two dimensions
                continue
                
            # Calculate distance in first two dimensions
            distance = (x[0] - min_point[0])**2 + (x[1] - min_point[1])**2
            
            # Add contribution from this minimum with sinusoidal modulation
            multimodal_term += 1.0 / (1.0 + distance) * np.sin(0.5 * distance)
        
        # Add sinusoidal modulation across all dimensions to increase complexity
        sin_modulation = np.sum(np.sin(x * 0.5))
        
        # Add a small noise term to make it non-trivial
        noise = np.sum(np.random.normal(0, 0.01, len(x)))
        
        return basin_term - multimodal_term + sin_modulation + noise