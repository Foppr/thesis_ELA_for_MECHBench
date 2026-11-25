import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponentially decaying sinusoidal waves with chaotic modulation
        wave_term = 0.0
        for i in range(self.dim):
            freq = (i % 6) + 2
            decay = np.exp(-0.1 * i)
            chaos_mod = np.sin(5 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
            wave_term += decay * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i]) * chaos_mod
        
        # Dynamic conditioning based on radial distance with chaotic scaling
        r = np.sqrt(np.sum(x_norm**2))
        cond_factor = 1.0 + 2.0 * np.sin(4 * np.pi * r)**2 * np.exp(-0.5 * r)
        
        # Rotation-invariant rugged landscape with multiple basin depths
        rugged_term = 0.0
        for i in range(self.dim):
            # Chaotic basin depth modulation
            depth_mod = 1.0 + 0.3 * np.sin(7 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i])
            rugged_term += depth_mod * (x_norm[i]**2 + 0.1 * np.sin(10 * np.pi * x_norm[i])**2)
        
        # Cross-term interactions with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + (x_norm[i] + x_norm[j])**2)
                coupling = np.sin(3 * np.pi * dist) * np.cos(4 * np.pi * dist)
                cross_term += coupling * np.exp(-dist * (1.0 + 0.2 * np.sin(5 * np.pi * dist)))
        
        # Multi-scale chaotic component with varying frequencies
        multi_scale = 0.0
        for i in range(self.dim):
            freqs = [2, 3, 5, 7]
            scale_factor = 1.0 / (i + 1)
            for f in freqs:
                multi_scale += scale_factor * np.sin(f * np.pi * x_norm[i]) * np.cos(f * np.pi * x_norm[i])
        
        # Combine all components with dynamic weighting based on dimensionality
        dim_weight = 1.0 + 0.1 * self.dim + 0.05 * np.sin(3 * np.pi * self.dim)
        result = dim_weight * (cond_factor * (0.7 * wave_term + 0.3 * rugged_term + 
                                             0.2 * cross_term + 0.4 * multi_scale))
        
        return result