import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.oscillation_freq = 2.0 * np.pi
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        self.poly_degree = 4
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component
        sin_component = np.sum(np.sin(self.oscillation_freq * x) * np.cos(self.oscillation_freq * x / 2.0))
        
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(len(self.rbf_centers)):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            rbf_sum += np.exp(-np.sum((x - center)**2) / (2 * width**2))
        
        # Polynomial conditioning term
        poly_term = np.sum(x**(self.poly_degree + 1)) / self.poly_degree
        
        # Cross-dimensional interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] - x[j])**2 * np.sin(x[i] + x[j])
        
        # Combine all components with varying weights
        result = 0.8 * sin_component + 0.6 * rbf_sum + 0.4 * poly_term + 0.3 * cross_term
        
        # Add noise and scaling
        return result + np.random.normal(0, 0.01) + 5.0 * self.dim