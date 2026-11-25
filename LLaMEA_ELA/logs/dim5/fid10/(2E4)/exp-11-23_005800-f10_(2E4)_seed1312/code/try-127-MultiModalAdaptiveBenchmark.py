import numpy as np

class MultiModalAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.freq_base = 3.0
        self.amplitude = 2.0
        self.radial_decay = 0.15
        self.curvature_factor = 3.0
        self.noise_level = 0.02
        self.phase_shift = np.random.uniform(0, 2*np.pi, dim)
        self.frequency_modulation = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced adaptive curvature
        r = np.linalg.norm(x)
        radial_term = self.radial_decay * r**3 * np.exp(-r**2 / (2.0 * self.dim))
        
        # Multi-frequency sinusoidal terms with chaotic phase interactions
        sin_sum = 0.0
        for i in range(self.dim):
            freq = self.freq_base * (i + 1) * self.frequency_modulation[i]
            phase = self.phase_shift[i] + np.sin(r * 0.1 * (i + 1))
            sin_sum += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase)
            
        # Dynamic conditioning with chaotic coupling terms
        cond_factor = 1.0
        for i in range(self.dim):
            cond_factor *= (1.0 + 0.3 * np.sin(x[i] * 2.0 + r * 0.5))
            
        # Energy-like potential wells with multiple local minima
        main_term = sin_sum**2 + self.amplitude * np.cos(0.3 * r) + radial_term
        
        # Add complex concave regions with variable curvature
        concave_terms = 0.0
        for i in range(self.dim):
            concave_terms += -0.4 * x[i]**4 + 0.1 * x[i]**6
            
        # Introduce chaotic saddle points and fractal-like structures
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += 0.2 * np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
            
        # Combine all components with dynamic scaling
        result = cond_factor * (main_term + concave_terms + saddle_term)
        
        # Add higher-order noise for increased robustness
        noise = np.random.normal(0, self.noise_level)
        
        return result + noise