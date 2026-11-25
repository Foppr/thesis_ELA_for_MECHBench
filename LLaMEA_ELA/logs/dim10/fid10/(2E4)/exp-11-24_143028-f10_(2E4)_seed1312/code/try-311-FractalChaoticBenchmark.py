import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced fractal parameters with higher dimensionality dependence
        self.fractal_dimensions = np.random.uniform(1.5, 2.8, dim)
        self.scale_factors = np.random.uniform(0.3, 1.5, dim)
        self.roughness_params = np.random.uniform(0.2, 0.8, dim)
        # Stronger chaotic perturbation parameters
        self.chaotic_amplitudes = np.random.uniform(0.3, 0.8, dim)
        self.chaotic_frequencies = np.random.uniform(3.0, 12.0, dim)
        # Increased interaction complexity
        self.interaction_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        np.fill_diagonal(self.interaction_weights, 0.0)
        # Enhanced basin parameters for greater ruggedness
        self.basin_depths = np.random.uniform(1.0, 3.0, dim)
        self.basin_spread = np.random.uniform(0.05, 0.3, dim)
        # Additional complexity terms
        self.frequency_modulators = np.random.uniform(0.5, 2.0, dim)
        self.amplitude_modulators = np.random.uniform(0.5, 1.5, dim)
        self.multi_scale_factors = np.random.uniform(0.1, 0.9, (dim, 4))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [0, 1] for fractal computation
        normalized_x = (x + 5.0) / 10.0
        
        # Compute enhanced fractal contributions with multi-scale self-similarity
        fractal_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Base fractal component with multiple scales and modulated frequencies
            fractal_component = 0.0
            for k in range(1, 8):  # More scales for increased complexity
                scale = self.scale_factors[i] * (2.0 ** (-k))
                freq = self.chaotic_frequencies[i] * (2.0 ** k) * self.frequency_modulators[i]
                # Fractal-like term with varying dimensionality and modulation
                fractal_component += scale * np.sin(freq * normalized_x[i])
            
            # Add enhanced chaotic perturbation
            chaotic_perturbation = self.chaotic_amplitudes[i] * np.sin(
                self.chaotic_frequencies[i] * (normalized_x[i] + 0.1 * np.sin(3.0 * normalized_x[i])) * self.amplitude_modulators[i]
            )
            
            # Add additional chaotic modulation
            additional_perturbation = 0.2 * np.sin(7.0 * normalized_x[i]) * np.cos(4.0 * normalized_x[i])
            
            # Combine all components
            fractal_values[i] = fractal_component + chaotic_perturbation + additional_perturbation
            
        # Compute enhanced fitness with multi-scale interaction terms
        fitness = 0.0
        for i in range(self.dim):
            # Enhanced basin effect with varying depth and spread
            basin_effect = self.basin_depths[i] * np.exp(-0.5 * ((normalized_x[i] - 0.5) / self.basin_spread[i])**2)
            
            # Multi-scale ruggedness term with more complex interactions
            ruggedness_term = 0.0
            for k in range(1, 6):
                ruggedness_term += (0.3 ** k) * np.sin(self.chaotic_frequencies[i] * (normalized_x[i] + k * 0.1 * self.frequency_modulators[i]))
            
            # Additional multi-scale fractal interaction terms
            fractal_interaction = 0.0
            for j in range(1, 4):
                fractal_interaction += (0.4 ** j) * np.sin(self.fractal_dimensions[i] * normalized_x[i] * j)
            
            # Combine with fractal values and basin effects
            fitness += (fractal_values[i] - basin_effect)**2 + ruggedness_term**2 + fractal_interaction**2
            
        # Add cross-dimensional interactions with enhanced fractal scaling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced interaction based on fractal dimension and coupling weights
                weight = np.abs(self.interaction_weights[i, j])
                # Fractal distance measure between dimensions with enhanced scaling
                fractal_distance = np.abs(fractal_values[i] - fractal_values[j])
                cross_term += weight * (fractal_distance ** self.fractal_dimensions[i]) * np.exp(-0.5 * fractal_distance**2) * np.cos(2.0 * fractal_distance)
                
        # Global scaling and additional complexity components with higher conditioning
        return fitness + 0.5 * cross_term + 0.15 * np.sum(np.abs(x)) + \
               0.2 * np.sum(np.sin(10.0 * x) * np.cos(5.0 * x)) + \
               0.1 * np.sum(np.sin(15.0 * x) * np.exp(-0.1 * x**2))