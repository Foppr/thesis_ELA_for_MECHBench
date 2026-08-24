import numpy as np

class StructuredMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.rbf_weights = np.random.uniform(0.3, 2.5, 15)
        self.conditioning_factors = np.random.uniform(0.05, 3.0, dim)
        self.frequency_modulators = np.random.uniform(1.0, 8.0, dim)
        self.cross_dimension_coupling = np.random.uniform(-0.5, 0.5, (dim, dim))
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Enhanced Radial Basis Function components with stronger interactions
        for i in range(15):
            diff = x - self.rbf_centers[i]
            rbf_value = np.exp(-np.sum(diff**2) / (2 * 0.3**2))
            result += self.rbf_weights[i] * rbf_value
        
        # Enhanced sinusoidal modulation with chaotic frequency interactions
        for i in range(self.dim):
            freq = self.frequency_modulators[i] * (1.0 + 0.3 * np.sin(3.0 * x[i]))
            result += 8 * np.sin(freq * x[i] / 5.0) * self.conditioning_factors[i]
        
        # Cross-dimension coupling with chaotic interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                coupling_term += self.cross_dimension_coupling[i, j] * x[i] * x[j]
        result += 2.0 * coupling_term
        
        # Complex boundary penalty with exponential decay
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_boundary = np.abs(x[i]) - 5.0
            boundary_penalty += 15 * dist_from_boundary**2 * np.exp(-0.2 * dist_from_boundary**2)
        result += boundary_penalty
        
        # Dynamic conditioning based on global position
        norm = np.linalg.norm(x)
        dynamic_factor = 1.0 + 0.8 * np.sin(norm / 3.0) * np.cos(norm / 7.0)
        result *= dynamic_factor
        
        # Structured noise with chaotic periodicity and cross-dimension interactions
        noise = 0.0
        for i in range(self.dim):
            noise += 5 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[i]) * np.exp(-0.1 * x[i]**2)
            for j in range(self.dim):
                if i != j:
                    noise += 1.5 * np.sin(0.3 * x[i] + 0.2 * x[j]) * np.cos(0.1 * x[i] - 0.3 * x[j])
        result += noise
        
        # Add a chaotic perturbation component
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            chaotic_perturbation += 3 * np.sin(10 * np.pi * x[i] + np.sin(5 * x[i]))
        result += chaotic_perturbation
        
        return result