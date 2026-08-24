import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        self.rbf_weights = np.random.uniform(0.5, 3.0, 10)
        self.sinusoidal_frequencies = np.random.uniform(2.0, 10.0, dim)
        self.conditioning_factors = np.random.uniform(0.1, 5.0, dim)
        self.cross_dim_coupling = np.random.uniform(-0.3, 0.3, (dim, dim))
        self.noise_amplitude = np.random.uniform(0.1, 0.5, dim)
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial Basis Function components
        for i in range(10):
            diff = x - self.rbf_centers[i]
            rbf_value = np.exp(-np.sum(diff**2) / (2 * self.rbf_widths[i]**2))
            result += self.rbf_weights[i] * rbf_value
        
        # Sinusoidal modulation with dynamic frequencies and cross-dimension coupling
        for i in range(self.dim):
            freq = self.sinusoidal_frequencies[i] * (1.0 + 0.2 * np.sin(0.5 * x[i]))
            result += 5 * np.sin(freq * x[i]) * self.conditioning_factors[i]
            # Add cross-dimension interactions
            for j in range(self.dim):
                if i != j:
                    result += 1.5 * np.sin(0.3 * x[i]) * np.cos(0.4 * x[j]) * self.cross_dim_coupling[i, j]
        
        # Boundary penalty with exponential decay
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_boundary = 5.0 - np.abs(x[i])
            if dist_from_boundary > 0:
                boundary_penalty += 10 * dist_from_boundary**2 * np.exp(-0.1 * dist_from_boundary)
        result += boundary_penalty
        
        # Dynamic conditioning based on x values and dimensionality
        dynamic_factor = 1.0 + 0.5 * np.sin(np.sum(x**2) / 10.0)
        result *= dynamic_factor
        
        # Chaotic noise term with dimensionally varying amplitude
        noise = 0.0
        for i in range(self.dim):
            noise += self.noise_amplitude[i] * np.sin(3 * x[i] + np.sin(2 * x[i])) * np.cos(1.5 * x[i])
        result += noise
        
        # Add a chaotic perturbation term with exponential scaling
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += 2.5 * np.sin(8 * x[i] + np.sin(5 * x[i])) * np.exp(-0.3 * np.abs(x[i]))
        result += chaotic_term
        
        return result