import numpy as np

class RuggedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Adaptive conditioning parameters
        self.conditioning = np.array([1.0 + 0.5 * np.sin(0.3 * np.pi * i) for i in range(dim)])
        # Sinusoidal frequency modulations
        self.frequencies = np.array([2.0 + 1.5 * np.cos(0.4 * np.pi * i) for i in range(dim)])
        # Radial basis function centers and widths
        self.centers = np.random.uniform(-3.0, 3.0, (5, dim))
        self.widths = np.random.uniform(0.5, 2.0, 5)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Adaptive conditioned quadratic term
        quadratic_term = np.sum(self.conditioning * x**2)
        
        # Sinusoidal oscillation component
        sinusoidal_term = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i]
            sinusoidal_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
        sinusoidal_term /= self.dim
        
        # Radial basis function combination
        rbf_term = 0.0
        for i in range(5):
            diff = x - self.centers[i]
            rbf_term += self.widths[i] * np.exp(-0.5 * np.sum((diff**2) / (self.widths[i]**2)))
        
        # Cross-dimensional interaction term with adaptive coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.2 * np.sin(0.5 * (x[i] + x[j]))
                cross_term += coupling * np.sin(0.7 * x[i]) * np.cos(0.7 * x[j])
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-scale oscillation with dynamic amplitude
        multi_scale = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(0.8 * np.pi * i + np.sum(x))
            multi_scale += amp * np.sin(2.5 * x[i]) * np.cos(1.2 * x[i])
        multi_scale /= self.dim
        
        # Combined objective with dynamic weighting
        total = 0.3 * quadratic_term + 0.2 * sinusoidal_term + 0.2 * rbf_term + \
                0.2 * cross_term + 0.1 * multi_scale
        
        return total