import numpy as np

class AsymmetricMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced periodic sinusoidal components with chaotic modulation
        periodic_term = 0.0
        for i in range(self.dim):
            freq = (i % 5) + 3
            amp = 1.0 / (i + 1)**1.5
            chaos_mod = np.sin(7 * np.pi * x_norm[i]) * np.cos(5 * np.pi * x_norm[i])
            periodic_term += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i]) * chaos_mod
        
        # Enhanced radial conditioning with chaotic scaling
        r = np.sqrt(np.sum(x_norm**2))
        asym_factor = 1.0 + 3.0 * (np.sin(3 * np.pi * r)**2) * (1.0 + 0.7 * np.cos(5 * np.pi * r)) * np.exp(-0.5 * r)
        
        # Enhanced asymmetric quadratic basin with chaotic weights
        asymmetric_basin = 0.0
        for i in range(self.dim):
            chaos_weight = 0.2 + 0.1 * np.sin(4 * np.pi * x_norm[i])
            if x_norm[i] >= 0:
                asymmetric_basin += chaos_weight * x_norm[i]**2
            else:
                asymmetric_basin += (0.3 + 0.05 * np.cos(3 * np.pi * x_norm[i])) * x_norm[i]**2
        
        # Enhanced interaction terms with chaotic decay and modulation
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                mod = np.sin(3 * np.pi * dist) * np.cos(2 * np.pi * dist)
                chaos_decay = np.exp(-dist * (1.0 + 0.3 * np.sin(6 * np.pi * dist)))
                interaction_term += chaos_decay * mod
        
        # Enhanced multi-modal component with chaotic depth and frequency
        multimodal_term = 0.0
        for i in range(self.dim):
            freq = (i % 4) + 2
            chaos_depth = 1.0 + 0.5 * np.sin(5 * np.pi * x_norm[i])
            multimodal_term += chaos_depth * np.sin(freq * np.pi * x_norm[i]) * np.cos(3 * freq * np.pi * x_norm[i])
        
        # Combine all terms with enhanced dynamic weighting
        dim_factor = 1.0 + 0.2 * self.dim + 0.05 * np.sin(2 * np.pi * self.dim)
        result = dim_factor * (asym_factor * (0.6 * r**2 + 0.4 * periodic_term + 
                                             0.3 * interaction_term + 0.5 * multimodal_term) + 
                              asymmetric_basin)
        
        return result