import numpy as np

class HierarchicalCubicSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters for increased complexity
        self.cubic_weights = np.logspace(0.5, 3.5, min(15, dim))
        self.sine_frequencies = np.logspace(1.0, 4.0, min(15, dim))
        self.conditioning_factors = np.logspace(1.2, 6.0, min(12, dim))
        # Add chaotic coupling parameters
        self.coupling_strengths = np.random.uniform(0.1, 1.5, min(15, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced cubic polynomial components with chaotic weights
        for i in range(min(len(self.cubic_weights), self.dim)):
            weight = self.cubic_weights[i] * np.sin(2.5 * i + x_norm[i])
            cubic_term = weight * (x_norm[i] ** 3)
            result += cubic_term
            
        # Sine modulation with chaotic frequencies
        sine_component = 0.0
        for i in range(min(len(self.sine_frequencies), self.dim)):
            freq = self.sine_frequencies[i] * np.cos(1.8 * i + x_norm[i])
            sine_term = np.sin(freq * x_norm[i])
            sine_component += sine_term
            
        # Chaotic conditioning-dependent scaling
        conditioning_term = 0.0
        for i in range(min(len(self.conditioning_factors), self.dim)):
            cond_factor = self.conditioning_factors[i] * (1.0 + 0.3 * np.sin(3.2 * i))
            conditioning_term += cond_factor * (x_norm[i] ** 2)
            
        # Multi-scale interaction terms with chaotic coupling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Chaotic coupling based on dimension indices and random factors
                coupling_strength = self.coupling_strengths[i] * self.coupling_strengths[j] * np.sin(0.5 * (i + j))
                interaction = coupling_strength * np.sin(x_norm[i] * x_norm[j])
                interaction_term += interaction
                
        # Hierarchical structure with fractal-like nested scaling
        hierarchical_term = 0.0
        for i in range(self.dim):
            # Fractal-like nested terms with varying exponents
            if i % 4 == 0:
                hierarchical_term += 0.8 * (x_norm[i] ** 5)
            elif i % 4 == 1:
                hierarchical_term += 0.6 * (x_norm[i] ** 6)
            elif i % 4 == 2:
                hierarchical_term += 0.4 * (x_norm[i] ** 7)
            else:
                hierarchical_term += 0.2 * (x_norm[i] ** 8)
                
        # Add chaotic noise component
        noise_component = 0.0
        for i in range(min(5, self.dim)):
            noise_component += np.sin(10.0 * x_norm[i]) * np.random.uniform(-0.1, 0.1)
            
        # Combine all components with enhanced weighting
        result = result + 1.2 * sine_component + 0.7 * conditioning_term + 0.6 * interaction_term + 0.3 * hierarchical_term + 0.1 * noise_component
        
        return result