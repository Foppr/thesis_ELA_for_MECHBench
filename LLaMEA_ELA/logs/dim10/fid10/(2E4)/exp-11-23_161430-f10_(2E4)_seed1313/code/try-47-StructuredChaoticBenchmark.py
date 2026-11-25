import numpy as np

class StructuredChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute parameters for radial basis functions
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (10, dim))
        self.rbf_weights = np.random.exponential(1.0, 10)
        # Trigonometric coupling parameters
        self.coupling_freqs = np.linspace(0.5, 3.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with exponential decay
        rbf_term = 0.0
        for i in range(10):
            diff = x - self.rbf_centers[i]
            rbf_term += self.rbf_weights[i] * np.exp(-0.5 * np.sum(diff**2))
        
        # Trigonometric coupling between dimensions
        trig_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            trig_term += np.sin(self.coupling_freqs[i] * x[i]) * np.cos(self.coupling_freqs[j] * x[j])
        
        # Adaptive conditioning based on distance from origin
        dist_from_origin = np.sqrt(np.sum(x**2))
        condition_factor = 1.0 + 0.3 * np.exp(-0.2 * dist_from_origin)
        
        # Cross-dimensional interaction with polynomial coupling
        poly_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            poly_coupling += (x[i]**2 + x[j]**2) * np.sin(0.5 * x[i] * x[j])
        
        # Combine all terms with different weights
        result = 0.4 * rbf_term + 0.3 * trig_term + 0.2 * poly_coupling + 0.1 * condition_factor
        
        return result