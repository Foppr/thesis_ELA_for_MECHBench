import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.exp_base = 3.0
        self.trig_freq = 4.0
        self.spherical_weight = 1.2
        self.chaotic_factor = 2.5
        self.barrier_strength = 3.0
        self.polynomial_degree = 5
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential component with chaotic base and adaptive exponents
        exp_term = 0.0
        for i in range(self.dim):
            chaotic_exp = self.exp_base ** (i / self.dim * self.chaotic_factor)
            exp_term += np.exp(chaotic_exp * x[i]) - 1.0
            
        # Trigonometric component with chaotic frequencies and phase shifts
        trig_term = 0.0
        for i in range(self.dim):
            freq = self.trig_freq * (1 + 0.4 * np.sin(i * 0.6 + 1.2))
            phase = 0.3 * np.cos(i * 0.8 + 0.5)
            trig_term += np.sin(freq * x[i] + phase) * np.cos(0.9 * freq * x[i] + phase)
            
        # Spherical component with polynomial weighting
        r_squared = np.sum(x**2)
        spherical_term = self.spherical_weight * (r_squared ** (self.polynomial_degree / 2))
        
        # Cross-dimensional interaction with chaotic coupling coefficients
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_coupling = 0.6 + 0.4 * np.sin(0.4 * (i + j) + 0.8)
                cross_term += chaotic_coupling * np.sin(x[i] * x[j]) * np.exp(-0.15 * abs(x[i] - x[j]))
                
        # Chaotic barrier terms with dynamic positions and strengths
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_pos = 2.5 * np.sin(i * 0.9 + 1.5)
            barrier_width = 0.4 + 0.3 * np.cos(i * 0.7 + 0.6)
            barrier_term += self.barrier_strength * np.exp(-0.5 * ((x[i] - barrier_pos) / barrier_width)**2)
            
        # Chaotic conditioning with polynomial scaling
        cond_term = 0.0
        for i in range(self.dim):
            chaotic_scale = 1.0 + 0.6 * np.sin(i * 0.5 + 0.9)
            cond_term += chaotic_scale * x[i]**self.polynomial_degree
            
        # Combined fitness function
        total = exp_term + trig_term + spherical_term + cross_term + barrier_term + cond_term
        
        return total