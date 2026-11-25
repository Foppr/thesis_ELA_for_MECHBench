import numpy as np

class SpiralMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.num_minima = 12
        self.spiral_radius = 4.0
        self.center_penalty = 10.0
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Normalize input to [-1, 1] for spiral calculation
        x_norm = x / 5.0
        x_norm = np.clip(x_norm, -1.0, 1.0)
        
        # Central global minimum with quadratic basin
        central_term = np.sum(x**2) * 0.05
        
        # Spiral pattern of local minima
        spiral_term = 0.0
        for i in range(self.num_minima):
            angle = i * (2 * np.pi / self.num_minima)
            radius = self.spiral_radius * np.exp(-i * 0.3)
            
            # Position in the spiral
            min_x = radius * np.cos(angle)
            min_y = radius * np.sin(angle)
            
            # Calculate distance in normalized space
            dist_x = x_norm[0] - min_x if self.dim > 0 else 0
            dist_y = x_norm[1] - min_y if self.dim > 1 else 0
            
            # Add contribution from this minimum (decaying with distance)
            distance_squared = dist_x**2 + dist_y**2
            spiral_term += np.exp(-distance_squared * 5.0) / (1.0 + i * 0.1)
        
        # Sinusoidal perturbations to increase complexity
        sin_term = np.sum(np.sin(x * 2.0) * 0.1)
        
        # Combine all terms
        return central_term - spiral_term + sin_term