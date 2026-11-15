import numpy as np

class ChaoticAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis function centers and widths
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        # Trigonometric coupling weights
        self.coupling_weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 10.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay radial basis function component
        rbf_sum = 0.0
        for i in range(10):
            center = self.centers[i]
            width = self.widths[i]
            distance = np.sum((x - center) ** 2)
            rbf_sum += np.exp(-distance / (2 * width ** 2))
        
        # Trigonometric coupling component with adaptive conditioning
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    trig_coupling += self.coupling_weights[i, j] * np.sin(x[i]) * np.cos(x[j]) * self.conditioning_factors[i]
        
        # Adaptive conditioning term with exponential modulation
        adaptive_conditioning = 0.0
        for i in range(self.dim):
            adaptive_conditioning += self.conditioning_factors[i] * np.exp(-0.5 * x[i] ** 2) * np.sin(3 * x[i])
        
        # Dynamic chaotic component with time-like parameter
        chaotic_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_component += np.sin(xi) * np.cos(2 * xi) * np.sin(3 * xi) * np.exp(-0.1 * np.abs(xi))
        
        # Cross-dimensional interaction with polynomial coupling
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i] ** 2) * (x[j] ** 3) * np.sin(0.5 * (x[i] + x[j]))
        
        # Combine all components with varying weights
        result = 0.4 * rbf_sum + 0.3 * trig_coupling + 0.15 * adaptive_conditioning + 0.1 * chaotic_component + 0.05 * poly_interaction
        
        return result