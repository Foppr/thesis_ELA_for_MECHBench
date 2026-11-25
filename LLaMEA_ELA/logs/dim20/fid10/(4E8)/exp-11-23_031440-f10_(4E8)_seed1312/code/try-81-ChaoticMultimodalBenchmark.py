import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial component with chaotic sine waves and multiple local minima
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = 0.7 * r**3 + 0.4 * np.sin(12 * np.pi * r) + 0.3 * np.cos(18 * np.pi * r) + 0.2 * np.sin(25 * np.pi * r)
        
        # Augmented periodic interference patterns with chaotic frequencies
        interference = 0.0
        for i in range(self.dim):
            freq = (i % 7) + 3  # Increased frequency range
            interference += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i]) * np.exp(-0.5 * (x_norm[i] - 0.3)**2)
        
        # Dynamic conditioning with chaotic scaling factor
        condition_factor = 1.0 + 5.0 * np.exp(-0.3 * r**2) * np.sin(7 * np.pi * r)**2
        
        # Multi-scale sinusoidal components with chaotic amplitudes and phases
        multiscale = 0.0
        for i in range(self.dim):
            amp = 1.5 / (1.0 + 0.3 * i + 0.1 * np.sin(5 * np.pi * i))  # Chaotic amplitude modulation
            phase = np.pi * i / self.dim + 0.5 * np.sin(3 * np.pi * i)  # Chaotic phase modulation
            freq = 2**(i % 6) + 0.5 * np.sin(4 * np.pi * i)  # Chaotic frequency progression
            multiscale += amp * np.sin(freq * x_norm[i] + phase)
        
        # Cross-term interactions with chaotic weighting and multi-scale coupling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                weight = np.exp(-dist**2) * (1 + 0.3 * np.sin(10 * np.pi * dist))  # Chaotic weighting
                cross_terms += weight * np.sin(6 * np.pi * dist) * np.cos(5 * np.pi * dist)
        
        # Enhanced basin structure with chaotic depth variations and multiple basins
        basin_depth = 0.0
        for i in range(self.dim):
            depth = 0.7 * (1 + np.tanh(3 * x_norm[i])) + 0.2 * np.sin(9 * np.pi * x_norm[i])**2
            basin_depth += depth * np.sin(8 * np.pi * x_norm[i])**3
        
        # Additional chaotic noise component
        noise = 0.1 * np.random.rand() * np.sum(np.sin(15 * x_norm)**2)
        
        # Combine all components with adjusted weights for maximum chaos and difficulty
        result = condition_factor * (radial_term + 0.4 * interference + 0.3 * multiscale + 
                                   0.2 * cross_terms + 0.15 * basin_depth) + noise
        
        return result