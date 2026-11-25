import numpy as np

class HierarchicalCubicSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced adaptive parameters for increased complexity
        self.cubic_weights = np.linspace(0.3, 2.5, min(12, dim))
        self.sine_frequencies = np.logspace(0.7, 3.0, min(12, dim))
        self.conditioning_factors = np.linspace(1.5, 6.0, min(10, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced cubic polynomial components with adaptive weights
        for i in range(min(len(self.cubic_weights), self.dim)):
            weight = self.cubic_weights[i]
            cubic_term = weight * (x_norm[i] ** 3)
            result += cubic_term
            
        # Sine modulation with enhanced frequencies
        sine_component = 0.0
        for i in range(min(len(self.sine_frequencies), self.dim)):
            freq = self.sine_frequencies[i]
            sine_term = np.sin(freq * x_norm[i])
            sine_component += sine_term
            
        # Enhanced conditioning-dependent scaling
        conditioning_term = 0.0
        for i in range(min(len(self.conditioning_factors), self.dim)):
            cond_factor = self.conditioning_factors[i]
            conditioning_term += cond_factor * (x_norm[i] ** 2)
            
        # Multi-scale interaction terms with increased coupling strength
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Enhanced coupling based on dimension indices
                coupling_strength = 0.15 * (i + j) / (self.dim + 1)
                interaction = coupling_strength * np.sin(x_norm[i] * x_norm[j])
                interaction_term += interaction
                
        # Hierarchical structure with enhanced nested scaling
        hierarchical_term = 0.0
        for i in range(self.dim):
            # Enhanced nested terms with higher-order polynomials
            if i % 3 == 0:
                hierarchical_term += 0.6 * (x_norm[i] ** 4)
            elif i % 3 == 1:
                hierarchical_term += 0.4 * (x_norm[i] ** 5)
            else:
                hierarchical_term += 0.2 * (x_norm[i] ** 6)
                
        # Combine all components with adjusted weighting
        result = result + 0.9 * sine_component + 0.4 * conditioning_term + 0.3 * interaction_term + 0.15 * hierarchical_term
        
        # Add enhanced noise with dimensionality-dependent amplitude
        noise_amplitude = 0.015 * (1.0 + 0.07 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise