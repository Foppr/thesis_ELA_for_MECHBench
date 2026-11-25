import numpy as np

class MultiModalAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.freq_base = 3.5
        self.amplitude = 2.5
        self.radial_decay = 0.2
        self.curvature_factor = 3.5
        self.noise_level = 0.003
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced adaptive curvature
        r = np.linalg.norm(x)
        radial_term = self.radial_decay * r**3 * np.exp(-r**2 / (2.0 * self.dim))
        
        # Multi-frequency sinusoidal terms with chaotic modulation
        sin_sum = 0.0
        for i in range(self.dim):
            freq = self.freq_base * (i + 1) * (1.0 + 0.35 * np.sin(0.7 * r))
            sin_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] + i * 0.5)
            
        # Adaptive conditioning with dynamic scaling
        cond_factor = 1.0
        for i in range(self.dim):
            cond_factor *= (1.0 + 0.45 * np.sin(x[i] * (1.0 + 0.25 * r)))
            
        # Combined landscape with enhanced multimodality
        main_term = sin_sum**2 + self.amplitude * np.cos(0.3 * r) + radial_term
        
        # Add complex concave regions with variable curvature
        concave_terms = 0.0
        for i in range(self.dim):
            concave_terms += -0.45 * x[i]**4 * (1.0 + 0.12 * np.sin(2.0 * x[i]))
            
        # Add chaotic saddle points and energy wells
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += 0.25 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            
        # Add radial coupling between dimensions
        radial_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                radial_coupling += 0.1 * x[i] * x[j] * np.exp(-0.5 * (x[i]**2 + x[j]**2))
                
        # Combine all components with dynamic weighting
        result = cond_factor * (main_term + concave_terms + saddle_term + radial_coupling)
        
        # Add structured noise for robustness
        noise = np.random.normal(0, self.noise_level)
        
        return result + noise