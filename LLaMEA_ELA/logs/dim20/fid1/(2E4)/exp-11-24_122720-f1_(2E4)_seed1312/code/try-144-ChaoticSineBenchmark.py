import numpy as np

class ChaoticSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.chaotic_factor = 4.0
        self.poly_degree = 5
        self.rbf_width = 1.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential component with enhanced nonlinearity and dimensionality scaling
        poly_sum = 0
        for i in range(self.dim):
            poly_sum += (x[i] ** (2 + i % 5)) * (1 + 0.2 * np.sin(i * 2.0))
            
        # Radial basis function component with adaptive centers, weights, and dynamic widths
        rbf_sum = 0
        for i in range(self.dim):
            center = 3.0 * np.sin(i * np.pi / (self.dim + 3))
            distance = np.abs(x[i] - center)
            weight = np.exp(-0.4 * (distance / (self.rbf_width + 0.2 * np.cos(i))) ** 2)
            rbf_sum += weight
            
        # Chaotic sine mapping component with hyperchaotic coupling and dynamic parameter
        chaotic_sum = 0
        for i in range(self.dim):
            # Apply hyperchaotic sine map with dynamic parameter based on dimension and position
            chaotic_param = self.chaotic_factor * (1 + 0.3 * np.cos(i * np.pi / (self.dim + 4)))
            chaotic_val = np.sin(chaotic_param * x[i]) + np.cos(chaotic_param * x[i]**2) + 0.6 * np.sin(2 * chaotic_param * x[i])
            chaotic_sum += chaotic_val ** 2
            
        # Enhanced cross-term interactions with multiple coupling types and interaction strength modulation
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling1 = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                coupling2 = np.exp(-0.6 * (x[i] - x[j])**2) * np.sin(x[i] + x[j])
                coupling3 = np.tanh(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2))
                cross_sum += (coupling1 + 0.4 * coupling2 + 0.3 * coupling3) ** 2
                
        # Multi-scale sinusoidal modulation with frequency variation and phase shifting
        mod_sum = 0
        for i in range(self.dim):
            scale_factor = 1.5 + 0.8 * np.sin(i * np.pi / (self.dim + 5))
            phase_shift = 0.5 * np.cos(i * np.pi / (self.dim + 2))
            mod_val = np.sin(scale_factor * x[i] + phase_shift) * np.cos(2 * scale_factor * x[i] + phase_shift) + 0.4 * np.sin(3 * scale_factor * x[i] + phase_shift)
            mod_sum += mod_val ** 2
            
        # Hyperchaotic coupling term between dimensions (mutated version with different interaction)
        hyperchaos_sum = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                # Mutated hyperchaotic coupling with altered power and interaction
                hyperchaos_val = np.sin(x[i]) * np.cos(x[i+1]) + np.cos(x[i]) * np.sin(x[i+1])
                hyperchaos_sum += hyperchaos_val ** 4  # Changed from cube to fourth power
                
        # Global scaling and dimensionality effect with improved conditioning
        scale = 1.2 + 0.5 * np.log(self.dim + 1)
        
        # Add a small constant to avoid flat regions
        return scale * (poly_sum + rbf_sum + chaotic_sum + cross_sum + mod_sum + hyperchaos_sum) + 0.15 * self.dim