import numpy as np

class StructuredMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_weights = np.random.uniform(0.5, 2.0, 10)
        self.conditioning_factors = np.random.uniform(0.1, 2.0, dim)
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial Basis Function components
        for i in range(10):
            diff = x - self.rbf_centers[i]
            rbf_value = np.exp(-np.sum(diff**2) / (2 * 0.5**2))
            result += self.rbf_weights[i] * rbf_value
        
        # Sinusoidal modulation with adaptive conditioning
        for i in range(self.dim):
            result += 5 * np.sin(2 * np.pi * x[i] / 5.0) * self.conditioning_factors[i]
        
        # Add a quadratic penalty near boundaries
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += 10 * (np.abs(x[i]) - 5.0)**2 * np.exp(-0.1 * (np.abs(x[i]) - 5.0)**2)
        result += boundary_penalty
        
        # Add a global scaling factor based on the norm
        norm = np.linalg.norm(x)
        result *= (1.0 + 0.5 * np.sin(norm / 2.0))
        
        # Add a structured noise component with periodicity
        noise = 0.0
        for i in range(self.dim):
            noise += 3 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i]) * np.exp(-0.05 * x[i]**2)
        result += noise
        
        return result