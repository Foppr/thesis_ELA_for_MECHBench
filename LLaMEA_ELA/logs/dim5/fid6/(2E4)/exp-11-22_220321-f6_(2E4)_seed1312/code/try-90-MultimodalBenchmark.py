import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.conditioning = 15.0
        self.modulation_freq = 3.0
        self.decay_rate = 0.3
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with chaotic conditioning
        result = 0.0
        for i in range(self.dim):
            condition = self.conditioning * (1 + 0.7 * np.sin(i * 2.3) * np.cos(i * 1.7))
            result += condition * x[i]**2
            
        # Chaotic exponential decay with multi-frequency modulation
        exp_decay = 0.0
        for i in range(self.dim):
            mod = 1 + 0.4 * (np.sin(self.modulation_freq * x[i]) + 
                           0.5 * np.cos(2 * self.modulation_freq * x[i]) + 
                           0.3 * np.sin(3 * self.modulation_freq * x[i]))
            exp_decay += np.exp(-self.decay_rate * np.abs(x[i])) * mod
            
        # Radial basis function interactions with dynamic centers
        rbf_term = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * 0.5)
            rbf_term += np.exp(-0.5 * (x[i] - center)**2 / (0.5 + 0.3 * np.sin(i * 1.2)))
            
        # Cross-dimensional chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1 + 0.5 * np.sin(0.7 * (x[i] + x[j]) + 
                                          0.3 * np.cos(x[i] - x[j]))
                cross_term += coupling * np.exp(-0.2 * (x[i]**2 + x[j]**2))
                
        # High-dimensional chaotic oscillations
        oscillation = 0.0
        for i in range(self.dim):
            freq = 7 + 4 * np.sin(i * 0.8) * np.cos(i * 0.6)
            oscillation += np.sin(freq * x[i]) * np.cos(3 * x[i]) * np.sin(2 * x[i])
            
        # Polynomial and chaotic mixture with dynamic scaling
        poly_exp = 0.0
        for i in range(self.dim):
            scale = 1 + 0.3 * np.sin(i * 1.1) * np.cos(i * 0.9)
            poly_exp += (x[i]**4 + x[i]**6) * np.exp(-0.15 * np.abs(x[i])) * scale
            
        # Adaptive phase-shifted interactions with chaotic phases
        phase_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(0.4 * (x[i] - x[j]) + 
                              0.2 * np.cos(x[i] + x[j]))
                phase_interaction += np.exp(-0.3 * (x[i] - x[j])**2) * phase
                
        # Chaotic global scaling factor
        global_scale = 1 + 0.2 * np.sin(np.sum(x) * 0.5) * np.cos(np.sum(x) * 0.3)
        
        return global_scale * (result + 0.4 * exp_decay + 0.3 * rbf_term + 
                              0.25 * cross_term + 0.45 * oscillation + 
                              0.4 * poly_exp + 0.25 * phase_interaction)