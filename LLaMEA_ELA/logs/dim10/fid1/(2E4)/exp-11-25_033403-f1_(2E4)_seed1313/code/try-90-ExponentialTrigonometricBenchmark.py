import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.exp_base = 2.0
        self.trig_freq = 3.0
        self.spherical_weight = 0.8
        self.adaptive_factor = 1.5
        self.barrier_strength = 2.0
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential component with base scaling and adaptive exponents
        exp_term = 0.0
        for i in range(self.dim):
            adaptive_exp = self.exp_base ** (i / self.dim * self.adaptive_factor)
            exp_term += np.exp(adaptive_exp * x[i]) - 1.0
            
        # Trigonometric component with multiple frequencies and phase shifts
        trig_term = 0.0
        for i in range(self.dim):
            freq = self.trig_freq * (1 + 0.3 * np.sin(i * 0.5))
            phase = 0.2 * np.cos(i * 0.7)
            trig_term += np.sin(freq * x[i] + phase) * np.cos(0.8 * freq * x[i] + phase)
            
        # Spherical component with dynamic weighting
        r_squared = np.sum(x**2)
        spherical_term = self.spherical_weight * r_squared
        
        # Cross-dimensional interaction with dynamic coupling coefficients
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.5 * np.sin(0.3 * (i + j))
                cross_term += coupling * np.sin(x[i] * x[j]) * np.exp(-0.1 * abs(x[i] - x[j]))
                
        # Dynamic barrier terms with varying strength and positions
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_pos = 3.0 * np.sin(i * 0.8)
            barrier_width = 0.5 + 0.3 * np.cos(i * 0.6)
            barrier_term += self.barrier_strength * np.exp(-0.5 * ((x[i] - barrier_pos) / barrier_width)**2)
            
        # Adaptive conditioning with dimension-dependent scaling
        cond_term = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(i * 0.4)
            cond_term += scale_factor * x[i]**3
            
        # Combined fitness function
        total = exp_term + trig_term + spherical_term + cross_term + barrier_term + cond_term
        
        return total