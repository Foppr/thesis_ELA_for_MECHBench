import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 5.0
        self.sin_freq = 6.0
        self.radial_weight = 1.2
        self.chaotic_factor = 7.0
        self.interaction_strength = 3.0
        self.barrier_positions = np.random.uniform(-4.8, 4.8, dim)
        self.barrier_widths = np.random.uniform(0.2, 1.0, dim)
        self.rotation_angles = np.random.uniform(-np.pi, np.pi, (dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with chaotic conditioning
        poly_term = 0.0
        for i in range(self.dim):
            chaotic_factor = self.chaotic_factor * (1.0 + 0.6 * np.sin(i * 0.7))
            poly_term += (x[i]**2) * (x[i]**self.poly_degree) * chaotic_factor
            
        # Sinusoidal component with dynamic frequencies
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.sin_freq * (1.0 + 0.8 * np.cos(i * 0.9))
            sin_term += np.sin(freq * x[i]) * np.cos(1.1 * freq * x[i])
            
        # Radial component with adaptive weighting
        r_squared = np.sum(x**2)
        radial_term = self.radial_weight * np.sqrt(r_squared + 1e-8)
        
        # Cross-dimensional interaction with chaotic coupling and rotation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_coupling = 1.0 + 0.7 * np.sin(i * j * 0.5)
                rotated_i = x[i] * np.cos(self.rotation_angles[i][j]) - x[j] * np.sin(self.rotation_angles[i][j])
                rotated_j = x[i] * np.sin(self.rotation_angles[i][j]) + x[j] * np.cos(self.rotation_angles[i][j])
                cross_term += chaotic_coupling * np.sin(rotated_i + rotated_j) * np.cos(0.8 * (rotated_i - rotated_j))
                
        # Chaotic barrier terms
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_pos = self.barrier_positions[i]
            barrier_width = self.barrier_widths[i]
            barrier_term += np.exp(-0.5 * ((x[i] - barrier_pos) / barrier_width)**2)
            
        # Adaptive conditioning with chaotic scaling
        cond_term = 0.0
        for i in range(self.dim):
            adaptive_scale = 1.0 + 1.0 * np.sin(i * 1.1 + self.chaotic_factor)
            cond_term += adaptive_scale * x[i]**4
            
        # Additional harmonic component for increased complexity
        harm_term = 0.0
        for i in range(self.dim):
            harm_term += np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) * (i + 1)
            
        # Combined fitness function
        total = poly_term + sin_term + radial_term + cross_term + barrier_term + cond_term + harm_term
        
        return total