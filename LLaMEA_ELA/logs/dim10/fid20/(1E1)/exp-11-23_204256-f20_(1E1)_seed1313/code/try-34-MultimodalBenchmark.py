import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with sinusoidal modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = r * (1.0 + 0.5 * np.sin(5 * np.pi * r))
        
        # Angular component with multiple frequencies
        if self.dim > 1:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular_term = np.sum([
                np.sin((i+1) * angles + i) * np.cos((i+1) * angles - i)
                for i in range(min(3, self.dim))
            ])
        else:
            angular_term = 0.0
            
        # Polynomial penalty terms
        poly_term = np.sum(x_norm**4) + 0.5 * np.sum(x_norm**6)
        
        # Cross-dimensional interaction terms
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x_norm[i] ** 2) * x_norm[i+1]
            
        # Add noise-like perturbations
        noise = np.sum(np.sin(13 * x_norm) * np.cos(7 * x_norm))
        
        # Combine all terms with adaptive scaling
        total = radial_term + angular_term + poly_term + cross_term + noise
        
        # Scale based on dimensionality for better conditioning
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return scale_factor * total