import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sinusoidal interference with increased frequency diversity
        wave_term = 0.0
        for i in range(self.dim):
            freq = (i % 7) + 2  # Increased frequency diversity
            decay = np.exp(-0.2 * i)  # Stronger decay rate
            chaos_mod = np.sin(5 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i]) * np.sin(1.5 * np.pi * x_norm[i])  # Triple modulation
            wave_term += decay * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i]) * chaos_mod
        
        # Dynamic conditioning with exponential scaling and enhanced nonlinearity
        r = np.sqrt(np.sum(x_norm**2))
        cond_factor = 1.0 + 2.0 * np.sin(4 * np.pi * r)**3 * np.exp(-0.5 * r)  # Cubic sine and stronger decay
        
        # Enhanced basin structure with multiple depth variations
        rugged_term = 0.0
        for i in range(self.dim):
            depth_mod = 1.0 + 0.6 * np.sin(7 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i]) * np.sin(2 * np.pi * x_norm[i])  # Triple depth modulation
            rugged_term += depth_mod * (x_norm[i]**2 + 0.2 * np.sin(10 * np.pi * x_norm[i])**3)  # Cubic sinusoidal component
        
        # Cross-term interactions with complex coupling and multi-scale effects
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + (x_norm[i] + x_norm[j])**2 + 0.1 * np.sin(5 * np.pi * (x_norm[i] + x_norm[j])))  # Added sinusoidal distance component
                coupling = np.sin(3 * np.pi * dist) * np.cos(4 * np.pi * dist) * np.sin(2 * np.pi * dist)  # Triple coupling
                cross_term += coupling * np.exp(-dist * (1.5 + 0.2 * np.sin(5 * np.pi * dist)))  # Modified decay
        
        # Multi-scale chaotic component with multiple frequency sets and complex scaling
        multi_scale = 0.0
        for i in range(self.dim):
            freqs = [2, 3, 5, 7, 9]  # Extended frequency set
            scale_factor = 1.0 / (i + 2.0)  # Modified scaling
            for f in freqs:
                multi_scale += scale_factor * np.sin(f * np.pi * x_norm[i]) * np.cos(f * np.pi * x_norm[i]) * np.sin(0.5 * f * np.pi * x_norm[i])
        
        # Combine all components with enhanced weighting and nonlinearity
        dim_weight = 1.0 + 0.15 * self.dim + 0.08 * np.sin(4 * np.pi * self.dim) + 0.03 * np.cos(2 * np.pi * self.dim)  # Complex weight function
        result = dim_weight * (cond_factor * (0.7 * wave_term + 0.25 * rugged_term + 
                                             0.3 * cross_term + 0.4 * multi_scale))
        
        return result