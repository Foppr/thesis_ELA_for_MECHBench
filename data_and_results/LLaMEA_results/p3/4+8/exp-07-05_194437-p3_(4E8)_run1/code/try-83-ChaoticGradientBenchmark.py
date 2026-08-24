import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.amplitudes = np.random.uniform(1.0, 5.0, dim)
        self.frequencies = np.random.uniform(0.5, 4.0, dim)
        self.decay_rates = np.random.uniform(0.05, 1.0, dim)
        self.cross_coupling = np.random.uniform(-1.5, 1.5, (dim, dim))
        self.global_offset = np.random.uniform(-3.0, 3.0)
        self.sinusoidal_modulation = np.random.uniform(0.5, 3.0, dim)
        self.conditioning_factors = np.random.uniform(0.3, 2.0, dim)
        self.saddle_points = np.random.uniform(-2.0, 2.0, dim)
        self.nonlinearity_strength = np.random.uniform(0.5, 2.5, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic gradient components with exponential decay and sinusoidal modulation
        for i in range(self.dim):
            oscillation = self.amplitudes[i] * np.sin(self.frequencies[i] * x[i])
            decay = np.exp(-self.decay_rates[i] * np.abs(x[i]))
            modulation = np.sin(self.sinusoidal_modulation[i] * x[i])
            result += oscillation * decay * modulation
            
        # Enhanced cross-dimensional coupling with chaotic interaction and saddle point influence
        for i in range(self.dim):
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_term += self.cross_coupling[i, j] * x[j] * np.sin(x[i] * x[j] * np.cos(x[i] + x[j]))
            # Add saddle point influence
            saddle_influence = np.sin(self.saddle_points[i] * x[i])
            result += coupling_term * saddle_influence
            
        # Add a global chaotic modulation with multiple frequencies and nonlinear interaction
        chaotic_mod = np.sin(np.sum(x**2) / 10.0) * np.cos(np.sum(x) / 5.0) * np.sin(np.sum(x) / 3.0)
        # Add nonlinear enhancement
        nonlinear_enhancement = np.prod(np.sin(x / 2.0) + 1.0)
        result += chaotic_mod * nonlinear_enhancement
        
        # Add a quadratic penalty near boundaries with enhanced penalty strength and nonlinearity
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += 15 * (np.abs(x[i]) - 5.0)**2 * (1.0 + 0.1 * np.sin(x[i]))
        result += boundary_penalty
        
        # Add a dynamic conditioning factor based on dimension with multiplicative effect and nonlinearities
        conditioning = 1.0
        for i in range(self.dim):
            conditioning *= (self.conditioning_factors[i] + 0.3 * np.sin(x[i]) * np.cos(x[i]))
        result *= conditioning
        
        # Add a multi-scale sinusoidal perturbation with chaotic interaction
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += np.sin(x[i] * 2.0) * np.cos(x[i] * 0.5) * np.sin(x[i] * 0.3)
        result += multi_scale * 0.7
        
        # Add a novel chaotic interaction term that introduces saddle points and complex curvature
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_interaction += np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * np.tan(x[i] - x[j])
        result += chaotic_interaction * 0.5
        
        # Add a nonlinearity-based penalty term
        nonlin_penalty = 0.0
        for i in range(self.dim):
            nonlin_penalty += self.nonlinearity_strength[i] * np.sin(x[i]**3) * np.cos(x[i]**2)
        result += nonlin_penalty
        
        # Add a global offset to shift the landscape
        result += self.global_offset
        
        return result