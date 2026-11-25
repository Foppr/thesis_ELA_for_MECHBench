import numpy as np

class AdaptivePolynomialExponentialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial degree coefficients
        self.poly_degrees = 2 + 3 * np.random.rand(dim)
        # Exponential decay rates
        self.exp_rates = 0.1 + 1.5 * np.random.rand(dim)
        # Sine frequency components
        self.sin_freqs = 1.0 + 5.0 * np.random.rand(dim)
        # Cross-dimensional coupling strengths
        self.coupling_strengths = 0.5 + 2.0 * np.random.rand(dim, dim)
        # Adaptive conditioning parameters
        self.conditioning_params = 0.5 + 2.5 * np.random.rand(dim)
        # Local minima positions
        self.minima_positions = -3.0 + 6.0 * np.random.rand(dim, 10)
        
    def f(self, x):
        x_norm = x / 5.0
        result = 0.0
        
        # Polynomial component
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += np.power(np.abs(x_norm[i]), self.poly_degrees[i])
        
        # Exponential barrier component
        exp_sum = 0.0
        for i in range(self.dim):
            exp_sum += np.exp(-self.exp_rates[i] * np.abs(x_norm[i]))
        
        # Sine-based interaction component
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += np.sin(self.sin_freqs[i] * x_norm[i])
        
        # Cross-dimensional coupling
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_strengths[i, j] * np.sin(x_norm[i] - x_norm[j])
        
        # Local minima attraction
        minima_sum = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x_norm[i] - self.minima_positions[i, :]))
            minima_sum += min_dist
        
        # Combine components with adaptive weights
        result = 0.4 * poly_sum + 0.3 * exp_sum + 0.2 * sin_sum + 0.1 * coupling_sum
        
        # Apply adaptive conditioning
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor += self.conditioning_params[i] * np.abs(x_norm[i])**2
        
        # Add penalty for distance from origin
        origin_penalty = 0.1 * np.sum(x_norm**2)
        
        return result * condition_factor + minima_sum + origin_penalty