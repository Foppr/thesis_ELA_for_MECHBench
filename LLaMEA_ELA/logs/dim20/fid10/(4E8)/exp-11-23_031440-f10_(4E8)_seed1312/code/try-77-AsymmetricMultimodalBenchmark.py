import numpy as np

class AsymmetricMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Periodic sinusoidal components with varying frequencies and amplitudes
        periodic_term = 0.0
        for i in range(self.dim):
            freq = (i % 5) + 3
            amp = 1.0 / (i + 1)**1.5
            periodic_term += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Radial conditioning with enhanced chaotic scaling
        r = np.sqrt(np.sum(x_norm**2))
        asym_factor = 1.0 + 3.0 * (np.sin(3 * np.pi * r)**2) * (1.0 + 0.7 * np.cos(4 * np.pi * r))
        
        # Asymmetric quadratic basin with modified weights
        asymmetric_basin = 0.0
        for i in range(self.dim):
            if x_norm[i] >= 0:
                asymmetric_basin += 0.15 * x_norm[i]**2
            else:
                asymmetric_basin += 0.35 * x_norm[i]**2
        
        # Enhanced interaction terms with chaotic modulation
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                mod = np.sin(2 * np.pi * dist) * np.cos(np.pi * dist)
                interaction_term += np.exp(-dist**1.5) * mod
        
        # Multi-modal component with increased depth and frequency
        multimodal_term = 0.0
        for i in range(self.dim):
            freq = (i % 4) + 2
            multimodal_term += np.sin(freq * np.pi * x_norm[i]) * np.cos(3 * freq * np.pi * x_norm[i])
        
        # Combine all terms with dynamic weighting based on dimensionality
        dim_factor = 1.0 + 0.15 * self.dim
        result = dim_factor * (asym_factor * (0.6 * r**2 + 0.4 * periodic_term + 
                                             0.3 * interaction_term + 0.5 * multimodal_term) + 
                              asymmetric_basin)
        
        return result