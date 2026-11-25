import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.conditioning = 12.0
        self.modulation_freq = 4.0
        self.decay_rate = 0.8
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic conditioning
        result = 0.0
        for i in range(self.dim):
            condition = self.conditioning * (1 + 0.5 * np.sin(i * 0.5))
            result += condition * x[i]**2
            
        # Modified exponential decay with enhanced sinusoidal modulation
        exp_decay = 0.0
        for i in range(self.dim):
            mod = 1 + 0.5 * np.sin(self.modulation_freq * x[i] + 0.3 * i)
            exp_decay += np.exp(-self.decay_rate * np.abs(x[i])) * mod
            
        # Cross-dimensional interaction with stronger coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1 + 0.6 * np.sin(0.7 * (x[i] + x[j]) + 0.2 * i * j)
                cross_term += coupling * np.exp(-0.2 * (x[i]**2 + x[j]**2))
                
        # Enhanced sinusoidal high-frequency oscillations
        oscillation = 0.0
        for i in range(self.dim):
            freq = 7 + 3 * np.sin(i * 0.9)
            oscillation += np.sin(freq * x[i]) * np.cos(3.0 * x[i])
            
        # Modified polynomial and exponential mixture with adaptive scaling
        poly_exp = 0.0
        for i in range(self.dim):
            scale = 1 + 0.4 * np.sin(i * 1.2)
            poly_exp += (x[i]**4 + x[i]**5) * np.exp(-0.3 * np.abs(x[i])) * scale
            
        # Improved dynamic phase-shifted interactions
        phase_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(0.5 * (x[i] - x[j]) + 0.1 * (i - j))
                phase_interaction += np.exp(-0.7 * (x[i] - x[j])**2) * phase
                
        # Global scaling factor with enhanced sinusoidal modulation
        global_scale = 1 + 0.3 * np.sin(np.sum(x) * 0.4)
        
        return global_scale * (result + 0.5 * exp_decay + 0.4 * cross_term + 0.6 * oscillation + 0.5 * poly_exp + 0.3 * phase_interaction)