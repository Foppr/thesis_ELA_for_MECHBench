import numpy as np

class HierarchicalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random parameters for each dimension
        self.frequency_params = np.random.uniform(1.0, 4.0, dim)
        self.amplitude_params = np.random.uniform(0.5, 2.0, dim)
        self.conditioning_params = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with multiple nested optima
        radius = np.sqrt(np.sum(x_norm**2))
        radial_term = np.sin(2 * np.pi * radius) * np.exp(-self.dim * radius**2)
        
        # Nested sinusoidal patterns with adaptive frequencies
        nested_terms = 0.0
        for i in range(self.dim):
            freq = self.frequency_params[i] * (1.0 + 0.5 * np.sin(0.5 * np.pi * i))
            amp = self.amplitude_params[i] * (1.0 + 0.3 * np.cos(0.3 * np.pi * i))
            nested_terms += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Adaptive conditioning based on dimension
        conditioning_term = 0.0
        for i in range(self.dim):
            cond_factor = self.conditioning_params[i] * (1.0 + 0.2 * np.sin(0.7 * np.pi * i))
            conditioning_term += cond_factor * x_norm[i]**2
        
        # Multi-scale interaction terms
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                interaction_term += np.exp(-dist**2) * np.sin(3 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Global structure with periodic modulation
        global_modulation = 1.0 + 0.3 * np.sin(0.2 * np.pi * radius)
        
        # Combine all terms
        result = (nested_terms + conditioning_term + interaction_term + radial_term) * global_modulation
        
        # Add dimensionality-dependent bias
        bias = 0.1 * self.dim * np.sum(np.sin(x_norm))
        
        return result + bias