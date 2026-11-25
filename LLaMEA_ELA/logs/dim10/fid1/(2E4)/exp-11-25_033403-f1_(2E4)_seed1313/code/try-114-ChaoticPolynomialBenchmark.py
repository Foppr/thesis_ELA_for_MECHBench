import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 4.0
        self.sin_freq = 2.5
        self.radial_scale = 1.2
        self.chaos_factor = 3.0
        self.barrier_height = 2.0
        self.interaction_strength = 1.5
        self.noise_level = 0.1
        self.rotation_angles = np.random.uniform(-np.pi, np.pi, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with varying degrees
        poly_term = 0.0
        for i in range(self.dim):
            degree = self.poly_degree * (1.0 + 0.3 * np.sin(i * 0.5))
            poly_term += x[i]**degree
            
        # Sinusoidal component with chaotic frequency modulation
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.sin_freq * (1.0 + self.chaos_factor * np.sin(i * 0.3 + x[i]))
            sin_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Radial component with barrier structures
        radial_term = 0.0
        for i in range(self.dim):
            distance = np.abs(x[i])
            radial_term += self.radial_scale * (distance**2 + self.barrier_height * np.exp(-distance))
            
        # Cross-dimensional coupling with chaotic interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction term
                interaction = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                cross_term += self.interaction_strength * interaction
                
        # Modified rotation with chaotic angles
        rot_term = 0.0
        for i in range(self.dim):
            rotated_x = x[i] * np.cos(self.rotation_angles[i]) - x[(i+1) % self.dim] * np.sin(self.rotation_angles[i])
            rot_term += rotated_x**3
            
        # Noise injection to increase complexity
        noise = 0.0
        for i in range(self.dim):
            noise += self.noise_level * np.sin(i * 1.2 + x[i]) * np.cos(i * 0.7 + x[i])
            
        # Combined fitness function with chaotic weighting
        total = poly_term + sin_term + radial_term + cross_term + rot_term + noise
        
        return total