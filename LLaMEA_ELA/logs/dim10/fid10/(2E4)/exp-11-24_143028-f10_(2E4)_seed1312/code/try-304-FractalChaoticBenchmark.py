import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal parameters with dimension-dependent scaling
        self.fractal_dimensions = np.random.uniform(1.1, 2.9, dim)
        self.scale_factors = np.random.uniform(0.5, 2.0, dim)
        self.roughness_params = np.random.uniform(0.1, 0.9, dim)
        # Chaotic perturbation parameters
        self.chaotic_amplitudes = np.random.uniform(0.1, 0.5, dim)
        self.chaotic_frequencies = np.random.uniform(2.0, 8.0, dim)
        # Multi-scale interaction weights
        self.interaction_weights = np.random.uniform(-0.3, 0.3, (dim, dim))
        np.fill_diagonal(self.interaction_weights, 0.0)
        # Fractal basin parameters for varying ruggedness
        self.basin_depths = np.random.uniform(0.5, 2.0, dim)
        self.basin_spread = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [0, 1] for fractal computation
        normalized_x = (x + 5.0) / 10.0
        
        # Compute fractal contributions with multi-scale self-similarity
        fractal_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Base fractal component using fractional Brownian motion approximation
            fractal_component = 0.0
            for k in range(1, 6):  # Multi-scale summation
                scale = self.scale_factors[i] * (2.0 ** (-k))
                freq = self.chaotic_frequencies[i] * (2.0 ** k)
                # Fractal-like term with varying dimensionality
                fractal_component += scale * np.sin(freq * normalized_x[i])
            
            # Add chaotic perturbation
            chaotic_perturbation = self.chaotic_amplitudes[i] * np.sin(
                self.chaotic_frequencies[i] * (normalized_x[i] + 0.1 * np.sin(3.0 * normalized_x[i]))
            )
            
            # Combine fractal and chaotic components
            fractal_values[i] = fractal_component + chaotic_perturbation
            
        # Compute fitness with multi-scale interaction terms
        fitness = 0.0
        for i in range(self.dim):
            # Basin effect with varying depth and spread
            basin_effect = self.basin_depths[i] * np.exp(-0.5 * ((normalized_x[i] - 0.5) / self.basin_spread[i])**2)
            
            # Multi-scale ruggedness term
            ruggedness_term = 0.0
            for k in range(1, 4):
                ruggedness_term += (0.5 ** k) * np.sin(self.chaotic_frequencies[i] * (normalized_x[i] + k * 0.1))
            
            # Combine with fractal values and basin effects
            fitness += (fractal_values[i] - basin_effect)**2 + ruggedness_term**2
            
        # Add cross-dimensional interactions with fractal scaling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction based on fractal dimension and coupling weights
                weight = np.abs(self.interaction_weights[i, j])
                # Fractal distance measure between dimensions
                fractal_distance = np.abs(fractal_values[i] - fractal_values[j])
                cross_term += weight * (fractal_distance ** self.fractal_dimensions[i]) * np.exp(-0.5 * fractal_distance**2)
                
        # Global scaling and additional complexity components
        return fitness + 0.3 * cross_term + 0.1 * np.sum(np.abs(x)) + \
               0.05 * np.sum(np.sin(10.0 * x) * np.cos(5.0 * x))