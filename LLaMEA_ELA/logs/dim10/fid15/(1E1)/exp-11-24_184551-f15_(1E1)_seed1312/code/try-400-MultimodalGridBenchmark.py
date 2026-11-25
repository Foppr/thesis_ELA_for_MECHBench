import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_minima = []
        
        # Generate hexagonal grid of global minima
        num_minima = 7
        radius = 3.0
        angles = np.linspace(0, 2*np.pi, num_minima, endpoint=False)
        for i in range(num_minima):
            x = radius * np.cos(angles[i])
            y = radius * np.sin(angles[i])
            self.global_minima.append([x, y])
        
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
            if len(min_point) != 2:  # Only use first two dimensions for grid pattern
                continue
                
            # Calculate distance using first two dimensions
            distance = (x[0] - min_point[0])**2 + (x[1] - min_point[1])**2
            
            # Add contribution from this minimum
            multimodal_term += 1.0 / (1.0 + distance)
        
        # Add sinusoidal perturbations to make it non-trivial
        perturbation = np.sum(np.sin(x * 0.5) * 0.1)
        
        return basin_term - multimodal_term + perturbation