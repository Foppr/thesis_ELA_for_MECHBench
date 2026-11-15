import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.amplitudes = np.random.uniform(1.0, 3.0, dim)
        self.frequencies = np.random.uniform(0.5, 2.0, dim)
        self.decay_rates = np.random.uniform(0.1, 0.5, dim)
        self.cross_coupling = np.random.uniform(-0.5, 0.5, (dim, dim))
        self.global_offset = np.random.uniform(-1.0, 1.0)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic gradient components with exponential decay
        for i in range(self.dim):
            # Harmonic oscillation with exponential decay
            oscillation = self.amplitudes[i] * np.sin(self.frequencies[i] * x[i])
            decay = np.exp(-self.decay_rates[i] * np.abs(x[i]))
            result += oscillation * decay
            
        # Cross-dimensional coupling with chaotic interaction
        for i in range(self.dim):
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_term += self.cross_coupling[i, j] * x[j] * np.sin(x[i] * x[j])
            result += coupling_term
            
        # Add a global chaotic modulation
        chaotic_mod = np.sin(np.sum(x**2) / 10.0) * np.cos(np.sum(x) / 5.0)
        result += chaotic_mod
        
        # Add a quadratic penalty near boundaries
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += 5 * (np.abs(x[i]) - 5.0)**2
        result += boundary_penalty
        
        # Add a dynamic conditioning factor based on dimension
        conditioning = 1.0
        for i in range(self.dim):
            conditioning *= (1.0 + 0.1 * np.sin(x[i]))
        result *= conditioning
        
        # Add a global offset to shift the landscape
        result += self.global_offset
        
        return result