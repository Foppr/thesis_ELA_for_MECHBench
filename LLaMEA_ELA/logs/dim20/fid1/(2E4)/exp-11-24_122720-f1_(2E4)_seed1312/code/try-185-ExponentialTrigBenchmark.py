import numpy as np

class ExponentialTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize exponential and trigonometric parameters with improved scaling
        self.exp_decay = 0.3
        self.trig_amp = 1.5
        self.sphere_radius = 2.5
        self.noise_level = 0.02
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay potential component with enhanced nonlinearity
        exp_sum = 0
        for i in range(self.dim):
            exp_sum += np.exp(-self.exp_decay * np.abs(x[i])) * (1 + 0.3 * np.sin(i * np.pi / (self.dim + 1)) + 0.2 * np.cos(i * np.pi / (self.dim + 2)))
            
        # Trigonometric coupling terms with cross-dimensional interactions
        trig_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.5 + 0.8 * np.sin(i * np.pi / (self.dim + 3))
                freq_j = 1.2 + 0.6 * np.cos(j * np.pi / (self.dim + 4))
                coupling = np.sin(freq_i * x[i]) * np.cos(freq_j * x[j]) * (1 + 0.1 * np.sin((i+j) * np.pi / self.dim))
                trig_sum += coupling ** 2
                
        # Spherical symmetry component with dynamic radius and enhanced curvature
        sphere_sum = 0
        norm = np.linalg.norm(x)
        if norm > 0:
            sphere_sum = ((norm - self.sphere_radius) ** 2) * (1 + 0.2 * np.sin(norm) + 0.1 * np.cos(norm))
            
        # Adaptive conditioning with improved scaling factor
        cond_factor = 1.0 + 0.4 * np.log(self.dim + 1) + 0.05 * np.sin(self.dim * np.pi / 4)
        
        # Enhanced noise injection with dimensionality-dependent variance
        noise = self.noise_level * np.random.normal(0, 1) * (1 + 0.1 * np.cos(self.dim))
        
        # Additional cross-dimensional interaction term for increased complexity
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim):
                cross_term += x[i] * np.sin(x[(i+1) % self.dim]) * (1 + 0.05 * np.cos(i * np.pi / self.dim))
                
        # Combine all components with proper scaling
        return cond_factor * (exp_sum + trig_sum + sphere_sum + 0.5 * cross_term) + noise + 0.08 * self.dim