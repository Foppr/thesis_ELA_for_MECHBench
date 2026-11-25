import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive conditioning parameters
        self.conditioning = np.random.uniform(0.5, 2.0, dim)
        # Initialize frequency parameters for oscillatory components
        self.frequencies = np.random.uniform(1.0, 8.0, dim)
        # Initialize radial basis centers and widths
        self.centers = np.random.uniform(-3.0, 3.0, (5, dim))
        self.widths = np.random.uniform(0.5, 2.0, 5)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component with adaptive frequencies
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += self.conditioning[i] * np.sin(self.frequencies[i] * x_norm[i]) * \
                       np.cos(self.frequencies[i] * x_norm[i])
        
        # Radial basis function component with multiple centers
        rbf_term = 0.0
        for i in range(5):
            distance = np.sum((x_norm - self.centers[i]) ** 2)
            rbf_term += np.exp(-self.widths[i] * distance)
        
        # Cross-dimension interaction term with adaptive coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (i + j) / (self.dim * (self.dim + 1)) * \
                          np.sin(2 * np.pi * x_norm[i] * x_norm[j])
                cross_term += coupling * np.exp(-0.5 * (x_norm[i] - x_norm[j])**2)
        
        # Polynomial conditioning component
        poly_term = np.sum(x_norm**4) + 0.5 * np.sum(x_norm**3)
        
        # Adaptive scaling based on dimension
        scale_factor = 1.0 + 0.1 * np.sin(np.sum(x_norm))
        
        # Combine all terms with dynamic weighting
        combined = scale_factor * (sin_term + rbf_term + cross_term + poly_term)
        
        # Add a small chaotic noise component
        noise = 0.005 * np.sin(np.sum(x_norm) * 10.0) * np.random.uniform(-1, 1)
        
        return combined + noise