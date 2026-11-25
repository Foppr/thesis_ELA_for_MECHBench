import numpy as np

class HierarchicalCubicSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced adaptive parameters for increased complexity and better conditioning
        self.cubic_weights = np.linspace(0.3, 2.8, min(12, dim))
        self.sine_frequencies = np.logspace(0.9, 3.5, min(12, dim))
        self.conditioning_factors = np.linspace(2.0, 8.0, min(10, dim))
        # Additional fractal-like parameters
        self.fractal_exponents = np.linspace(1.2, 2.5, min(8, dim))
        self.interaction_strengths = np.logspace(-1.0, 0.5, min(10, dim))
        
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
            
        # Multi-scale interaction terms with increased coupling strength and fractal structure
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Fractal-like coupling based on dimension indices and interaction strengths
                coupling_strength = self.interaction_strengths[min(i, len(self.interaction_strengths)-1)] * \
                                   (i + j) / (self.dim + 1)
                # Add fractal modulation to interactions
                fractal_mod = np.sin(np.pi * (x_norm[i] + x_norm[j]) / 2.0) ** self.fractal_exponents[min(i, len(self.fractal_exponents)-1)]
                interaction = coupling_strength * np.sin(x_norm[i] * x_norm[j]) * fractal_mod
                interaction_term += interaction
                
        # Hierarchical structure with enhanced nested scaling and nonlinearity
        hierarchical_term = 0.0
        for i in range(self.dim):
            # Enhanced nested terms with higher-order polynomials and fractal exponents
            if i % 4 == 0:
                hierarchical_term += 0.8 * (x_norm[i] ** 4)
            elif i % 4 == 1:
                hierarchical_term += 0.6 * (x_norm[i] ** 5)
            elif i % 4 == 2:
                hierarchical_term += 0.4 * (x_norm[i] ** 6)
            else:
                # Add fractal-like nonlinearity
                fractal_exp = self.fractal_exponents[min(i, len(self.fractal_exponents)-1)]
                hierarchical_term += 0.3 * np.abs(x_norm[i]) ** (2.0 + fractal_exp)
                
        # Combine all components with adjusted weighting
        result = result + 1.2 * sine_component + 0.6 * conditioning_term + 0.5 * interaction_term + 0.3 * hierarchical_term
        
        # Add enhanced noise with dimensionality-dependent amplitude and fractal characteristics
        noise_amplitude = 0.03 * (1.0 + 0.1 * self.dim)
        # Fractal noise component
        fractal_noise = np.sin(np.pi * np.random.rand()) * noise_amplitude
        noise = fractal_noise + 0.01 * np.random.randn()
        
        return result + noise