import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential radial component with multiple frequencies
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**2) * (np.sin(10 * np.pi * r) + 0.3 * np.cos(25 * np.pi * r) + 0.1 * np.sin(50 * np.pi * r))
        
        # Angular component with chaotic behavior
        if self.dim == 1:
            angular_term = 0
        else:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular_term = np.sin(15 * angles) * np.cos(7 * angles) + 0.5 * np.sin(23 * angles) * np.cos(11 * angles)
            
        # Chaotic cross-dimensional interactions with non-linear coupling
        cross_terms = 0
        for i in range(self.dim - 1):
            cross_terms += np.exp(-abs(x_norm[i] - x_norm[i+1])) * np.sin(20 * (x_norm[i]**2 + x_norm[i+1]**2))
            
        # Adaptive conditioning with exponential scaling
        cond_factor = 1.0 + 2.0 * np.exp(-self.dim / 5.0)
        
        # High-frequency chaotic noise component
        noise = np.sum(np.sin(30 * np.pi * x_norm) ** 6 + 0.5 * np.cos(40 * np.pi * x_norm) ** 4)
        
        # Additional global structure with periodic modulation
        periodic_structure = np.sin(2 * np.pi * r) * np.cos(3 * np.pi * r)
        
        # Combine all components with appropriate scaling
        return cond_factor * (radial_term + angular_term + cross_terms + noise + periodic_structure)