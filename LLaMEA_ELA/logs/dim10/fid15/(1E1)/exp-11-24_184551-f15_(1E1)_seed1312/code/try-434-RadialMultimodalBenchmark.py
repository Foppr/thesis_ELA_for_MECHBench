import numpy as np

class RadialMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.num_local_minima = 12
        self.angle_step = 2 * np.pi / self.num_local_minima
        self.radius_decay = 0.8
        self.base_radius = 3.0
        
        # Precompute local minima positions
        self.local_minima = []
        for i in range(self.num_local_minima):
            angle = i * self.angle_step
            radius = self.base_radius * (self.radius_decay ** i)
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            self.local_minima.append([x, y])
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Center global minimum
        center_term = np.sum(x**2) * 0.05
        
        # Radial local minima
        radial_term = 0.0
        for i, min_point in enumerate(self.local_minima):
            if self.dim >= 2:
                distance = np.sqrt((x[0] - min_point[0])**2 + (x[1] - min_point[1])**2)
                # Exponentially decaying contribution
                radial_term += np.exp(-distance) * (0.5 ** i)
        
        # Sinusoidal perturbation for increased complexity
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(x[i] * (i + 1)) * 0.1
            
        return center_term - radial_term + sin_term