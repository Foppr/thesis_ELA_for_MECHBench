import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis centers and widths for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function components with adaptive scaling
        rbf_sum = 0.0
        for i in range(10):
            diff = x - self.centers[i]
            rbf_sum += np.exp(-0.5 * np.sum((diff / self.widths[i])**2))
        
        # Cross-dimensional coupling with polynomial interaction
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x[i] * x[i+1])**3 + np.sin(x[i] + x[i+1])**2
        
        # Add periodic modulation with varying frequencies
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(2 * np.pi * x[i] * (i + 1)) * np.cos(3 * np.pi * x[i] * (i + 1))
        
        # Add a global quadratic term for conditioning
        quadratic = 0.1 * np.sum(x**2)
        
        # Combine all terms with different weights
        return 0.7 * rbf_sum + 0.2 * coupling + 0.1 * periodic + quadratic + 5.0