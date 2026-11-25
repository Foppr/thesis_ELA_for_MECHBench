import numpy as np

class ExponentialTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters with enhanced nonlinearity and chaos
        self.exp_decay = 0.7
        self.trig_amp = 2.5
        self.sphere_radius = 2.5
        self.noise_level = 0.04
        self.fractal_factor = 1.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with fractal-like scaling
        exp_sum = 0
        for i in range(self.dim):
            scale = 1 + 0.4 * np.sin(i * np.pi / (self.dim + 1)) + 0.3 * np.cos(i * np.pi / (self.dim + 2))
            exp_sum += np.exp(-self.exp_decay * np.abs(x[i])) * scale
            
        # Chaotic trigonometric coupling with fractal frequency modulation
        trig_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 2.5 + 2.0 * np.sin(i * np.pi / (self.dim + 3)) * np.cos(i * np.pi / (self.dim + 5))
                freq_j = 2.0 + 1.5 * np.cos(j * np.pi / (self.dim + 4)) * np.sin(j * np.pi / (self.dim + 6))
                coupling = np.sin(freq_i * x[i]) * np.cos(freq_j * x[j])
                # Fractal interaction strength
                interaction_strength = 1 + 0.3 * np.sin((i+j) * np.pi / self.dim) * np.cos((i-j) * np.pi / (self.dim + 1))
                trig_sum += coupling ** 2 * interaction_strength
                
        # Spherical component with fractal curvature and chaotic distortion
        sphere_sum = 0
        norm = np.linalg.norm(x)
        if norm > 0:
            base_distortion = (norm - self.sphere_radius) ** 2
            fractal_distortion = 1 + 0.4 * np.sin(norm * np.pi / (self.dim + 1)) + 0.3 * np.cos(norm * np.pi / (self.dim + 2))
            sphere_sum = base_distortion * fractal_distortion
            
        # Fractal adaptive conditioning with chaotic scaling
        cond_factor = 1.0 + 0.6 * np.log(self.dim + 1) + 0.15 * np.sin(self.dim * np.pi / 3) * np.cos(self.dim * np.pi / 5)
        
        # Enhanced noise injection with fractal variance
        noise = self.noise_level * np.random.normal(0, 1) * (1 + 0.3 * np.sin(self.dim * np.pi / 4))
        
        # Novel fractal cross-dimensional interaction term
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim):
                j = (i + 1) % self.dim
                # Fractal coupling with multiple scaling factors
                scale1 = 1 + 0.2 * np.sin(i * np.pi / self.dim)
                scale2 = 1 + 0.2 * np.cos(j * np.pi / self.dim)
                cross_term += x[i] * np.sin(x[j]) * scale1 * scale2 * (1 + 0.08 * np.sin((i+j) * np.pi / self.dim))
                
        # Add fractal-like interaction between all dimensions
        fractal_interaction = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    fractal_interaction += x[i] * np.sin(x[j]) * np.cos(i * j * np.pi / self.dim)
                    
        # Combine all components with proper scaling
        return cond_factor * (exp_sum + trig_sum + sphere_sum + self.fractal_factor * cross_term + 0.4 * fractal_interaction) + noise + 0.15 * self.dim