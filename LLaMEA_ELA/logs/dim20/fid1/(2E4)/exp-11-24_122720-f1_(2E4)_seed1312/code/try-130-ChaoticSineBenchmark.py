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
        
        # Polynomial potential component with adaptive exponents
        poly_sum = 0
        for i in range(self.dim):
            adaptive_exp = 2 + (i % 4) + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            poly_sum += (x[i] ** adaptive_exp) * (1 + 0.2 * np.cos(i))
            
        # Radial basis function component with dynamic centers and weights
        rbf_sum = 0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * np.pi / (self.dim + 2)) * np.cos(i * np.pi / (self.dim + 3))
            distance = np.abs(x[i] - center)
            weight = np.exp(-0.3 * (distance / self.rbf_width) ** 2) * (1 + 0.1 * np.sin(i))
            rbf_sum += weight
            
        # Chaotic sine mapping component with parameter modulation
        chaotic_sum = 0
        for i in range(self.dim):
            # Apply chaotic sine map with dynamic parameter
            chaotic_param = self.chaotic_factor * np.sin(i * np.pi / (self.dim + 3)) * np.cos(i * np.pi / (self.dim + 4))
            chaotic_val = np.sin(chaotic_param * x[i]) + np.cos(chaotic_param * x[i]**2) + 0.3 * np.sin(2 * chaotic_param * x[i])
            chaotic_sum += chaotic_val ** 2
            
        # Enhanced cross-term interactions with multiple coupling functions
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling1 = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                coupling2 = np.tanh(x[i] - x[j]) * np.exp(-0.5 * (x[i] - x[j])**2)
                cross_sum += coupling1 ** 2 + coupling2 ** 2
                
        # Multi-scale sinusoidal modulation with adaptive frequencies
        mod_sum = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.4 * np.sin(i * np.pi / (self.dim + 2)) * np.cos(i * np.pi / (self.dim + 4))
            mod_val = np.sin(scale_factor * x[i]) * np.cos(2 * scale_factor * x[i]) + 0.2 * np.sin(3 * scale_factor * x[i])
            mod_sum += mod_val ** 2
            
        # Global scaling with dimensionality-aware adjustment
        scale = 1.0 + 0.4 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * np.pi / 4)
        
        # Add noise term to increase robustness
        noise_term = 0.05 * np.sum(np.sin(x) ** 2)
        
        return scale * (poly_sum + rbf_sum + chaotic_sum + cross_sum + mod_sum) + noise_term