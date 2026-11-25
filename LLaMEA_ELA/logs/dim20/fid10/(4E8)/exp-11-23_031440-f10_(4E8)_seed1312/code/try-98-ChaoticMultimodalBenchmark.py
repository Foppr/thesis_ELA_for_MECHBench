import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Modified chaotic sinusoidal interference with altered frequencies
        wave_term = 0.0
        for i in range(self.dim):
            freq = (i % 5) + 3  # Slightly different frequency pattern
            decay = np.exp(-0.15 * i)  # Adjusted decay rate
            chaos_mod = np.sin(4 * np.pi * x_norm[i]) * np.cos(2.5 * np.pi * x_norm[i])  # Changed modulation
            wave_term += decay * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i]) * chaos_mod
        
        # Dynamic conditioning with altered scaling factors
        r = np.sqrt(np.sum(x_norm**2))
        cond_factor = 1.0 + 1.5 * np.sin(3.5 * np.pi * r)**2 * np.exp(-0.4 * r)  # Modified conditioning
        
        # Adjusted basin structure with enhanced depth variation
        rugged_term = 0.0
        for i in range(self.dim):
            depth_mod = 1.0 + 0.4 * np.sin(6 * np.pi * x_norm[i]) * np.cos(2.5 * np.pi * x_norm[i])  # Changed depth modulation
            rugged_term += depth_mod * (x_norm[i]**2 + 0.15 * np.sin(9 * np.pi * x_norm[i])**2)  # Increased sinusoidal component
        
        # Cross-term interactions with modified coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + (x_norm[i] + x_norm[j])**2)
                coupling = np.sin(2.5 * np.pi * dist) * np.cos(3.5 * np.pi * dist)  # Different coupling
                cross_term += coupling * np.exp(-dist * (1.2 + 0.15 * np.sin(4 * np.pi * dist)))  # Modified decay
        
        # Multi-scale chaotic component with adjusted frequencies
        multi_scale = 0.0
        for i in range(self.dim):
            freqs = [3, 4, 6, 8]  # Changed frequency set
            scale_factor = 1.0 / (i + 1.5)  # Modified scaling
            for f in freqs:
                multi_scale += scale_factor * np.sin(f * np.pi * x_norm[i]) * np.cos(f * np.pi * x_norm[i])
        
        # Combine all components with modified weighting
        dim_weight = 1.0 + 0.12 * self.dim + 0.06 * np.sin(3.5 * np.pi * self.dim)  # Adjusted weight
        result = dim_weight * (cond_factor * (0.65 * wave_term + 0.35 * rugged_term + 
                                             0.25 * cross_term + 0.35 * multi_scale))
        
        return result