import numpy as np

class RadialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis function centers and widths
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        x = np.array(x)
        
        # Radial basis function component
        rbf_term = 0.0
        for i in range(10):
            center = self.centers[i]
            width = self.widths[i]
            rbf_term += np.exp(-np.sum((x - center)**2) / (2 * width**2))
        
        # Sinusoidal coupling terms between dimensions
        sin_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sin_coupling += np.sin(x[i] * x[j]) + 0.5 * np.cos(x[i] + x[j])
        
        # Adaptive conditioning based on position
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += (1 + 0.1 * np.abs(x[i])) * x[i]**2
        
        # Add noise component
        noise = np.sum(np.random.normal(0, 0.1, self.dim))
        
        # Combine all terms with different weights
        return 2.0 * rbf_term + 0.5 * sin_coupling + 0.3 * conditioning + noise