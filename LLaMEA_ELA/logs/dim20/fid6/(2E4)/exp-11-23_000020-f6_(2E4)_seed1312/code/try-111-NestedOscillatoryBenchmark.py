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
        # Fractal-like enhancement parameters
        self.fractal_exponent = np.random.rand(dim) * 0.5 + 0.5
        self.phase_shifts = np.random.rand(dim) * np.pi * 2
        
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
                phase = self.phase_shifts[i] * depth
                oscillation += ampl * np.sin(freq * x_norm[i] + phase)
            nested_sum += oscillation
        
        # Fractal-like conditioning component
        fractal_conditioning = 0.0
        for i in range(self.dim):
            fractal_conditioning += self.conditioning_factors[i] * (x_norm[i]**2) ** (1.0 + self.fractal_exponent[i] * 0.5)
        
        # Cross-dimensional coupling with dynamic weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    weight = self.cross_dim_coupling[i, j] * (1.0 + 0.5 * np.sin(x_norm[i]))
                    cross_coupling += weight * x_norm[i] * x_norm[j]
        
        # Additional nonlinear interaction terms with enhanced complexity
        nonlinear_interaction = 0.0
        for i in range(self.dim):
            nonlinear_interaction += (x_norm[i]**3 + 0.5 * x_norm[i]**4 + 
                                   np.sin(2 * x_norm[i]) * np.cos(x_norm[(i+1) % self.dim]) +
                                   0.1 * np.sin(5 * x_norm[i]) * np.tanh(x_norm[(i+2) % self.dim]))
        
        # Combine all components with adaptive scaling
        result = (self.adaptive_scale * nested_sum + 
                 0.3 * fractal_conditioning + 
                 0.2 * cross_coupling + 
                 0.1 * nonlinear_interaction + 
                 2.0)
        
        return result