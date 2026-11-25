import numpy as np

class HybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with mixed degrees
        poly_term = np.sum(x**4 + 0.5 * x**3 + 0.1 * x**2)
        
        # Logarithmic barrier near boundaries to penalize out-of-range values
        log_term = np.sum(np.log(26.0 - x**2))
        
        # Spherical component with adaptive radius based on dimension
        sphere_radius = 1.0 + 0.1 * self.dim
        sphere_term = np.sum((x / sphere_radius)**2)
        
        # Cross-term interactions with sinusoidal modulation
        cross_term = np.sum(np.sin(x) * np.cos(0.5 * x) * np.exp(-0.01 * np.sum(x**2)))
        
        # Combine all terms with dimension-dependent weights
        return 0.3 * poly_term + 0.4 * log_term + 0.2 * sphere_term + 0.1 * cross_term