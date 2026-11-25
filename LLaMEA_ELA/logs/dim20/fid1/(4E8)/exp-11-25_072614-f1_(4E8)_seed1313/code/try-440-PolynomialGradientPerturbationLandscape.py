import numpy as np

class PolynomialGradientPerturbationLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial exponents and coefficients
        self.exponents = 2 + np.random.randint(1, 4, size=dim)
        self.coefficients = 0.5 + 2.0 * np.random.rand(dim)
        # Gradient field parameters
        self.attraction_strength = 0.3 + 1.2 * np.random.rand()
        self.field_decay = 0.1 + 0.9 * np.random.rand()
        # Stochastic perturbation parameters
        self.perturbation_magnitude = 0.1 + 0.4 * np.random.rand()
        self.perturbation_frequency = 0.5 + 2.0 * np.random.rand()
        # Dynamic valley parameters
        self.valley_count = 3 + np.random.randint(0, 3)
        self.valley_widths = 0.5 + 1.5 * np.random.rand(self.valley_count)
        self.valley_positions = -5.0 + 10.0 * np.random.rand(self.valley_count, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential component
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += self.coefficients[i] * (x[i] ** self.exponents[i])
        
        # Gradient attraction field component
        grad_term = 0.0
        for i in range(self.dim):
            dist_to_center = np.abs(x[i] - 0.0)
            grad_term += self.attraction_strength * np.exp(-self.field_decay * dist_to_center)
        
        # Dynamic valley component with multiple minima
        valley_term = 0.0
        for v in range(self.valley_count):
            valley_dist = 0.0
            for i in range(self.dim):
                diff = x[i] - self.valley_positions[v, i]
                valley_dist += (diff ** 2) / (self.valley_widths[v] ** 2)
            valley_term += np.exp(-valley_dist)
        
        # Stochastic perturbation component
        perturbation_term = 0.0
        for i in range(self.dim):
            perturbation_term += self.perturbation_magnitude * np.sin(
                self.perturbation_frequency * x[i] + 
                np.random.rand() * np.pi
            )
        
        # Combine all components with appropriate weights
        result = (poly_term + 
                 grad_term + 
                 valley_term + 
                 perturbation_term)
        
        return result