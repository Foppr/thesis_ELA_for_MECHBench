import numpy as np

class AsymmetricMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced periodic sinusoidal components with chaotic frequency modulation
        periodic_term = 0.0
        for i in range(self.dim):
            freq = (i % 7) + 5 + 2 * np.sin(0.5 * i * np.pi)
            amp = 1.5 / (i + 1)**1.8
            periodic_term += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Radial conditioning with chaotic scaling and multiple basin centers
        r = np.sqrt(np.sum(x_norm**2))
        asym_factor = 1.0 + 4.0 * (np.sin(5 * np.pi * r)**2) * (1.0 + 0.8 * np.cos(6 * np.pi * r)) * (1.0 + 0.3 * np.sin(7 * np.pi * r))
        
        # Asymmetric quadratic basin with dynamic weights and chaotic modulation
        asymmetric_basin = 0.0
        for i in range(self.dim):
            if x_norm[i] >= 0:
                weight = 0.2 + 0.1 * np.sin(3 * i * np.pi)
                asymmetric_basin += weight * x_norm[i]**2
            else:
                weight = 0.4 + 0.2 * np.cos(2 * i * np.pi)
                asymmetric_basin += weight * x_norm[i]**2
        
        # Enhanced interaction terms with chaotic modulation and multi-scale effects
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                mod1 = np.sin(3 * np.pi * dist) * np.cos(np.pi * dist)
                mod2 = np.cos(2 * np.pi * dist) * np.sin(4 * np.pi * dist)
                interaction_term += np.exp(-dist**2.0) * (mod1 + 0.5 * mod2) * (1.0 + 0.2 * np.sin(5 * np.pi * dist))
        
        # Multi-modal component with increased depth, frequency, and chaotic interference
        multimodal_term = 0.0
        for i in range(self.dim):
            freq = (i % 6) + 3 + 1.5 * np.cos(0.7 * i * np.pi)
            multimodal_term += np.sin(freq * np.pi * x_norm[i]) * np.cos(4 * freq * np.pi * x_norm[i]) * (1.0 + 0.4 * np.sin(2 * np.pi * x_norm[i]))
        
        # Additional chaotic cross-terms with fractal-like behavior
        chaos_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(x_norm[i] - x_norm[j])
                    chaos_term += np.sin(10 * np.pi * dist) * np.cos(8 * np.pi * dist) * (1.0 + 0.3 * np.sin(6 * np.pi * x_norm[i]))
        
        # Combine all terms with dynamic weighting based on dimensionality and chaos
        dim_factor = 1.0 + 0.25 * self.dim + 0.1 * np.sin(0.3 * self.dim * np.pi)
        result = dim_factor * (asym_factor * (0.7 * r**2 + 0.3 * periodic_term + 
                                             0.4 * interaction_term + 0.6 * multimodal_term + 
                                             0.2 * chaos_term) + 
                              asymmetric_basin)
        
        return result