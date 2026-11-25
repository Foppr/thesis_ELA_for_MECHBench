import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 4.0
        self.sin_freq = 2.5
        self.radial_weight = 0.7
        self.chaotic_factor = 3.8
        self.interaction_strength = 1.2
        self.barrier_positions = np.random.uniform(-4.0, 4.0, dim)
        self.barrier_widths = np.random.uniform(0.3, 0.8, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with chaotic conditioning
        poly_term = 0.0
        for i in range(self.dim):
            chaotic_factor = self.chaotic_factor * (1.0 + 0.2 * np.sin(i * 0.3))
            poly_term += (x[i]**2) * (x[i]**self.poly_degree) * chaotic_factor
            
        # Sinusoidal component with dynamic frequencies
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.sin_freq * (1.0 + 0.4 * np.cos(i * 0.5))
            sin_term += np.sin(freq * x[i]) * np.cos(0.7 * freq * x[i])
            
        # Radial component with adaptive weighting
        r_squared = np.sum(x**2)
        radial_term = self.radial_weight * np.sqrt(r_squared + 1e-8)
        
        # Cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_coupling = 1.0 + 0.3 * np.sin(i * j * 0.2)
                cross_term += chaotic_coupling * np.sin(x[i] + x[j]) * np.cos(0.5 * (x[i] - x[j]))
                
        # Chaotic barrier terms
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_pos = self.barrier_positions[i]
            barrier_width = self.barrier_widths[i]
            barrier_term += np.exp(-0.5 * ((x[i] - barrier_pos) / barrier_width)**2)
            
        # Adaptive conditioning with chaotic scaling
        cond_term = 0.0
        for i in range(self.dim):
            adaptive_scale = 1.0 + 0.6 * np.sin(i * 0.7 + self.chaotic_factor)
            cond_term += adaptive_scale * x[i]**4
            
        # Combined fitness function
        total = poly_term + sin_term + radial_term + cross_term + barrier_term + cond_term
        
        return total