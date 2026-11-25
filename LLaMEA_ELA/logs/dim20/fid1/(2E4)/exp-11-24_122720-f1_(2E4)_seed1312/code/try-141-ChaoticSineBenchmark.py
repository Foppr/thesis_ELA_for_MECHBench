import numpy as np

class ChaoticSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.chaotic_factor = 3.9
        self.poly_degree = 4
        self.rbf_width = 1.2
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential component with enhanced nonlinearity
        poly_sum = 0
        for i in range(self.dim):
            poly_sum += (x[i] ** (2 + i % 4)) * (1 + 0.15 * np.sin(i * 1.5))
            
        # Radial basis function component with adaptive centers and weights
        rbf_sum = 0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * np.pi / (self.dim + 2))
            distance = np.abs(x[i] - center)
            weight = np.exp(-0.3 * (distance / self.rbf_width) ** 2)
            rbf_sum += weight
            
        # Chaotic sine mapping component with dynamic parameter
        chaotic_sum = 0
        for i in range(self.dim):
            # Apply chaotic sine map with dynamic parameter based on dimension
            chaotic_param = self.chaotic_factor * (1 + 0.2 * np.cos(i * np.pi / (self.dim + 3)))
            chaotic_val = np.sin(chaotic_param * x[i]) + np.cos(chaotic_param * x[i]**2) + 0.5 * np.sin(2 * chaotic_param * x[i])
            chaotic_sum += chaotic_val ** 2
            
        # Enhanced cross-term interactions with multiple coupling types
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling1 = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                coupling2 = np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(x[i] + x[j])
                cross_sum += (coupling1 + 0.3 * coupling2) ** 2
                
        # Multi-scale sinusoidal modulation with frequency variation
        mod_sum = 0
        for i in range(self.dim):
            scale_factor = 1.2 + 0.6 * np.sin(i * np.pi / (self.dim + 4))
            mod_val = np.sin(scale_factor * x[i]) * np.cos(2 * scale_factor * x[i]) + 0.3 * np.sin(3 * scale_factor * x[i])
            mod_sum += mod_val ** 2
            
        # Global scaling and dimensionality effect with improved conditioning
        scale = 1.0 + 0.4 * np.log(self.dim + 1)
        
        # Add a small constant to avoid flat regions
        return scale * (poly_sum + rbf_sum + chaotic_sum + cross_sum + mod_sum) + 0.1 * self.dim