import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.coupling_coeffs = np.random.uniform(0.5, 2.0, dim)
        self.frequency_coeffs = np.random.uniform(1.0, 8.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.saddle_points = np.random.uniform(-5.0, 5.0, (10, dim))
        self.time_variant_factor = 0.0
        
    def f(self, x):
        self.time_variant_factor = 0.5 + 0.5 * np.sin(0.1 * np.sum(x))
        
        # Chaotic gradient component with time variation
        grad_component = 0.0
        for i in range(self.dim):
            xi = x[i] / 5.0
            grad_component += (self.coupling_coeffs[i] * 
                              np.sin(self.frequency_coeffs[i] * xi + self.phase_shifts[i]) *
                              np.cos(self.frequency_coeffs[i] * xi * 1.3 + self.phase_shifts[i])) * \
                              self.time_variant_factor
        
        # Saddle-point landscape with multiple attracting regions
        saddle_term = 0.0
        for i in range(10):
            diff = x - self.saddle_points[i]
            distance = np.sqrt(np.sum(diff**2))
            saddle_term += 1.0 / (1.0 + distance**2) * np.cos(distance * 0.5)
        
        # Periodic time-variant modulation
        periodic_term = 0.0
        for i in range(self.dim):
            xi = x[i] / 5.0
            periodic_term += np.sin(self.frequency_coeffs[i] * xi * self.time_variant_factor) * \
                            np.cos(self.frequency_coeffs[i] * xi * 0.7 * self.time_variant_factor)
        
        # Cross-dimensional interaction with asymmetric coupling
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x[i]**2 + x[i+1]**2) * \
                         np.sin(np.pi * (x[i] + x[i+1]) * self.time_variant_factor) * \
                         np.cos(np.pi * (x[i] - x[i+1]) * self.time_variant_factor)
        
        # Asymmetric polynomial terms to create non-symmetric basins
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (0.1 * x[i]**4 + 0.05 * x[i]**6) * (1.0 + 0.2 * np.sin(3 * x[i]))
        
        # Add a term that creates a dynamic global minimum location
        dynamic_min = np.sin(self.time_variant_factor) * np.cos(self.time_variant_factor)
        dynamic_term = 0.5 * (np.sum(x**2) - 2 * dynamic_min * np.sum(x))
        
        return grad_component + saddle_term + periodic_term + cross_term + poly_term + dynamic_term