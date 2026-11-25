import numpy as np

class HierarchicalCubicSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Adaptive parameters based on dimensionality
        self.cubic_weights = np.linspace(0.5, 2.0, min(10, dim))
        self.sine_frequencies = np.logspace(0.5, 2.5, min(10, dim))
        self.conditioning_factors = np.linspace(1.0, 5.0, min(8, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Initialize result
        result = 0.0
        
        # Cubic polynomial components with adaptive weights
        for i in range(min(len(self.cubic_weights), self.dim)):
            weight = self.cubic_weights[i]
            cubic_term = weight * (x_norm[i] ** 3)
            result += cubic_term
            
        # Sine modulation with dimensionally varying frequencies
        sine_component = 0.0
        for i in range(min(len(self.sine_frequencies), self.dim)):
            freq = self.sine_frequencies[i]
            sine_term = np.sin(freq * x_norm[i])
            sine_component += sine_term
            
        # Add conditioning-dependent scaling
        conditioning_term = 0.0
        for i in range(min(len(self.conditioning_factors), self.dim)):
            cond_factor = self.conditioning_factors[i]
            conditioning_term += cond_factor * (x_norm[i] ** 2)
            
        # Multi-scale interaction terms
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Adaptive coupling based on dimension indices
                coupling_strength = 0.1 * (i + j) / (self.dim + 1)
                interaction = coupling_strength * np.sin(x_norm[i] * x_norm[j])
                interaction_term += interaction
                
        # Hierarchical structure with nested scaling
        hierarchical_term = 0.0
        for i in range(self.dim):
            # Nested cubic terms with increasing complexity
            if i % 2 == 0:
                hierarchical_term += 0.5 * (x_norm[i] ** 4)
            else:
                hierarchical_term += 0.3 * (x_norm[i] ** 5)
                
        # Combine all components with adaptive weighting
        result = result + 0.8 * sine_component + 0.3 * conditioning_term + 0.2 * interaction_term + 0.1 * hierarchical_term
        
        # Add noise with dimensionality-dependent amplitude
        noise_amplitude = 0.01 * (1.0 + 0.05 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise