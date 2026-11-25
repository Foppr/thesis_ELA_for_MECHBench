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
            freq = (i % 4) + 2
            amp = 1.0 / (i + 1)
            periodic_term += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Radial conditioning with asymmetric scaling
        r = np.sqrt(np.sum(x_norm**2))
        asym_factor = 1.0 + 2.0 * (np.sin(2 * np.pi * r)**2) * (1.0 + 0.5 * np.cos(3 * np.pi * r))
        
        # Asymmetric quadratic basin with different weights for positive and negative regions
        asymmetric_basin = 0.0
        for i in range(self.dim):
            if x_norm[i] >= 0:
                asymmetric_basin += 0.2 * x_norm[i]**2
            else:
                asymmetric_basin += 0.3 * x_norm[i]**2
        
        # Interaction terms with exponential decay and sinusoidal modulation
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                mod = np.sin(np.pi * dist)
                interaction_term += np.exp(-dist) * mod
        
        # Multi-modal component with varying depth and frequency
        multimodal_term = 0.0
        for i in range(self.dim):
            freq = (i % 3) + 1
            multimodal_term += np.sin(freq * np.pi * x_norm[i]) * np.cos(2 * freq * np.pi * x_norm[i])
        
        # Combine all terms with dynamic weighting based on dimensionality
        dim_factor = 1.0 + 0.1 * self.dim
        result = dim_factor * (asym_factor * (0.5 * r**2 + 0.3 * periodic_term + 
                                             0.2 * interaction_term + 0.4 * multimodal_term) + 
                              asymmetric_basin)
        
        return result