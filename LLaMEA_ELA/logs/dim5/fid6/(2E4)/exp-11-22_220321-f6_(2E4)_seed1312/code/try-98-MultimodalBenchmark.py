import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.conditioning = 15.0
        self.modulation_freq = 3.0
        self.decay_rate = 0.7
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic conditioning
        result = 0.0
        for i in range(self.dim):
            condition = self.conditioning * (1 + 0.6 * np.sin(i * 0.4))
            result += condition * x[i]**2
            
        # Nested exponential decay with sinusoidal modulation
        exp_decay = 0.0
        for i in range(self.dim):
            mod = 1 + 0.4 * np.sin(self.modulation_freq * x[i])
            exp_decay += np.exp(-self.decay_rate * np.abs(x[i])) * mod
            
        # Cross-dimensional interaction with dynamic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1 + 0.5 * np.sin(0.6 * (x[i] + x[j]))
                cross_term += coupling * np.exp(-0.15 * (x[i]**2 + x[j]**2))
                
        # Sinusoidal high-frequency oscillations
        oscillation = 0.0
        for i in range(self.dim):
            freq = 6 + 4 * np.sin(i * 0.8)
            oscillation += np.sin(freq * x[i]) * np.cos(2.5 * x[i])
            
        # Polynomial and exponential mixture with adaptive scaling
        poly_exp = 0.0
        for i in range(self.dim):
            scale = 1 + 0.3 * np.sin(i * 1.0)
            poly_exp += (x[i]**3 + x[i]**5) * np.exp(-0.25 * np.abs(x[i])) * scale
            
        # Dynamic phase-shifted interactions
        phase_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(0.4 * (x[i] - x[j]))
                phase_interaction += np.exp(-0.6 * (x[i] - x[j])**2) * phase
                
        # Global scaling factor with sinusoidal modulation
        global_scale = 1 + 0.2 * np.sin(np.sum(x) * 0.3)
        
        # Additional harmonic interaction term for increased complexity
        harmonic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                harmonic_interaction += np.sin(0.5 * x[i] * x[j]) * np.exp(-0.3 * (x[i]**2 + x[j]**2))
                
        return global_scale * (result + 0.4 * exp_decay + 0.3 * cross_term + 0.5 * oscillation + 0.4 * poly_exp + 0.3 * phase_interaction + 0.15 * harmonic_interaction)