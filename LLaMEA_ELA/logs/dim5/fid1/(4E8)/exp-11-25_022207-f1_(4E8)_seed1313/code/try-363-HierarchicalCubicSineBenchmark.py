import numpy as np

class HierarchicalCubicSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters for increased complexity
        self.cubic_weights = np.logspace(0.8, 5.0, min(30, dim))
        self.sine_frequencies = np.logspace(2.0, 6.0, min(30, dim))
        self.conditioning_factors = np.logspace(1.5, 8.0, min(25, dim))
        # Add chaotic coupling parameters with irregular spacing
        self.coupling_strengths = np.random.uniform(0.01, 3.0, min(30, dim))
        # Introduce irregular fractal exponents and noise scaling
        self.fractal_exponents = np.random.choice([2, 3, 4, 5, 6, 7, 8, 9], size=min(30, dim), p=[0.03, 0.1, 0.12, 0.18, 0.2, 0.18, 0.12, 0.07])
        self.noise_scalings = np.random.lognormal(0.0, 0.9, min(15, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced cubic polynomial components with chaotic weights and phase shifts
        for i in range(min(len(self.cubic_weights), self.dim)):
            weight = self.cubic_weights[i] * np.sin(4.0 * i + x_norm[i] + np.cos(2.0 * i))
            cubic_term = weight * (x_norm[i] ** 3)
            result += cubic_term
            
        # Sine modulation with chaotic frequencies and phase modulations
        sine_component = 0.0
        for i in range(min(len(self.sine_frequencies), self.dim)):
            freq = self.sine_frequencies[i] * np.cos(3.0 * i + x_norm[i])
            phase_shift = np.sin(1.0 * i + x_norm[i])
            sine_term = np.sin(freq * x_norm[i] + phase_shift)
            sine_component += sine_term
            
        # Chaotic conditioning-dependent scaling with irregular factors
        conditioning_term = 0.0
        for i in range(min(len(self.conditioning_factors), self.dim)):
            cond_factor = self.conditioning_factors[i] * (1.0 + 0.7 * np.sin(5.0 * i + x_norm[i]))
            conditioning_term += cond_factor * (x_norm[i] ** 2)
            
        # Multi-scale interaction terms with chaotic coupling and irregular strengths
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Chaotic coupling based on dimension indices and random factors with irregularity
                coupling_strength = self.coupling_strengths[i] * self.coupling_strengths[j] * np.sin(0.5 * (i + j) + np.cos(i - j))
                interaction = coupling_strength * np.sin(x_norm[i] * x_norm[j] + 0.2 * np.sin(i * j))
                interaction_term += interaction
                
        # Hierarchical structure with fractal-like nested scaling and irregular exponents
        hierarchical_term = 0.0
        for i in range(self.dim):
            # Fractal-like nested terms with varying exponents and noise modulation
            exponent = self.fractal_exponents[i]
            hierarchical_term += (0.7 + 0.3 * np.sin(2.0 * i)) * (x_norm[i] ** exponent)
                
        # Add enhanced chaotic noise component with irregular scaling
        noise_component = 0.0
        for i in range(min(len(self.noise_scalings), self.dim)):
            noise_scale = self.noise_scalings[i]
            noise_component += np.sin(20.0 * x_norm[i]) * np.random.uniform(-noise_scale, noise_scale)
            
        # Combine all components with enhanced weighting and irregular contributions
        result = result + 2.5 * sine_component + 1.0 * conditioning_term + 0.9 * interaction_term + 0.6 * hierarchical_term + 0.4 * noise_component
        
        return result