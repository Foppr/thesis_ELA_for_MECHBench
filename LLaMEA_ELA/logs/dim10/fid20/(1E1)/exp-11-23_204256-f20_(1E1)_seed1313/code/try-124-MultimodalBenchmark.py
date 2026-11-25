import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with multiple sinusoidal modulations
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.sin(5 * np.pi * r) + 0.5 * np.sin(15 * np.pi * r) + 0.3 * np.sin(25 * np.pi * r)
        
        # Angular component using trigonometric functions in polar coordinates
        if self.dim == 1:
            angular_term = 0
        else:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular_term = np.sin(8 * angles) + 0.7 * np.cos(12 * angles) + 0.4 * np.sin(16 * angles)
            
        # Cross-dimensional interactions with varying coupling strengths
        cross_terms = 0
        for i in range(self.dim - 1):
            cross_terms += (x_norm[i]**2 + x_norm[i+1]**2) * np.sin(3 * np.pi * x_norm[i] * x_norm[i+1]) + 0.2 * x_norm[i] * x_norm[i+1]
            
        # Adaptive conditioning factor based on dimensionality
        cond_factor = 1.0 + 0.5 * np.log(self.dim + 1) + 0.1 * np.sin(2 * np.pi * self.dim)
        
        # Additional high-frequency noise component
        noise = np.sum(np.sin(25 * np.pi * x_norm) ** 4) + 0.3 * np.sum(np.cos(30 * np.pi * x_norm))
        
        # Combine all components with appropriate scaling
        return cond_factor * (radial_term + angular_term + cross_terms + noise)