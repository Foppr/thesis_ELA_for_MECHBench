import numpy as np

class FractionalBrownianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Generate multiple radial basis function centers
        self.centers = np.random.uniform(-5.0, 5.0, (15, dim))
        # Random weights for each RBF
        self.weights = np.random.uniform(0.5, 2.0, 15)
        # Fractional Brownian motion parameters
        self.hurst = np.random.uniform(0.1, 0.9, dim)
        # Adaptive conditioning factors
        self.conditioning_factors = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial Basis Function component
        rbf_value = 0.0
        for i in range(15):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            rbf_value += weight * np.exp(-distance / (2 * 0.3 ** 2))
        
        # Fractional Brownian motion noise component
        fbm_noise = 0.0
        for i in range(self.dim):
            xi = x[i]
            hurst = self.hurst[i]
            # Simplified fractional Brownian motion approximation
            fbm_noise += np.sin(xi * (i + 1)) * np.cos(xi * (i + 2)) * (1.0 / (1.0 + hurst))
        
        # Adaptive conditioning component
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += self.conditioning_factors[i] * (x[i] ** 2) * np.exp(-x[i] ** 2 / (2 * (i + 1) ** 2))
        
        # Cross-dimensional coupling with sine modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (i + 1) * (j + 1)
        
        # Combine all components with adaptive weights
        result = 0.3 * rbf_value + 0.4 * fbm_noise + 0.2 * conditioning + 0.1 * coupling
        
        return result