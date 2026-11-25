import numpy as np

class ChaoticRadialSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = 0.5 + 2.0 * np.random.rand(dim)
        # Precompute chaotic logistic map parameters
        self.logistic_r = 3.95 + 0.1 * np.random.rand(dim)
        # Precompute saddle-point coupling weights
        self.saddle_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Precompute gradient-based interaction terms
        self.gradient_coeffs = np.random.uniform(-0.2, 0.2, (dim, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with varying widths and centers
        rbf_sum = 0.0
        for i in range(self.dim):
            rbf_val = 0.0
            for j in range(self.dim):
                diff = x_norm[i] - self.rbf_centers[i, j]
                rbf_val += np.exp(-0.5 * (diff / self.rbf_widths[j])**2)
            rbf_sum += rbf_val
        
        # Chaotic logistic map component with dynamic parameters
        logistic_sum = 0.0
        for i in range(self.dim):
            x_log = x_norm[i]
            for _ in range(5):  # Iterate chaotic map 5 times
                x_log = self.logistic_r[i] * x_log * (1 - x_log)
            logistic_sum += x_log**2
        
        # Saddle-point coupling component with gradient-based weights
        saddle_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    diff = x_norm[i] - x_norm[j]
                    saddle_val = self.saddle_weights[i, j] * diff**2 * np.exp(-0.1 * diff**2)
                    saddle_sum += saddle_val
        
        # Gradient-based interaction component
        gradient_sum = 0.0
        for i in range(self.dim):
            grad_term = 0.0
            for j in range(self.dim):
                if i != j:
                    grad_term += self.gradient_coeffs[i, j] * (x_norm[i] - x_norm[j])
            gradient_sum += grad_term**2
        
        # Combined landscape with dynamic weighting
        result = 0.4 * rbf_sum + 0.3 * logistic_sum + 0.2 * saddle_sum + 0.1 * gradient_sum
        
        # Dynamic conditioning based on input magnitude and chaotic characteristics
        condition_factor = 1.0
        for i in range(self.dim):
            logistic_val = self.logistic_r[i] * x_norm[i] * (1 - x_norm[i])
            chaos_factor = 1.0 + 0.3 * np.abs(logistic_val)
            mag_factor = 1.0 + 0.2 * np.abs(x_norm[i])
            condition_factor *= (chaos_factor + 0.2 * mag_factor)
        
        # Final transformation with global scaling and penalty for large values
        penalty = 0.15 * np.sum(np.abs(x_norm)**3)
        return result * condition_factor + penalty + 0.02 * np.sum(x_norm**4)