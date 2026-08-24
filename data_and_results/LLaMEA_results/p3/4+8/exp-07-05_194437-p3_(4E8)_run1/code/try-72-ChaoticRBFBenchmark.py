import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_weights = np.random.uniform(0.5, 3.0, 10)
        self.rbf_widths = np.random.uniform(0.2, 1.0, 10)
        self.frequency_modulators = np.random.uniform(2.0, 10.0, dim)
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
        
        # Chaotic sinusoidal modulations with dynamic frequencies
        for i in range(self.dim):
            freq = self.frequency_modulators[i] * (1.0 + 0.5 * np.sin(0.3 * x[i]))
            result += 5 * np.sin(freq * x[i]) * self.conditioning_factors[i]
            
            # Cross-dimension coupling
            for j in range(self.dim):
                if i != j:
                    result += 1.5 * np.sin(0.4 * x[i]) * np.cos(0.6 * x[j]) * self.cross_dim_coupling[i, j]
        
        # Boundary penalty with exponential decay
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_boundary = 5.0 - np.abs(x[i])
            if dist_from_boundary > 0:
                boundary_penalty += 10 * dist_from_boundary**3 * np.exp(-0.1 * dist_from_boundary)
        result += boundary_penalty
        
        # Adaptive conditioning based on position and dimensionality
        norm = np.linalg.norm(x)
        dynamic_factor = 1.0 + 0.7 * np.sin(norm / 2.0) * np.cos(norm / 4.0)
        result *= dynamic_factor
        
        # Structured noise with chaotic periodicity
        noise = 0.0
        for i in range(self.dim):
            noise += self.noise_amplitude[i] * np.sin(1.2 * x[i]) * np.cos(0.8 * x[i]) * np.exp(-0.05 * x[i]**2)
        result += noise
        
        # Chaotic perturbation term
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += 2.5 * np.sin(8 * x[i] + np.sin(5 * x[i])) * np.cos(3 * x[i])
        result += chaotic_term
        
        return result