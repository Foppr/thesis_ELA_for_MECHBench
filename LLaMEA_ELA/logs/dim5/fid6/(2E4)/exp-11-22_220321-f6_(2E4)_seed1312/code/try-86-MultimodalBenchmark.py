import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.conditioning = 10.0
        self.modulation_freq = 2.0
        self.decay_rate = 0.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic conditioning
        result = 0.0
        for i in range(self.dim):
            condition = self.conditioning * (1 + 0.5 * np.sin(i * 0.3))
            result += condition * x[i]**2
            
        # Nested exponential decay with sinusoidal modulation
        exp_decay = 0.0
        for i in range(self.dim):
            mod = 1 + 0.3 * np.sin(self.modulation_freq * x[i])
            exp_decay += np.exp(-self.decay_rate * np.abs(x[i])) * mod
            
        # Cross-dimensional interaction with dynamic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1 + 0.4 * np.sin(0.5 * (x[i] + x[j]))
                cross_term += coupling * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Sinusoidal high-frequency oscillations
        oscillation = 0.0
        for i in range(self.dim):
            freq = 5 + 3 * np.sin(i * 0.7)
            oscillation += np.sin(freq * x[i]) * np.cos(2 * x[i])
            
        # Polynomial and exponential mixture with adaptive scaling
        poly_exp = 0.0
        for i in range(self.dim):
            scale = 1 + 0.2 * np.sin(i * 0.9)
            poly_exp += (x[i]**3 + x[i]**5) * np.exp(-0.2 * np.abs(x[i])) * scale
            
        # Dynamic phase-shifted interactions
        phase_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(0.3 * (x[i] - x[j]))
                phase_interaction += np.exp(-0.5 * (x[i] - x[j])**2) * phase
                
        # Global scaling factor with sinusoidal modulation
        global_scale = 1 + 0.1 * np.sin(np.sum(x) * 0.2)
        
        return global_scale * (result + 0.3 * exp_decay + 0.25 * cross_term + 0.4 * oscillation + 0.35 * poly_exp + 0.2 * phase_interaction)