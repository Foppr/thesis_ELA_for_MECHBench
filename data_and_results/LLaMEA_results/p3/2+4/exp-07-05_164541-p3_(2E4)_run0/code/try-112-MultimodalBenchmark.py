import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis function centers and widths for stability
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion with mixed terms
        poly_expansion = np.sum(
            np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * 
            np.sin(4 * np.pi * x) * np.cos(5 * np.pi * x) * 
            np.sin(6 * np.pi * x) * np.cos(7 * np.pi * x)
        )
        
        # Radial basis function component with dynamic widths
        rbf_sum = 0.0
        for i in range(10):
            dist = np.sum((x - self.centers[i]) ** 2)
            rbf_sum += np.exp(-self.widths[i] * dist)
        
        # Dynamic coupling with time-dependent phase shifts
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x[i] - x[i+1])**4 * np.sin(10 * np.pi * (x[i] + x[i+1]))
            coupling += (x[i] + x[i+1])**3 * np.cos(8 * np.pi * (x[i] - x[i+1]))
        
        # Multi-scale oscillatory component with varying frequencies
        oscillatory = np.sum(
            np.sin(15 * x) * np.cos(13 * x) * 
            np.sin(11 * x) * np.cos(9 * x) * 
            np.sin(7 * x) * np.cos(5 * x) * 
            np.sin(3 * x) * np.cos(1 * x)
        )
        
        # Fractional polynomial with non-integer exponents
        fractional = np.sum(
            0.5 * x**2.7 - 1.2 * x**3.1 + 0.8 * x**1.9 - 0.3 * x**2.3 + 
            0.6 * x**1.5 - 0.9 * x**2.1 + 0.4 * x**1.7 - 0.2 * x**1.3
        )
        
        # Combine all components with optimized weights
        return 0.4 * poly_expansion + 0.3 * rbf_sum + 0.2 * coupling + 0.1 * oscillatory + 0.05 * fractional + 2.0