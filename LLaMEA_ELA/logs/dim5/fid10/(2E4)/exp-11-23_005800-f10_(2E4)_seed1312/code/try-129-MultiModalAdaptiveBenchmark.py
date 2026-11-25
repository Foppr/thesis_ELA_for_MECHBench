import numpy as np

class MultiModalAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.freq_base = 2.0
        self.amplitude = 1.5
        self.radial_decay = 0.1
        self.curvature_factor = 2.0
        self.noise_level = 0.01
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with adaptive curvature
        r = np.linalg.norm(x)
        radial_term = self.radial_decay * r**2 * np.exp(-r**2 / (2.0 * self.dim))
        
        # Multi-frequency sinusoidal terms
        sin_sum = 0.0
        for i in range(self.dim):
            freq = self.freq_base * (i + 1)
            sin_sum += np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Adaptive conditioning based on position
        cond_factor = 1.0
        for i in range(self.dim):
            cond_factor *= (1.0 + 0.5 * np.sin(x[i]))
            
        # Combined landscape with multiple local minima
        main_term = sin_sum**2 + self.amplitude * np.cos(0.5 * r) + radial_term
        
        # Add concave regions
        concave_terms = 0.0
        for i in range(self.dim):
            concave_terms += -0.3 * x[i]**4
            
        # Combine all components
        result = cond_factor * (main_term + concave_terms)
        
        # Add noise for robustness
        noise = np.random.normal(0, self.noise_level)
        
        return result + noise