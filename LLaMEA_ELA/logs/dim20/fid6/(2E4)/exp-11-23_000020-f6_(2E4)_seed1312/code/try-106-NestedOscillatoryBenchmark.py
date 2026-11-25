import numpy as np

class NestedOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate chaotic parameters for tent map
        self.tent_r = np.random.rand(dim) * 2.0 + 2.5
        # Quantum harmonic oscillator parameters
        self.oscillator_freq = np.random.rand(dim) * 8.0 + 2.0
        self.oscillator_ampl = np.random.rand(dim) * 3.0 + 1.0
        # Dynamic conditioning factors
        self.conditioning_factors = np.random.rand(dim) * 6.0 + 2.0
        # Cross-dimensional coupling with dynamic weights
        self.cross_dim_coupling = np.random.randn(dim, dim) * 0.5
        # Chaotic scaling parameters
        self.chaotic_scale = np.random.rand() * 3.0 + 1.0
        # Nesting depth for chaotic iterations
        self.nesting_depth = np.random.randint(3, 8)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic tent map component with nested iterations
        chaotic_sum = 0.0
        for i in range(self.dim):
            tent_value = x_norm[i]
            chaotic_term = 0.0
            for depth in range(1, self.nesting_depth + 1):
                tent_value = self.tent_r[i] * tent_value * (1 - tent_value)
                if depth > 1:
                    chaotic_term += tent_value * (1.0 / depth**1.2)
            chaotic_sum += chaotic_term
        
        # Quantum harmonic oscillator component
        quantum_sum = 0.0
        for i in range(self.dim):
            freq = self.oscillator_freq[i]
            ampl = self.oscillator_ampl[i]
            quantum_sum += ampl * (np.sin(freq * x_norm[i]) + np.cos(freq * x_norm[i]))
        
        # Dynamic conditioning component
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += self.conditioning_factors[i] * x_norm[i]**3
        
        # Cross-dimensional coupling with dynamic weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    weight = np.sin(0.5 * (i + j)) * self.cross_dim_coupling[i, j]
                    cross_coupling += weight * x_norm[i] * x_norm[j]
        
        # Additional nonlinear interaction terms with chaotic mixing
        nonlinear_interaction = 0.0
        for i in range(self.dim):
            nonlinear_interaction += (x_norm[i]**4 + 0.3 * x_norm[i]**5 + 
                                   np.sin(3 * x_norm[i]) * np.cos(x_norm[(i+1) % self.dim]) * 
                                   chaotic_sum[i % 3] if len(chaotic_sum) > 0 else 1.0)
        
        # Combine all components with chaotic scaling
        result = (self.chaotic_scale * chaotic_sum + 
                 0.2 * quantum_sum + 
                 0.4 * conditioning + 
                 0.3 * cross_coupling + 
                 0.1 * nonlinear_interaction + 
                 3.0)
        
        return result