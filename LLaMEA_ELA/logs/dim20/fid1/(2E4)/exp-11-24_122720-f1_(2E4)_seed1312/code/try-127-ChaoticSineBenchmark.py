import numpy as np

class ChaoticSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.chaotic_factor = 3.8
        self.poly_degree = 4
        self.rbf_width = 1.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential component
        poly_sum = 0
        for i in range(self.dim):
            poly_sum += (x[i] ** (2 + i % 3)) * (1 + 0.1 * np.sin(i))
            
        # Radial basis function component with chaotic modulation
        rbf_sum = 0
        for i in range(self.dim):
            center = 3.0 * np.sin(i * np.pi / (self.dim + 1))
            distance = np.abs(x[i] - center)
            weight = np.exp(-0.5 * (distance / self.rbf_width) ** 2)
            rbf_sum += weight
            
        # Chaotic sine mapping component
        chaotic_sum = 0
        for i in range(self.dim):
            # Apply chaotic sine map with varying parameter
            chaotic_param = self.chaotic_factor * np.sin(i * np.pi / (self.dim + 2))
            chaotic_val = np.sin(chaotic_param * x[i]) + np.cos(chaotic_param * x[i]**2)
            chaotic_sum += chaotic_val ** 2
            
        # Cross-term interactions with sinusoidal coupling
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                cross_sum += coupling ** 2
                
        # Multi-scale sinusoidal modulation
        mod_sum = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 3))
            mod_val = np.sin(scale_factor * x[i]) * np.cos(2 * scale_factor * x[i])
            mod_sum += mod_val ** 2
            
        # Global scaling and dimensionality effect
        scale = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return scale * (poly_sum + rbf_sum + chaotic_sum + cross_sum + mod_sum)