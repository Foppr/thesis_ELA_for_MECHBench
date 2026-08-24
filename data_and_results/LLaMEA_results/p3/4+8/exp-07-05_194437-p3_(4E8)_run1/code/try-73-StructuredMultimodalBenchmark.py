import numpy as np

class StructuredMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.rbf_weights = np.random.uniform(0.5, 3.0, 20)
        self.conditioning_factors = np.random.uniform(0.1, 4.0, dim)
        self.frequency_modulators = np.random.uniform(1.5, 10.0, dim)
        self.cross_dim_coupling = np.random.uniform(-0.7, 0.7, (dim, dim))
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Enhanced Radial Basis Function components with varying scales
        for i in range(20):
            diff = x - self.rbf_centers[i]
            rbf_value = np.exp(-np.sum(diff**2) / (2 * (0.2 + 0.1 * i)**2))
            result += self.rbf_weights[i] * rbf_value
        
        # Chaotic sinusoidal modulation with frequency modulation and cross-dimension coupling
        for i in range(self.dim):
            freq = self.frequency_modulators[i] * (1.0 + 0.4 * np.sin(0.8 * x[i]))
            result += 10 * np.sin(freq * x[i]) * self.conditioning_factors[i]
            # Add cross-dimension interactions
            for j in range(self.dim):
                if i != j:
                    result += 3 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[j]) * self.cross_dim_coupling[i, j]
        
        # Enhanced boundary penalty with exponential decay
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_boundary = 5.0 - np.abs(x[i])
            boundary_penalty += 20 * dist_from_boundary**2 * np.exp(-0.3 * dist_from_boundary**2)
        result += boundary_penalty
        
        # Dynamic conditioning based on norm and dimensionality
        norm = np.linalg.norm(x)
        dynamic_factor = 1.0 + 1.0 * np.sin(norm / 4.0) * np.cos(norm / 6.0)
        result *= dynamic_factor
        
        # Structured noise with chaotic periodicity and dimensionally dependent scaling
        noise = 0.0
        for i in range(self.dim):
            noise += 5 * np.sin(0.9 * x[i]) * np.cos(0.5 * x[i]) * np.exp(-0.15 * x[i]**2) * (1.0 + 0.3 * np.sin(1.7 * x[i]))
        result += noise
        
        # Add a chaotic perturbation term
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += 4 * np.sin(12 * x[i] + np.sin(8 * x[i])) * np.cos(6 * x[i])
        result += chaotic_term
        
        return result