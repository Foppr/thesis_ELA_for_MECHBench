import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for radial basis functions
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Polynomial chaos expansion component
        poly_term = np.sum(x**4) - 0.5 * np.sum(x**2)
        
        # Radial basis function component with multiple centers
        rbf_sum = 0.0
        for i in range(10):
            dist = np.sum((x - self.centers[i])**2)
            rbf_sum += np.exp(-self.widths[i] * dist)
        
        # Periodic gradient field component
        periodic_term = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x))
        
        # Coupling between dimensions with chaotic modulation
        coupling_term = 0.0
        for i in range(self.dim - 1):
            coupling_term += np.sin(5 * np.pi * x[i]) * np.cos(7 * np.pi * x[i+1]) * np.exp(-0.1 * (x[i]**2 + x[i+1]**2))
        
        # Add a fractional dimension coupling term
        frac_coupling = 0.3 * np.sum(np.abs(x[:-1] - x[1:])**(1.3))
        
        # Combine all terms with different weights
        return poly_term + 0.5 * rbf_sum + 0.3 * periodic_term + 0.2 * coupling_term + frac_coupling