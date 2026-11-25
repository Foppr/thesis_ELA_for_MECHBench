import numpy as np

class ExponentialTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced exponential decay parameters with fractal scaling
        self.exp_decay = 0.5 + 0.2 * np.sin(dim * np.pi / 8)
        self.trig_amp = 2.0 + 0.5 * np.cos(dim * np.pi / 6)
        self.sphere_radius = 3.0 + 0.8 * np.sin(dim * np.pi / 10)
        self.noise_level = 0.03 + 0.01 * np.cos(dim * np.pi / 12)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with chaotic modulation
        exp_sum = 0
        for i in range(self.dim):
            modulator = 1 + 0.4 * np.sin(i * np.pi / (self.dim + 2)) * np.cos(i * np.pi / (self.dim + 3))
            exp_sum += np.exp(-self.exp_decay * np.abs(x[i])) * modulator
            
        # Chaotic trigonometric coupling with fractal frequency patterns
        trig_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 2.0 + 1.5 * np.sin(i * np.pi / (self.dim + 4)) * np.cos(i * np.pi / (self.dim + 5))
                freq_j = 1.8 + 1.2 * np.cos(j * np.pi / (self.dim + 6)) * np.sin(j * np.pi / (self.dim + 7))
                coupling = np.sin(freq_i * x[i]) * np.cos(freq_j * x[j])
                # Add fractal interaction term
                fractal_term = 0.1 * np.sin((i+j) * np.pi / self.dim) * np.cos((i-j) * np.pi / (self.dim + 1))
                trig_sum += coupling ** 2 * (1 + fractal_term)
                
        # Fractal spherical symmetry with dynamic radius and chaotic curvature
        sphere_sum = 0
        norm = np.linalg.norm(x)
        if norm > 0:
            # Add chaotic curvature terms
            curvature = 1 + 0.3 * np.sin(norm * np.pi / 5) * np.cos(norm * np.pi / 7)
            sphere_sum = ((norm - self.sphere_radius) ** 2) * curvature
            
        # Enhanced adaptive conditioning with fractal scaling factor
        cond_factor = 1.5 + 0.6 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * np.pi / 8)
        
        # Fractal noise injection with chaotic variance
        noise = self.noise_level * np.random.normal(0, 1) * (1 + 0.2 * np.sin(self.dim * np.pi / 9))
        
        # Novel cross-dimensional synergy term with fractal interaction
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim):
                j = (i + 1) % self.dim
                synergy = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                # Add fractal scaling to synergy
                scale = 1 + 0.15 * np.sin(i * np.pi / (self.dim + 2)) * np.cos(j * np.pi / (self.dim + 3))
                cross_term += synergy * scale
                
        # Additional chaotic interaction term
        chaos_term = 0
        if self.dim > 2:
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    k = (i + j) % self.dim
                    if k != i and k != j:
                        chaos_term += np.sin(x[i] * x[j] * x[k]) * (1 + 0.08 * np.sin((i+j+k) * np.pi / self.dim))
        
        # Combine all components with proper scaling
        return cond_factor * (exp_sum + trig_sum + sphere_sum + 0.7 * cross_term + 0.3 * chaos_term) + noise + 0.12 * self.dim