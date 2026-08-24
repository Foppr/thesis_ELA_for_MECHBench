import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.coupling_coeffs = np.random.uniform(0.5, 2.0, dim)
        self.frequency_coeffs = np.random.uniform(1.0, 8.0, dim)
        self.curvature_params = np.random.uniform(0.1, 1.0, dim)
        self.saddle_points = np.random.uniform(-5.0, 5.0, (10, dim))
        self.adaptation_factor = 1.0 + 0.5 * np.log(dim + 1)
        
    def f(self, x):
        x_scaled = x / 5.0
        result = 0.0
        
        # Chaotic oscillatory component with dimension-adaptive frequency
        for i in range(self.dim):
            freq = self.frequency_coeffs[i] * self.adaptation_factor
            result += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7) * \
                     np.exp(-0.5 * (x_scaled[i] ** 2))
        
        # Saddle point interactions with adaptive weights
        for i in range(10):
            diff = x_scaled - self.saddle_points[i]
            distance = np.sqrt(np.sum(diff**2))
            # Saddle point contribution with varying curvature
            curvature = self.curvature_params[i % self.dim] * self.adaptation_factor
            result += curvature * np.exp(-distance**2) * np.sin(distance * 3.0)
        
        # Coupling terms between dimensions with chaotic modulation
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.coupling_coeffs[i] * self.coupling_coeffs[j]
                coupling_sum += coupling * np.sin(x_scaled[i] * x_scaled[j] * 2.0)
        
        # Add polynomial and gradient-based terms for varied curvature
        poly_term = 0.05 * np.sum(x_scaled**4)
        grad_term = 0.1 * np.sum(np.abs(x_scaled)**3)
        
        # Add a term that penalizes proximity to saddle points to increase difficulty
        penalty = 0.0
        for point in self.saddle_points:
            diff = x_scaled - point
            dist = np.sqrt(np.sum(diff**2))
            penalty += 1.0 / (1.0 + dist**3)
        
        return result + coupling_sum + poly_term + grad_term + penalty