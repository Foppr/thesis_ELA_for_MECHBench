import numpy as np

class NestedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with multiple nested minima
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = 0.5 * r**2 + 0.3 * np.sin(8 * np.pi * r) + 0.2 * np.cos(12 * np.pi * r)
        
        # Periodic interference patterns with varying frequencies
        interference = 0.0
        for i in range(self.dim):
            freq = (i % 5) + 1
            interference += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Adaptive conditioning based on distance from origin
        condition_factor = 1.0 + 3.0 * np.exp(-0.5 * r**2)
        
        # Multi-scale sinusoidal components with varying amplitudes and phases
        multiscale = 0.0
        for i in range(self.dim):
            amp = 1.0 / (1.0 + 0.2 * i)
            phase = np.pi * i / self.dim
            freq = 2**(i % 4)  # Geometric frequency progression
            multiscale += amp * np.sin(freq * x_norm[i] + phase)
        
        # Cross-term interactions with exponential weighting
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                weight = np.exp(-dist**2)
                cross_terms += weight * np.sin(4 * np.pi * dist) * np.cos(3 * np.pi * dist)
        
        # Nested basin structure with varying depths
        basin_depth = 0.0
        for i in range(self.dim):
            depth = 0.5 * (1 + np.tanh(2 * x_norm[i]))
            basin_depth += depth * np.sin(6 * np.pi * x_norm[i])**2
        
        # Combine all components with adjusted weights
        result = condition_factor * (radial_term + 0.3 * interference + 0.2 * multiscale + 
                                   0.15 * cross_terms + 0.1 * basin_depth)
        
        return result