import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.coupling_coeffs = np.random.uniform(0.5, 2.0, dim)
        self.frequency_coeffs = np.random.uniform(1.0, 8.0, dim)
        self.saddle_points = np.random.uniform(-5.0, 5.0, (10, dim))
        self.curvature_shifts = np.random.uniform(-1.0, 1.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        result = 0.0
        
        # Chaotic gradient components with dynamic frequency modulation
        for i in range(self.dim):
            freq = self.frequency_coeffs[i] * (1.0 + 0.3 * np.sin(x_norm[i] * 2.0))
            result += (np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 1.7)) * \
                     self.coupling_coeffs[i]
        
        # Saddle-point landscape with adaptive curvature
        saddle_sum = 0.0
        for i in range(10):
            diff = x_norm - self.saddle_points[i]
            # Adaptive curvature based on distance from saddle point
            curvature = 1.0 + 0.5 * np.tanh(np.sum(diff**2) - 1.0)
            saddle_sum += curvature * np.prod(diff**2)
        
        # Dynamic shift in curvature based on position
        shift_factor = 0.0
        for i in range(self.dim):
            shift_factor += self.curvature_shifts[i] * np.sin(x_norm[i] * 3.0)
        
        # Cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            cross_term += np.sin(x_norm[i] * x_norm[j] * 2.0) * \
                         np.cos(x_norm[i] * x_norm[j] * 1.5) * \
                         (1.0 + 0.2 * np.sin(shift_factor))
        
        # Polynomial and interaction terms
        poly_term = 0.02 * np.sum(x_norm**4)
        interaction_term = 0.03 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**3)
        
        # Add chaotic noise with position-dependent amplitude
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x_norm[i]**3 + x_norm[(i+2) % self.dim]**2) * \
                    np.cos(x_norm[i]**2 + x_norm[(i+2) % self.dim]**3) * \
                    (0.1 + 0.3 * np.abs(x_norm[i]))
        
        # Combine all components
        return result + saddle_sum + cross_term + poly_term + interaction_term + noise