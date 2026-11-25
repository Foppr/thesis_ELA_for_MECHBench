import numpy as np

class NestedOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random parameters for nested oscillations
        self.oscillation_freq = np.random.rand(dim) * 10.0 + 1.0
        self.oscillation_ampl = np.random.rand(dim) * 2.0 + 1.0
        self.conditioning_factors = np.random.rand(dim) * 5.0 + 1.0
        self.cross_dim_coupling = np.random.randn(dim, dim) * 0.5
        # Adaptive scaling parameters
        self.adaptive_scale = np.random.rand() * 2.0 + 1.0
        self.nesting_depth = np.random.randint(2, 6)
        # Enhanced fractal-like behavior
        self.fractal_exponent = np.random.rand(dim) * 0.8 + 0.3
        self.phase_shifts = np.random.rand(dim) * np.pi * 2
        # Additional complexity parameters
        self.nonlinear_weight = np.random.rand() * 0.5 + 0.5
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Nested sinusoidal component with varying frequencies and amplitudes
        nested_sum = 0.0
        for i in range(self.dim):
            oscillation = 0.0
            for depth in range(1, self.nesting_depth + 1):
                freq = self.oscillation_freq[i] * (depth ** 1.7)
                ampl = self.oscillation_ampl[i] / (depth ** 0.7)
                phase = self.phase_shifts[i] * depth
                oscillation += ampl * np.sin(freq * x_norm[i] + phase)
            nested_sum += oscillation
        
        # Fractal-like conditioning component with enhanced nonlinearity
        fractal_conditioning = 0.0
        for i in range(self.dim):
            fractal_conditioning += self.conditioning_factors[i] * (x_norm[i]**2) ** (1.0 + self.fractal_exponent[i] * 0.7)
        
        # Cross-dimensional coupling with dynamic weights and enhanced interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    weight = self.cross_dim_coupling[i, j] * (1.0 + 0.7 * np.sin(x_norm[i]) * np.cos(x_norm[j]))
                    cross_coupling += weight * x_norm[i] * x_norm[j]
        
        # Additional nonlinear interaction terms with enhanced complexity
        nonlinear_interaction = 0.0
        for i in range(self.dim):
            nonlinear_interaction += (self.nonlinear_weight * (x_norm[i]**3 + 0.3 * x_norm[i]**4 + 
                                   np.sin(2.5 * x_norm[i]) * np.cos(x_norm[(i+1) % self.dim]) +
                                   0.15 * np.sin(6 * x_norm[i]) * np.tanh(x_norm[(i+2) % self.dim])))
        
        # Combine all components with adaptive scaling
        result = (self.adaptive_scale * nested_sum + 
                 0.4 * fractal_conditioning + 
                 0.3 * cross_coupling + 
                 0.2 * nonlinear_interaction + 
                 2.5)
        
        return result