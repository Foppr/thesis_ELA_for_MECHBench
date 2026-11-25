import numpy as np

class NestedOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random parameters for nested oscillations
        self.oscillation_freq = np.random.rand(dim) * 10.0 + 1.0
        self.oscillation_ampl = np.random.rand(dim) * 2.0 + 1.0
        self.conditioning_factors = np.random.rand(dim) * 5.0 + 1.0
        self.cross_dim_coupling = np.random.randn(dim, dim) * 0.3
        # Adaptive scaling parameters
        self.adaptive_scale = np.random.rand() * 2.0 + 1.0
        self.nesting_depth = np.random.randint(2, 6)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Nested sinusoidal component with varying frequencies and amplitudes
        nested_sum = 0.0
        for i in range(self.dim):
            oscillation = 0.0
            for depth in range(1, self.nesting_depth + 1):
                freq = self.oscillation_freq[i] * (depth ** 1.5)
                ampl = self.oscillation_ampl[i] / (depth ** 0.5)
                oscillation += ampl * np.sin(freq * x_norm[i])
            nested_sum += oscillation
        
        # Adaptive conditioning component
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += self.conditioning_factors[i] * x_norm[i]**2
        
        # Cross-dimensional coupling
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_coupling += self.cross_dim_coupling[i, j] * x_norm[i] * x_norm[j]
        
        # Additional nonlinear interaction terms
        nonlinear_interaction = 0.0
        for i in range(self.dim):
            nonlinear_interaction += (x_norm[i]**3 + 0.5 * x_norm[i]**4 + 
                                   np.sin(2 * x_norm[i]) * np.cos(x_norm[(i+1) % self.dim]))
        
        # Combine all components with adaptive scaling
        result = (self.adaptive_scale * nested_sum + 
                 0.3 * conditioning + 
                 0.2 * cross_coupling + 
                 0.1 * nonlinear_interaction + 
                 2.0)
        
        return result