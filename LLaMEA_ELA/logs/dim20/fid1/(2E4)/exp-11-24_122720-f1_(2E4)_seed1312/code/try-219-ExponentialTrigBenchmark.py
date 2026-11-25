import numpy as np

class ExponentialTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize exponential and trigonometric parameters with increased complexity
        self.exp_decay = 1.9
        self.trig_amp = 2.7
        self.sphere_radius = 2.1
        self.noise_level = 0.02
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay potential component with enhanced nonlinearity and chaotic modulation
        exp_sum = 0
        for i in range(self.dim):
            exp_sum += np.exp(-self.exp_decay * np.abs(x[i])) * (1 + 0.7 * np.sin(i * np.pi / (self.dim + 1)) + 0.25 * np.cos(i * np.pi / (self.dim + 3)) + 0.1 * np.sin(i * np.pi / (self.dim + 5)))
            
        # Trigonometric coupling terms with stronger interactions, more frequencies and chaotic modulation
        trig_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 2.5 + 0.4 * np.sin(i * np.pi / (self.dim + 2)) + 0.2 * np.cos(i * np.pi / (self.dim + 4)) + 0.1 * np.sin(i * np.pi / (self.dim + 6))
                freq_j = 1.9 + 0.3 * np.cos(j * np.pi / (self.dim + 3)) + 0.25 * np.sin(j * np.pi / (self.dim + 5)) + 0.15 * np.cos(j * np.pi / (self.dim + 7))
                coupling = np.sin(freq_i * x[i]) * np.cos(freq_j * x[j]) * np.exp(-0.15 * np.abs(x[i] - x[j])) * (1 + 0.1 * np.sin(i * j))
                trig_sum += coupling ** 2
                
        # Spherical symmetry component with adaptive radius, additional harmonic terms and chaotic modulation
        sphere_sum = 0
        norm = np.linalg.norm(x)
        if norm > 0:
            sphere_sum = (norm - self.sphere_radius) ** 2 * (1 + 0.3 * np.sin(norm) + 0.15 * np.cos(norm) + 0.05 * np.sin(norm ** 2))
            
        # Add higher-order polynomial terms for increased complexity with chaotic coefficients
        quartic_sum = 0
        quintic_sum = 0
        for i in range(self.dim):
            quartic_sum += 0.15 * x[i] ** 4 * (1 + 0.1 * np.sin(i))
            quintic_sum += 0.03 * x[i] ** 5 * (1 + 0.05 * np.cos(i))
            
        # Adaptive conditioning based on dimensionality with enhanced scaling and chaotic modulation
        cond_factor = 1.0 + 0.4 * np.log(self.dim + 1) + 0.1 * np.sin(np.log(self.dim + 1)) + 0.05 * np.cos(self.dim)
        
        # Noise injection for robustness with chaotic perturbation
        noise = self.noise_level * np.random.normal(0, 1) * (1 + 0.15 * np.cos(self.dim) + 0.08 * np.sin(self.dim) + 0.03 * np.cos(self.dim ** 2))
        
        # Combine all components with proper scaling and chaotic adjustment
        return cond_factor * (exp_sum + trig_sum + sphere_sum + quartic_sum + quintic_sum) + noise + 0.4 * self.dim