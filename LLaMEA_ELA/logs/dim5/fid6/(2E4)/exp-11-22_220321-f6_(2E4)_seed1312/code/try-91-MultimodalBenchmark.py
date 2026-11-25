import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.conditioning = 15.0
        self.modulation_freq = 3.0
        self.decay_rate = 0.8
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with chaotic conditioning
        result = 0.0
        for i in range(self.dim):
            condition = self.conditioning * (1 + 0.7 * np.sin(i * 1.2 + np.sqrt(i + 1)))
            result += condition * x[i]**2
            
        # Nested exponential decay with chaotic modulation
        exp_decay = 0.0
        for i in range(self.dim):
            mod = 1 + 0.5 * np.sin(self.modulation_freq * x[i] + np.cos(i * 0.8))
            exp_decay += np.exp(-self.decay_rate * np.abs(x[i])) * mod
            
        # Cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1 + 0.6 * np.sin(0.7 * (x[i] + x[j]) + np.cos(i * j * 0.3))
                cross_term += coupling * np.exp(-0.15 * (x[i]**2 + x[j]**2))
                
        # Chaotic high-frequency oscillations
        oscillation = 0.0
        for i in range(self.dim):
            freq = 8 + 5 * np.sin(i * 0.9 + np.cos(i * 0.4))
            oscillation += np.sin(freq * x[i]) * np.cos(3 * x[i] + np.sin(i * 0.6))
            
        # Polynomial and exponential mixture with chaotic scaling
        poly_exp = 0.0
        for i in range(self.dim):
            scale = 1 + 0.3 * np.sin(i * 1.1 + np.cos(i * 0.5))
            poly_exp += (x[i]**3 + x[i]**5 + x[i]**7) * np.exp(-0.25 * np.abs(x[i])) * scale
            
        # Chaotic phase-shifted interactions
        phase_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(0.4 * (x[i] - x[j]) + np.cos(x[i] * x[j] * 0.2))
                phase_interaction += np.exp(-0.6 * (x[i] - x[j])**2) * phase
                
        # Radial basis function component with adaptive centers
        rbf = 0.0
        for i in range(self.dim):
            center = 2 * np.sin(i * 0.7 + np.cos(i * 0.3))
            rbf += np.exp(-0.3 * (x[i] - center)**2)
            
        # Global scaling factor with chaotic modulation
        global_scale = 1 + 0.2 * np.sin(np.sum(x) * 0.3 + np.cos(np.sum(x) * 0.1))
        
        return global_scale * (result + 0.4 * exp_decay + 0.3 * cross_term + 0.5 * oscillation + 0.4 * poly_exp + 0.25 * phase_interaction + 0.15 * rbf)