import numpy as np

class MultiModalAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.freq_base = 3.0
        self.amplitude = 2.0
        self.radial_decay = 0.15
        self.curvature_factor = 3.0
        self.noise_level = 0.02
        self.phase_shift = np.random.rand(dim) * 2 * np.pi
        self.frequency_modulation = np.random.rand(dim) * 2 + 1
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced potential wells
        r = np.linalg.norm(x)
        radial_term = self.radial_decay * r**3 * np.exp(-r**2 / (2.0 * self.dim))
        
        # Multi-frequency sinusoidal terms with chaotic phase interactions
        sin_sum = 0.0
        for i in range(self.dim):
            freq = self.freq_base * self.frequency_modulation[i] * (i + 1)
            phase = self.phase_shift[i] + np.sin(r * 0.5) * 0.1
            sin_sum += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase)
            
        # Adaptive conditioning with dynamic curvature
        cond_factor = 1.0
        for i in range(self.dim):
            cond_factor *= (1.0 + 0.3 * np.sin(x[i]) * np.cos(x[i]))
            
        # Enhanced landscape with multiple energy basins
        main_term = sin_sum**2 + self.amplitude * np.cos(0.3 * r) + radial_term
        
        # Add complex concave and convex regions
        concave_terms = 0.0
        convex_terms = 0.0
        for i in range(self.dim):
            concave_terms += -0.4 * x[i]**4
            convex_terms += 0.2 * x[i]**6
            
        # Add chaotic saddle points
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += np.sin(x[i] * 10) * np.cos(x[i] * 15)
            
        # Combine all components
        result = cond_factor * (main_term + concave_terms + convex_terms + saddle_term)
        
        # Add chaotic noise for robustness
        noise = np.random.normal(0, self.noise_level)
        
        return result + noise