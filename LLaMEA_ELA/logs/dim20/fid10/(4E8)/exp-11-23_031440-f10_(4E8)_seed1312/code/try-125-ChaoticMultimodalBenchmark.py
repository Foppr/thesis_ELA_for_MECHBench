import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sinusoidal interference with multiple frequency components
        chaotic_term = 0.0
        for i in range(self.dim):
            freqs = [2, 3, 5, 7, 11]
            for j, freq in enumerate(freqs):
                # Add chaotic modulation with varying amplitudes and phases
                amp = 1.0 / (j + 1)
                phase = np.pi * i * (j + 1) / self.dim
                chaotic_term += amp * np.sin(freq * np.pi * x_norm[i] + phase) * \
                               np.cos(freq * np.pi * x_norm[i] + phase) * \
                               np.sin(3 * np.pi * x_norm[i]) * \
                               np.cos(2 * np.pi * x_norm[i])
        
        # Dynamic conditioning with exponential decay and chaotic scaling
        r = np.sqrt(np.sum(x_norm**2))
        cond_factor = 1.0 + 3.0 * np.sin(5 * np.pi * r)**2 * np.exp(-0.3 * r)
        
        # Enhanced basin structure with multiple depth variations
        basin_term = 0.0
        for i in range(self.dim):
            # Multi-scale basin depth modulation
            depth_mod1 = 1.0 + 0.5 * np.sin(8 * np.pi * x_norm[i])
            depth_mod2 = 1.0 + 0.3 * np.cos(6 * np.pi * x_norm[i])
            depth_mod3 = 1.0 + 0.4 * np.sin(4 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
            basin_term += depth_mod1 * depth_mod2 * depth_mod3 * (x_norm[i]**2 + 0.1 * np.sin(15 * np.pi * x_norm[i])**2)
        
        # Cross-term interactions with chaotic coupling and variable coupling strength
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + (x_norm[i] + x_norm[j])**2)
                # Enhanced chaotic coupling with multiple interaction terms
                coupling1 = np.sin(4 * np.pi * dist) * np.cos(5 * np.pi * dist)
                coupling2 = np.sin(6 * np.pi * dist) * np.cos(3 * np.pi * dist)
                coupling3 = np.sin(2 * np.pi * dist) * np.cos(7 * np.pi * dist)
                coupling_strength = 1.0 + 0.5 * np.sin(8 * np.pi * (i + j))
                cross_term += coupling_strength * (coupling1 + coupling2 + coupling3) * \
                             np.exp(-dist * (1.0 + 0.3 * np.sin(6 * np.pi * dist)))
        
        # Fractal-like self-similar structure with multiple scales
        fractal_term = 0.0
        for i in range(self.dim):
            scale_factors = [1.0, 0.5, 0.25, 0.125]
            for k, scale in enumerate(scale_factors):
                freq = (k + 1) * 4
                fractal_term += scale * np.sin(freq * np.pi * x_norm[i]) * \
                               np.cos(freq * np.pi * x_norm[i]) * \
                               np.sin(2 * np.pi * x_norm[i]**2)
        
        # Combine all components with adaptive weighting based on dimensionality and chaos
        dim_weight = 1.0 + 0.2 * self.dim + 0.1 * np.sin(4 * np.pi * self.dim)
        chaos_factor = 1.0 + 0.5 * np.mean(np.abs(x_norm)) * np.sin(7 * np.pi * r)
        
        # Modified coefficients and scaling factors for better benchmark performance
        result = dim_weight * chaos_factor * (0.65 * chaotic_term + 0.22 * basin_term + 
                                             0.18 * cross_term + 0.05 * fractal_term)
        
        return result