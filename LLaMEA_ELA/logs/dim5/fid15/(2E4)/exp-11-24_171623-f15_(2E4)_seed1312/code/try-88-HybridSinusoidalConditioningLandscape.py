import numpy as np

class HybridSinusoidalConditioningLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute modulation frequencies and conditioning parameters
        self.frequencies = np.array([2**(i/3) for i in range(dim)])
        self.conditioning_params = np.array([1.0 + 0.5 * np.sin(i) for i in range(dim)])
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal modulation component with varying frequencies
        sin_modulation = 0.0
        for i in range(self.dim):
            sin_modulation += np.sin(self.frequencies[i] * x_norm[i]) * \
                             np.cos(self.frequencies[i] * x_norm[i]**2) * \
                             (1 + 0.3 * np.sin(i))
        
        # Polynomial conditioning with asymmetric exponents
        poly_conditioning = 0.0
        for i in range(self.dim):
            exp_factor = 2.0 + 0.5 * np.cos(i)
            poly_conditioning += self.conditioning_params[i] * (x_norm[i]**exp_factor)
        
        # Gradient-based attraction fields with multiple local minima
        attraction_fields = 0.0
        for i in range(self.dim):
            # Create attractive points at specific locations
            attractor_pos = np.sin(i * np.pi / self.dim) * 0.5 + 0.1 * np.cos(i)
            dist_from_attractor = abs(x_norm[i] - attractor_pos)
            attraction_fields += np.exp(-dist_from_attractor**2 * 2.0) * \
                                (1 + 0.4 * np.sin(i) * np.cos(i))
        
        # Cross-dimensional coupling with exponential interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                cross_coupling += np.exp(-abs(x_norm[i] - x_norm[j])**2) * \
                                 (x_norm[i]**3 + x_norm[j]**3) * \
                                 (i + j) / (self.dim + 1)
        
        # Multi-scale oscillatory component for increased complexity
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += np.sin(5 * x_norm[i]) * np.cos(7 * x_norm[i]) * \
                          np.exp(-x_norm[i]**2) * (1 + 0.2 * np.sin(i))
        
        # Combine all components with carefully tuned weights
        result = 0.25 * sin_modulation + 0.35 * poly_conditioning + \
                 0.20 * attraction_fields + 0.15 * cross_coupling + \
                 0.05 * oscillatory
        
        # Add a global scaling factor to control overall difficulty
        return result * (1.0 + 0.1 * np.sum(np.abs(x_norm)))