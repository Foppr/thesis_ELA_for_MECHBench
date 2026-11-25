import numpy as np

class HierarchicalFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal parameters
        self.fractal_dims = np.random.uniform(1.1, 2.9, dim)
        self.scale_factors = np.random.uniform(0.1, 2.0, dim)
        self.rotation_angles = np.random.uniform(0, 2*np.pi, dim)
        self.correlation_strengths = np.random.uniform(0.1, 0.9, dim)
        self.hurst_exponents = np.random.uniform(0.1, 0.9, dim)
        self.fractal_weights = np.random.dirichlet(np.ones(dim))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Hierarchical fractal mapping with multiple scales
        result = 0.0
        for i in range(self.dim):
            # Fractal component with self-similarity
            fractal_value = 0.0
            for j in range(5):
                scale = self.scale_factors[i] * (2 ** (-j))
                freq = 2 ** j
                fractal_value += scale * np.sin(freq * x_norm[i] + self.rotation_angles[i])
            
            # Adaptive dimensionality reduction effect
            dim_reduction = 1.0 / (1.0 + np.exp(-self.correlation_strengths[i] * x_norm[i]))
            
            # Hurst parameter influence for long-range correlation
            hurst_effect = np.power(np.abs(x_norm[i]), self.hurst_exponents[i])
            
            # Combine components with fractal weights
            result += self.fractal_weights[i] * fractal_value * dim_reduction * hurst_effect
            
        # Multi-scale interaction terms
        interaction_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-interaction
                # Self-similar correlation structure
                corr_strength = self.correlation_strengths[i] * self.correlation_strengths[j]
                interaction = np.sin(corr_strength * (x_norm[i] - x_norm[j]))
                interaction_terms += interaction
                
        # Add noise and scale the result
        noise = np.random.normal(0, 0.01)
        total = result + 0.5 * interaction_terms + noise
        
        # Apply non-linear transformation for additional complexity
        total = np.tanh(total) * (1.0 + 0.1 * np.sin(np.sum(x_norm**2)))
        
        return total