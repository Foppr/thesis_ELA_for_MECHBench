import numpy as np

class ExponentialTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize exponential and trigonometric parameters
        self.exp_decay = 0.8
        self.trig_amp = 1.3
        self.sphere_radius = 2.2
        self.noise_level = 0.05
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay potential component
        exp_sum = 0
        for i in range(self.dim):
            exp_sum += np.exp(-self.exp_decay * np.abs(x[i])) * (1 + 0.2 * np.sin(i * np.pi / (self.dim + 1)))
            
        # Trigonometric coupling terms with varying frequencies
        trig_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.5 + 0.2 * np.sin(i * np.pi / (self.dim + 3))
                freq_j = 0.9 + 0.3 * np.cos(j * np.pi / (self.dim + 4))
                coupling = np.sin(freq_i * x[i]) * np.cos(freq_j * x[j])
                trig_sum += coupling ** 2
                
        # Spherical symmetry component with adaptive radius
        sphere_sum = 0
        norm = np.linalg.norm(x)
        if norm > 0:
            sphere_sum = (norm - self.sphere_radius) ** 2 * (1 + 0.2 * np.sin(norm))
            
        # Add quartic terms for increased complexity
        quartic_sum = 0
        for i in range(self.dim):
            quartic_sum += 0.07 * x[i] ** 4
            
        # Adaptive conditioning based on dimensionality
        cond_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Noise injection for robustness
        noise = self.noise_level * np.random.normal(0, 1) * (1 + 0.1 * np.cos(self.dim))
        
        # Combine all components with proper scaling
        return cond_factor * (exp_sum + trig_sum + sphere_sum + quartic_sum) + noise + 0.2 * self.dim