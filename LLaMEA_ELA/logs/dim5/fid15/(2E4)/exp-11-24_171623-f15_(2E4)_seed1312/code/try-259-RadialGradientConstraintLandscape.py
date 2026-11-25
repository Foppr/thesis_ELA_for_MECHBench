import numpy as np

class RadialGradientConstraintLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (15, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 15)
        # Gradient field parameters for adaptive conditioning
        self.grad_magnitudes = np.random.uniform(1.0, 3.0, dim)
        self.grad_frequencies = np.random.uniform(0.5, 2.0, dim)
        # Constraint penalty weights and exponents
        self.penalty_weights = np.random.uniform(0.5, 2.0, dim)
        self.penalty_exponents = np.random.uniform(2.0, 5.0, dim)
        # Adaptive scaling factors
        self.scale_factors = 1.0 + 0.5 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(15):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            distance = np.sum((x_norm - center)**2)
            rbf_sum += np.exp(-distance / (2 * width**2))
        
        # Adaptive gradient field component
        grad_field = 0.0
        for i in range(self.dim):
            grad_field += self.grad_magnitudes[i] * np.sin(self.grad_frequencies[i] * x_norm[i]) * \
                         np.cos(self.grad_frequencies[i] * x_norm[i])
        
        # Implicit constraint penalties
        penalty_sum = 0.0
        for i in range(self.dim):
            penalty_sum += self.penalty_weights[i] * (np.abs(x_norm[i])**self.penalty_exponents[i])
        
        # Combined landscape with adaptive scaling
        result = 0.3 * rbf_sum + 0.4 * grad_field + 0.3 * penalty_sum
        
        # Adaptive conditioning based on position and scale factors
        condition_factor = 1.0
        for i in range(self.dim):
            pos_factor = 1.0 + 0.5 * np.abs(x_norm[i])
            scale_factor = self.scale_factors[i]
            condition_factor *= (pos_factor * scale_factor)
        
        # Global penalty with cubic and quartic terms
        global_penalty = 0.1 * np.sum(np.abs(x_norm)**3) + 0.05 * np.sum(x_norm**4)
        
        return result * condition_factor + global_penalty