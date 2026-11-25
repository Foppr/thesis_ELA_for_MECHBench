import numpy as np

class MultimodalRadialChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive conditioning parameters
        self.conditioning = np.array([1.0 + 0.5 * np.sin(0.3 * np.pi * i) for i in range(dim)])
        self.frequency = np.array([2.0 + 1.5 * np.cos(0.4 * np.pi * i) for i in range(dim)])
        self.amplitude = np.array([1.0 + 0.3 * np.sin(0.5 * np.pi * i) for i in range(dim)])
        # Radial basis function centers and widths
        self.centers = np.random.uniform(-4.0, 4.0, (dim, dim))
        self.widths = np.array([0.5 + 0.3 * np.cos(0.2 * np.pi * i) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component
        sin_component = 0.0
        for i in range(self.dim):
            sin_component += self.amplitude[i] * np.sin(self.frequency[i] * x[i]) * np.exp(-0.1 * x[i]**2)
        sin_component /= self.dim
        
        # Radial basis function component with adaptive widths
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_term = 0.0
            for j in range(self.dim):
                diff = x[j] - self.centers[i, j]
                rbf_term += np.exp(-0.5 * (diff**2) / (self.widths[i]**2))
            rbf_component += rbf_term
        rbf_component /= self.dim
        
        # Chaotic conditioning with adaptive scaling
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += self.conditioning[i] * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.05 * x[i]**2)
        chaotic_component /= self.dim
        
        # Cross-dimensional interaction with multi-scale coupling
        cross_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.5 * (x[i] + x[j])) * np.cos(0.3 * (x[i] - x[j]))
                cross_component += coupling * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        cross_component /= (self.dim * (self.dim - 1) / 2.0)
        
        # Adaptive fitness landscape with multiple local minima
        adaptive_component = 0.0
        for i in range(self.dim):
            adaptive_component += (x[i]**6 - 3.0 * x[i]**4 + 2.0 * x[i]**2) * np.exp(-0.15 * x[i]**2)
        adaptive_component /= self.dim
        
        # Combine all components with dynamic weighting
        total = 0.2 * sin_component + 0.3 * rbf_component + 0.25 * chaotic_component + 0.15 * cross_component + 0.1 * adaptive_component
        
        return total