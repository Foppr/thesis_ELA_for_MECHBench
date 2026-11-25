import numpy as np

class ExponentialRadialHillClimbLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Exponential decay potentials with random exponents and amplitudes
        self.potential_amplitudes = 2.0 + 3.0 * np.random.rand(dim)
        self.potential_exponents = 0.5 + 2.0 * np.random.rand(dim)
        # Radial basis functions with adaptive centers and varying widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, dim))
        self.rbf_widths = 0.5 + 2.0 * np.random.rand(dim)
        # Asymmetric hill-climbing gradients with directional bias
        self.gradient_directions = np.random.randn(dim, dim)
        self.gradient_bias = 1.0 + 2.0 * np.random.rand(dim)
        # Condition number variation across dimensions
        self.condition_numbers = 0.1 + 5.0 * np.random.rand(dim)
        
    def f(self, x):
        x_norm = x / 5.0
        # Exponential decay potential component
        potential_sum = 0.0
        for i in range(self.dim):
            dist = np.abs(x_norm[i])
            potential_sum += self.potential_amplitudes[i] * np.exp(-self.potential_exponents[i] * dist)
        
        # Radial basis function component with adaptive centers
        rbf_sum = 0.0
        for i in range(self.dim):
            rbf_val = 0.0
            for j in range(self.dim):
                dist_sq = np.sum((x_norm - self.rbf_centers[i]) ** 2)
                rbf_val += np.exp(-0.5 * dist_sq / (self.rbf_widths[i] ** 2))
            rbf_sum += rbf_val
        
        # Asymmetric hill-climbing gradient component
        grad_sum = 0.0
        for i in range(self.dim):
            grad_component = 0.0
            for j in range(self.dim):
                grad_component += self.gradient_directions[i, j] * (x_norm[j] ** 3) * self.gradient_bias[i]
            grad_sum += grad_component
        
        # Combined landscape with condition number scaling
        result = potential_sum + 0.5 * rbf_sum + 0.3 * grad_sum
        
        # Apply dimension-wise conditioning
        conditioned_result = 0.0
        for i in range(self.dim):
            conditioned_result += result * (1.0 + self.condition_numbers[i] * x_norm[i]**2)
        
        # Add global penalty term
        penalty = 0.1 * np.sum(np.abs(x_norm)**4)
        
        return conditioned_result + penalty