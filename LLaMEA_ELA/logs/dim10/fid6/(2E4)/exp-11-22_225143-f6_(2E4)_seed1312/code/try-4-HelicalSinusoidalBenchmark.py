import numpy as np

class HelicalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f_val = np.sum(x_norm**2)
        
        # Helical structure: combine radial and angular components
        if self.dim >= 2:
            # Radial component
            r = np.sqrt(x_norm[0]**2 + x_norm[1]**2)
            # Angular component (in 2D plane)
            theta = np.arctan2(x_norm[1], x_norm[0])
            
            # Helical sinusoidal modulation
            f_val += 2.0 * np.sin(5 * r) * np.cos(3 * theta) + 1.0 * np.sin(7 * r) * np.sin(4 * theta)
        
        # Add higher dimensional interactions with sinusoidal patterns
        for i in range(self.dim):
            # Radial sinusoidal oscillations
            radial_sum = 0.0
            for j in range(i):
                if j < self.dim - 1:
                    radial_sum += np.sin(2 * np.pi * (x_norm[i] + x_norm[j]))
            f_val += 0.3 * np.sin(4 * np.pi * x_norm[i]) * (1 + 0.5 * radial_sum)
        
        # Add multi-modal structure with varying frequencies
        for i in range(self.dim):
            f_val += 0.2 * np.sin(6 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
        
        # Add global structure with multiple valleys
        if self.dim >= 3:
            # 3D helical pattern
            f_val += 0.5 * np.sin(2 * np.pi * (x_norm[0] + x_norm[1] + x_norm[2])) * \
                     np.cos(2 * np.pi * (x_norm[0] - x_norm[1]) * x_norm[2])
        
        return f_val