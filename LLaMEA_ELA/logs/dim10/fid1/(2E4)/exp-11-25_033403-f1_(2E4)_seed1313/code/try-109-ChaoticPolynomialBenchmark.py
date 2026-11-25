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
        self.fractal_exponent = 0.7
        self.peak_positions = np.random.uniform(-4.0, 4.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with fractal-like conditioning
        poly_term = 0.0
        for i in range(self.dim):
            chaotic_factor = self.chaotic_factor * (1.0 + 0.4 * np.sin(i * 0.5))
            poly_term += (x[i]**2) * (x[i]**self.poly_degree) * chaotic_factor * (1.0 + 0.2 * np.sin(x[i] * 3.0))
            
        # Modified sinusoidal component with fractal frequency modulation
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.sin_freq * (1.0 + 0.6 * np.cos(i * 0.7) * np.sin(x[i] * 0.5))
            sin_term += np.sin(freq * x[i]) * np.cos(0.9 * freq * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Enhanced radial component with fractal scaling
        r_squared = np.sum(x**2)
        radial_term = self.radial_weight * (r_squared + 1e-8)**self.fractal_exponent
            
        # Improved cross-dimensional interaction with fractal coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                fractal_coupling = 1.0 + 0.5 * np.sin(i * j * 0.4) * np.cos(x[i] * x[j] * 0.3)
                cross_term += fractal_coupling * np.sin(x[i] + x[j]) * np.cos(0.7 * (x[i] - x[j]))
                
        # Advanced chaotic barrier terms with multiple peaks
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_pos = self.barrier_positions[i]
            barrier_width = self.barrier_widths[i]
            barrier_term += np.exp(-0.5 * ((x[i] - barrier_pos) / barrier_width)**2) + \
                          0.3 * np.exp(-0.5 * ((x[i] - (barrier_pos + 1.5)) / (barrier_width * 0.7))**2)
            
        # Fractal conditioning term
        cond_term = 0.0
        for i in range(self.dim):
            fractal_scale = 1.0 + 0.8 * np.sin(i * 0.9 + self.chaotic_factor) * np.cos(x[i] * 0.4)
            cond_term += fractal_scale * x[i]**4
            
        # Peak attraction component
        peak_term = 0.0
        for i in range(self.dim):
            peak_pos = self.peak_positions[i]
            peak_term += 0.5 * np.exp(-0.5 * ((x[i] - peak_pos) / 1.2)**2)
            
        # Combined fitness function
        total = poly_term + sin_term + radial_term + cross_term + barrier_term + cond_term + peak_term
        
        return total