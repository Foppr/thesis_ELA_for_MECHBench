import numpy as np

class PolynomialChaosRBF:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for radial basis functions
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Polynomial chaos component with mixed terms
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i]**4) - 6*(x[i]**2) + 9
            if i > 0:
                poly_term += 0.5 * x[i] * x[i-1]
        
        # Radial basis functions with varying widths and centers
        rbf_sum = 0.0
        for i in range(10):
            dist = np.sum((x - self.rbf_centers[i])**2)
            rbf_sum += np.exp(-dist / (2 * self.rbf_widths[i]**2))
        
        # Adaptive gradient field component
        grad_field = 0.0
        for i in range(self.dim):
            grad_field += np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            if i > 0:
                grad_field += 0.2 * (x[i] - x[i-1])**3
        
        # Cross-dimensional coupling with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
        
        # Add a global scaling factor based on input magnitude
        scale_factor = 1.0 + 0.1 * np.sum(np.abs(x))
        
        # Combine all components with adaptive weights
        result = scale_factor * (poly_term + 0.5 * rbf_sum + 0.3 * grad_field + 0.2 * cross_term)
        
        # Add small noise to prevent exact replication
        result += np.random.normal(0, 0.001)
        
        return result