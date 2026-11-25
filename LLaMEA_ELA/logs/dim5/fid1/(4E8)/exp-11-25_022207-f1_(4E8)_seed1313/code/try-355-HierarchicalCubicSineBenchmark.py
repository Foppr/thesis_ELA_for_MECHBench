import numpy as np

class HierarchicalCubicSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters for increased complexity
        self.cubic_weights = np.logspace(0.5, 4.5, min(25, dim))
        self.sine_frequencies = np.logspace(1.8, 5.5, min(25, dim))
        self.conditioning_factors = np.logspace(1.2, 7.5, min(20, dim))
        # Add chaotic coupling parameters with irregular spacing
        self.coupling_strengths = np.random.uniform(0.02, 2.5, min(25, dim))
        # Introduce irregular fractal exponents and noise scaling
        self.fractal_exponents = np.random.choice([2, 3, 4, 5, 6, 7, 8], size=min(25, dim), p=[0.05, 0.1, 0.15, 0.2, 0.2, 0.2, 0.1])
        self.noise_scalings = np.random.lognormal(0.0, 0.7, min(10, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced cubic polynomial components with chaotic weights and phase shifts
        for i in range(min(len(self.cubic_weights), self.dim)):
            weight = self.cubic_weights[i] * np.sin(3.5 * i + x_norm[i] + np.cos(1.8 * i))
            cubic_term = weight * (x_norm[i] ** 3)
            result += cubic_term
            
        # Sine modulation with chaotic frequencies and phase modulations
        sine_component = 0.0
        for i in range(min(len(self.sine_frequencies), self.dim)):
            freq = self.sine_frequencies[i] * np.cos(2.5 * i + x_norm[i])
            phase_shift = np.sin(0.8 * i + x_norm[i])
            sine_term = np.sin(freq * x_norm[i] + phase_shift)
            sine_component += sine_term
            
        # Chaotic conditioning-dependent scaling with irregular factors
        conditioning_term = 0.0
        for i in range(min(len(self.conditioning_factors), self.dim)):
            cond_factor = self.conditioning_factors[i] * (1.0 + 0.6 * np.sin(4.5 * i + x_norm[i]))
            conditioning_term += cond_factor * (x_norm[i] ** 2)
            
        # Multi-scale interaction terms with chaotic coupling and irregular strengths
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Chaotic coupling based on dimension indices and random factors with irregularity
                coupling_strength = self.coupling_strengths[i] * self.coupling_strengths[j] * np.sin(0.4 * (i + j) + np.cos(i - j))
                interaction = coupling_strength * np.sin(x_norm[i] * x_norm[j] + 0.15 * np.sin(i * j))
                interaction_term += interaction
                
        # Hierarchical structure with fractal-like nested scaling and irregular exponents
        hierarchical_term = 0.0
        for i in range(self.dim):
            # Fractal-like nested terms with varying exponents and noise modulation
            exponent = self.fractal_exponents[i]
            hierarchical_term += (0.6 + 0.2 * np.sin(1.5 * i)) * (x_norm[i] ** exponent)
                
        # Add enhanced chaotic noise component with irregular scaling
        noise_component = 0.0
        for i in range(min(len(self.noise_scalings), self.dim)):
            noise_scale = self.noise_scalings[i]
            noise_component += np.sin(15.0 * x_norm[i]) * np.random.uniform(-noise_scale, noise_scale)
            
        # Combine all components with enhanced weighting and irregular contributions
        result = result + 2.0 * sine_component + 0.9 * conditioning_term + 0.8 * interaction_term + 0.5 * hierarchical_term + 0.3 * noise_component
        
        return result