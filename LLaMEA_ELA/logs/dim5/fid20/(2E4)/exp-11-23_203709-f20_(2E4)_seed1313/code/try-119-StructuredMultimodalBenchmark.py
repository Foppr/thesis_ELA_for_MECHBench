import numpy as np

class StructuredMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis centers and widths
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        # Precompute attraction field parameters
        self.attraction_centers = np.random.uniform(-5.0, 5.0, (5, dim))
        self.attraction_strengths = np.random.uniform(1.0, 3.0, 5)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component
        sin_component = 0.0
        for i in range(self.dim):
            sin_component += np.sin(2.0 * np.pi * x[i] / 10.0) * (i + 1)
        
        # Radial basis function component
        rbf_component = 0.0
        for i in range(10):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            distance = np.sum((x - center) ** 2)
            rbf_component += np.exp(-distance / (2 * width ** 2))
        
        # Gradient-based attraction field
        attr_component = 0.0
        for i in range(5):
            center = self.attraction_centers[i]
            strength = self.attraction_strengths[i]
            distance = np.sum((x - center) ** 2)
            attr_component += strength / (distance + 1e-8)
        
        # Cross-dimensional interaction terms
        cross_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_component += np.sin(x[i] * x[j]) * (i + j + 1)
        
        # Combined function with dynamic weights
        total = 0.7 * sin_component + 1.5 * rbf_component - 0.8 * attr_component + 0.4 * cross_component
        
        return total