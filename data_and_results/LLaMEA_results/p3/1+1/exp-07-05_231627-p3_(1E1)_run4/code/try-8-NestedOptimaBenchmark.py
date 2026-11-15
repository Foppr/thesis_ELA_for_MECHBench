import numpy as np

class NestedOptimaBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for consistent scaling
        x_norm = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_norm**2, axis=-1, keepdims=True))
        radial = np.exp(-5 * r) * (1 + 0.5 * np.sin(10 * r))
        
        # Angular modulation with multiple frequencies
        if self.dim > 1:
            angles = np.arctan2(x_norm[..., 1], x_norm[..., 0])
            angular = np.sum([np.sin((i+1) * angles) * np.cos((i+1) * angles) 
                             for i in range(min(3, self.dim))], axis=0)
        else:
            angular = 0
        
        # Multi-scale sinusoidal modulation
        scale_mod = np.sum([np.sin((i+1) * np.pi * x_norm) * np.cos((i+1) * np.pi * x_norm) 
                           for i in range(min(4, self.dim))], axis=0)
        
        # Nested quadratic wells with varying depths
        wells = np.sum([(x_norm - np.sin(np.pi * x_norm))**2 + 0.1 * np.sin(5 * np.pi * x_norm)**2] * self.dim, axis=0)
        
        # Combined landscape with adaptive weights
        result = 0.3 * radial + 0.25 * angular + 0.2 * scale_mod + 0.25 * wells
        
        # Add small perturbation to avoid exact replicability
        perturbation = 0.001 * np.sum(np.sin(x_norm**3), axis=-1)
        
        return np.squeeze(result + perturbation)