import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Quadratic basin term - encourages convergence to center
        basin_term = 0.1 * np.sum(x**2)
        
        # Multimodal terms with sinusoidal perturbations
        multimodal_term = 0.0
        for i in range(-2, 3):
            for j in range(-2, 3):
                if i == 0 and j == 0:
                    continue  # Skip the center point
                # Use first two dimensions for the grid pattern
                if self.dim >= 2:
                    distance = (x[0] - 2*i)**2 + (x[1] - 2*j)**2
                    multimodal_term += 1.0 / (1.0 + distance)
        
        # Add center minimum
        if self.dim >= 2:
            distance_center = x[0]**2 + x[1]**2
            multimodal_term += 5.0 / (1.0 + distance_center)
        
        # Sinusoidal perturbations to increase complexity
        sin_perturbation = np.sum(np.sin(x * 0.5))
        
        return basin_term - multimodal_term + sin_perturbation