import numpy as np

class NestedHyperbolicInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Hyperbolic scaling factors with exponential growth for increased conditioning
        self.hyperbolic_factors = np.logspace(1.0, 3.0, min(12, dim)) * 1.5
        # Dynamic conditioning gradients with varying steepness across dimensions
        self.conditioning_gradients = np.linspace(0.8, 3.2, min(10, dim)) * 1.3
        # Interference pattern coefficients for cross-dimensional coupling
        self.interference_coeffs = np.random.uniform(0.5, 2.0, min(8, dim)) * 1.1
        # Nested well depths with logarithmic scaling to create multiple hierarchy levels
        self.well_depths = np.logspace(0.5, 2.5, min(6, dim)) * 0.8
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Nested hyperbolic paraboloid wells with varying depths and curvatures
        hyperbolic_term = 0.0
        for i in range(min(len(self.hyperbolic_factors), self.dim)):
            factor = self.hyperbolic_factors[i]
            # Hyperbolic term with nested structure and variable steepness
            hyperbolic_val = factor * (x_norm[i] ** 2) * np.log(1.0 + 0.5 * abs(x_norm[i]))
            hyperbolic_term += hyperbolic_val
            
        # Dynamic conditioning gradients with varying impact per dimension
        conditioning_term = 0.0
        for i in range(min(len(self.conditioning_gradients), self.dim)):
            gradient = self.conditioning_gradients[i]
            # Conditioning term with cubic modulation and dynamic scaling
            conditioning_val = gradient * (x_norm[i] ** 3) * np.sin(3.0 * x_norm[i])
            conditioning_term += conditioning_val
            
        # Cross-dimensional interference patterns with coupling strength
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coeff = self.interference_coeffs[i % len(self.interference_coeffs)]
                # Interference term with phase-shifted sinusoidal coupling
                interference_val = coeff * x_norm[i] * x_norm[j] * np.cos(2.0 * (x_norm[i] + x_norm[j]))
                interference_term += interference_val
                
        # Multi-level nested wells with different depth scaling and positioning
        nested_well_term = 0.0
        for i in range(self.dim):
            depth = self.well_depths[i % len(self.well_depths)]
            # Nested well structure with multiple local minima at different positions
            well_pos = 2.0 * np.sin(0.5 * (i + 1) * np.pi / self.dim)
            distance = x_norm[i] - well_pos
            # Multi-hierarchical well with increasing complexity in higher dimensions
            well_val = depth * (distance ** 4) + 0.3 * (distance ** 6) + 0.05 * (distance ** 8)
            nested_well_term += well_val
            
        # Combined terms with adjusted weights for balanced multimodality and conditioning
        result = 0.8 * hyperbolic_term + 0.7 * conditioning_term + 0.6 * interference_term + 0.5 * nested_well_term
        
        # Add adaptive noise with dimensionality-dependent amplitude
        noise_amplitude = 0.03 * (1.0 + 0.05 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise