import numpy as np

class RadialOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**2) * (1.0 + 0.5 * np.sin(5.0 * r))
        
        # Angular oscillations in all dimensions
        angular_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angular_sum += np.cos(3.0 * (x_norm[i] - x_norm[j])) * np.sin(2.0 * (x_norm[i] + x_norm[j]))
        
        # High-frequency sine modulation
        freq_mod = np.sum(np.sin(17.0 * x_norm) * np.cos(11.0 * x_norm))
        
        # Polynomial shaping term
        poly_term = np.sum(x_norm**4)
        
        # Cross-term interaction
        cross_term = np.sum(x_norm * np.sin(2.0 * r)) if r > 1e-8 else 0.0
        
        # Combine all terms with dynamic weights based on dimensionality
        weight_radial = 0.6 + 0.2 / (1.0 + np.exp(-0.5 * self.dim))
        weight_angular = 0.3 + 0.1 / (1.0 + np.exp(-0.3 * self.dim))
        weight_freq = 0.2 + 0.1 / (1.0 + np.exp(-0.4 * self.dim))
        weight_poly = 0.1 + 0.05 / (1.0 + np.exp(-0.2 * self.dim))
        
        return weight_radial * radial_term + weight_angular * angular_sum + \
               weight_freq * freq_mod + weight_poly * poly_term + 0.05 * cross_term