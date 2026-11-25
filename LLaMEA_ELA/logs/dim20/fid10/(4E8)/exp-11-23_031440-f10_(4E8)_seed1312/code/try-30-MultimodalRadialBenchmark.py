import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial distance from origin
        r = np.sqrt(np.sum(x_norm**2))
        
        # Base quadratic term with adaptive conditioning
        base_term = 0.1 * r**2
        
        # Sinusoidal perturbations in radial direction
        radial_sine = 0.5 * np.sin(5 * np.pi * r) * np.sin(3 * np.pi * r)
        
        # Angular terms creating multiple minima
        angle_terms = 0.0
        for i in range(self.dim):
            angle_terms += np.sin((i + 1) * np.pi * x_norm[i]) * np.cos((i + 1) * np.pi * x_norm[(i + 1) % self.dim])
        
        # Nested basin structure with varying depths
        depth_factor = 1.0 / (1.0 + np.exp(-5 * (r - 0.5)))
        basin_depth = 2.0 * depth_factor
        
        # Combine all terms with adaptive weighting
        result = base_term + radial_sine + 0.3 * angle_terms + basin_depth * r**4
        
        return result