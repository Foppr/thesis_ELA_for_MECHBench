import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize landscape parameters
        self.exp_decay_base = 0.5
        self.trig_coupling_strength = 2.0
        self.noise_amplitude = 0.1
        self.adaptive_scale_factor = 1.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay potential component
        exp_sum = 0
        for i in range(self.dim):
            decay_factor = self.exp_decay_base ** (i + 1)
            exp_sum += decay_factor * np.exp(-0.5 * (x[i] / (1.0 + 0.1 * i)) ** 2)
            
        # Trigonometric coupling terms with adaptive weights
        trig_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 + 0.5 * np.sin((i + j) * np.pi / (self.dim + 1))
                coupling = np.sin(self.trig_coupling_strength * x[i]) * np.cos(self.trig_coupling_strength * x[j])
                trig_sum += weight * coupling
                
        # Adaptive noise injection with dimensionality scaling
        noise_sum = 0
        for i in range(self.dim):
            noise = self.noise_amplitude * (1.0 + 0.2 * np.sin(i * np.pi / (self.dim + 2))) * np.random.normal(0, 1)
            noise_sum += noise
            
        # Polynomial and sinusoidal modulation
        mod_sum = 0
        for i in range(self.dim):
            poly_term = x[i] ** 3
            sin_term = np.sin(3 * x[i])
            mod_sum += (poly_term + sin_term) ** 2
            
        # Cross-dimensional interaction with exponential scaling
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.exp(-0.1 * (x[i] - x[j]) ** 2) * np.cos(x[i] + x[j])
                cross_sum += interaction
                
        # Global scaling factor based on dimensionality
        scale_factor = self.adaptive_scale_factor * np.log(self.dim + 2)
        
        # Combine all components with proper weighting
        return scale_factor * (exp_sum + trig_sum + mod_sum + cross_sum) + noise_sum + 0.1 * self.dim