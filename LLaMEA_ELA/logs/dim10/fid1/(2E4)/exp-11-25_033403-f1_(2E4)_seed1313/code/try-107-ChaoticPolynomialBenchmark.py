import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 4.0
        self.sin_freq = 4.0
        self.radial_weight = 1.2
        self.chaotic_factor = 5.0
        self.interaction_strength = 2.0
        self.barrier_positions = np.random.uniform(-4.8, 4.8, dim)
        self.barrier_widths = np.random.uniform(0.15, 1.1, dim)
        self.frequency_modulators = np.random.uniform(0.5, 1.5, dim)
        self.phase_shifts = np.random.uniform(-np.pi, np.pi, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with chaotic conditioning
        poly_term = 0.0
        for i in range(self.dim):
            chaotic_factor = self.chaotic_factor * (1.0 + 0.4 * np.sin(i * 0.5 + self.phase_shifts[i]))
            poly_term += (x[i]**2) * (x[i]**self.poly_degree) * chaotic_factor
            
        # Sinusoidal component with dynamic frequencies and phase shifts
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.sin_freq * self.frequency_modulators[i]
            sin_term += np.sin(freq * x[i] + self.phase_shifts[i]) * np.cos(0.7 * freq * x[i] + self.phase_shifts[i])
            
        # Radial component with adaptive weighting
        r_squared = np.sum(x**2)
        radial_term = self.radial_weight * np.log(r_squared + 1e-8) * np.sqrt(r_squared + 1e-8)
        
        # Cross-dimensional interaction with chaotic coupling and varying strengths
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_coupling = 1.0 + 0.5 * np.sin(i * j * 0.4 + self.phase_shifts[i] * self.phase_shifts[j])
                cross_term += chaotic_coupling * np.sin(x[i] + x[j]) * np.cos(0.5 * (x[i] - x[j]))
                
        # Chaotic barrier terms with varying shapes
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_pos = self.barrier_positions[i]
            barrier_width = self.barrier_widths[i]
            barrier_term += np.exp(-0.3 * ((x[i] - barrier_pos) / barrier_width)**2) + 0.5 * np.sin(2 * (x[i] - barrier_pos))
            
        # Adaptive conditioning with chaotic scaling and additional nonlinearity
        cond_term = 0.0
        for i in range(self.dim):
            adaptive_scale = 1.0 + 0.8 * np.sin(i * 0.9 + self.chaotic_factor * np.cos(i * 0.3))
            cond_term += adaptive_scale * x[i]**4
            
        # Additional fractal-like component for increased complexity
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(2**i * x[i]) * np.cos(3**i * x[i])
            
        # Combined fitness function
        total = poly_term + sin_term + radial_term + cross_term + barrier_term + cond_term + 0.5 * fractal_term
        
        return total