import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with increased frequency and modified amplitude
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = 1.5 * np.sin(7 * np.pi * r) + 0.3 * np.sin(20 * np.pi * r)
        
        # Angular component with altered frequency and added harmonic
        if self.dim == 1:
            angular_term = 0
        else:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular_term = 0.8 * np.sin(10 * angles) + 0.4 * np.cos(15 * angles) + 0.2 * np.sin(25 * angles)
            
        # Cross-dimensional interactions with modified coupling strengths
        cross_terms = 0
        for i in range(self.dim - 1):
            cross_terms += (x_norm[i]**2 + x_norm[i+1]**2) * np.sin(4 * np.pi * x_norm[i] * x_norm[i+1])
            
        # Adaptive conditioning factor with different base
        cond_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Additional high-frequency noise component with modified scaling
        noise = 0.5 * np.sum(np.sin(30 * np.pi * x_norm) ** 4)
        
        # Combine all components with appropriate scaling
        return cond_factor * (radial_term + angular_term + cross_terms + noise)