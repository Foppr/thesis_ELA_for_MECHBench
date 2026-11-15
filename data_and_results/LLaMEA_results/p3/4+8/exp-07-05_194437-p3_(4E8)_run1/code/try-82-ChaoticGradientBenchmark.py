import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.amplitudes = np.random.uniform(1.0, 4.0, dim)
        self.frequencies = np.random.uniform(0.5, 3.0, dim)
        self.decay_rates = np.random.uniform(0.05, 0.7, dim)
        self.cross_coupling = np.random.uniform(-1.0, 1.0, (dim, dim))
        self.global_offset = np.random.uniform(-2.0, 2.0)
        self.sinusoidal_modulation = np.random.uniform(0.5, 2.0, dim)
        self.conditioning_factors = np.random.uniform(0.5, 1.5, dim)
        self.multi_scale_factors = np.random.uniform(0.1, 0.5, dim)
        self.boundary_strength = np.random.uniform(8.0, 12.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic gradient components with exponential decay and sinusoidal modulation
        for i in range(self.dim):
            oscillation = self.amplitudes[i] * np.sin(self.frequencies[i] * x[i])
            decay = np.exp(-self.decay_rates[i] * np.abs(x[i]))
            modulation = np.sin(self.sinusoidal_modulation[i] * x[i])
            result += oscillation * decay * modulation
            
        # Enhanced cross-dimensional coupling with chaotic interaction
        for i in range(self.dim):
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_term += self.cross_coupling[i, j] * x[j] * np.sin(x[i] * x[j] * np.cos(x[i] + x[j]))
            result += coupling_term * np.sin(x[i])
            
        # Add a global chaotic modulation with multiple frequencies
        chaotic_mod = np.sin(np.sum(x**2) / 10.0) * np.cos(np.sum(x) / 5.0) * np.sin(np.sum(x) / 3.0)
        result += chaotic_mod
        
        # Add a more sophisticated boundary penalty with dimension-specific strength
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_boundary = 5.0 - np.abs(x[i])
            boundary_penalty += self.boundary_strength[i] * (dist_from_boundary ** 4) * (dist_from_boundary < 0)
        result += boundary_penalty
        
        # Add a dynamic conditioning factor based on dimension with multiplicative effect
        conditioning = 1.0
        for i in range(self.dim):
            conditioning *= (self.conditioning_factors[i] + 0.3 * np.sin(x[i]) * np.cos(x[i]))
        result *= conditioning
        
        # Add a multi-scale sinusoidal perturbation with enhanced complexity
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += self.multi_scale_factors[i] * np.sin(x[i] * 3.0) * np.cos(x[i] * 0.7) * np.sin(x[i] * 1.3)
        result += multi_scale
        
        # Add a periodic penalty term to increase multimodality
        periodic_penalty = 0.0
        for i in range(self.dim):
            periodic_penalty += 2.0 * np.sin(x[i] * 2.0 * np.pi / 5.0) * np.cos(x[i] * 3.0 * np.pi / 5.0)
        result += periodic_penalty
        
        # Add a global offset to shift the landscape
        result += self.global_offset
        
        return result