import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.conditioning = 20.0
        self.modulation_freq = 8.0
        self.decay_rate = 0.9
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic conditioning
        result = 0.0
        for i in range(self.dim):
            condition = self.conditioning * (1 + 0.8 * np.sin(i * 0.6))
            result += condition * x[i]**2
            
        # Nested exponential decay with sinusoidal modulation
        exp_decay = 0.0
        for i in range(self.dim):
            mod = 1 + 0.6 * np.sin(self.modulation_freq * x[i])
            exp_decay += np.exp(-self.decay_rate * np.abs(x[i])) * mod
            
        # Cross-dimensional interaction with dynamic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1 + 0.7 * np.sin(0.8 * (x[i] + x[j]))
                cross_term += coupling * np.exp(-0.2 * (x[i]**2 + x[j]**2))
                
        # Sinusoidal high-frequency oscillations
        oscillation = 0.0
        for i in range(self.dim):
            freq = 10 + 6 * np.sin(i * 1.2)
            oscillation += np.sin(freq * x[i]) * np.cos(3.0 * x[i])
            
        # Polynomial and exponential mixture with adaptive scaling
        poly_exp = 0.0
        for i in range(self.dim):
            scale = 1 + 0.5 * np.sin(i * 1.5)
            poly_exp += (x[i]**4 + x[i]**6 + x[i]**8) * np.exp(-0.3 * np.abs(x[i])) * scale
            
        # Dynamic phase-shifted interactions
        phase_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(0.6 * (x[i] - x[j]))
                phase_interaction += np.exp(-0.8 * (x[i] - x[j])**2) * phase
                
        # Additional higher-order cross-dimensional terms
        high_order_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    high_order_cross += np.sin(0.5 * (x[i] + x[j] + x[k])) * np.exp(-0.1 * (x[i]**2 + x[j]**2 + x[k]**2))
                    
        # Global scaling factor with sinusoidal modulation
        global_scale = 1 + 0.3 * np.sin(np.sum(x) * 0.5)
        
        return global_scale * (result + 0.6 * exp_decay + 0.4 * cross_term + 0.7 * oscillation + 0.6 * poly_exp + 0.35 * phase_interaction + 0.2 * high_order_cross)