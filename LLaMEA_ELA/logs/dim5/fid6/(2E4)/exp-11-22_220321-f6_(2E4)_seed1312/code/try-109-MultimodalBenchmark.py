import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.conditioning = 15.0
        self.modulation_freq = 8.0
        self.decay_rate = 1.2
        self.fractal_dim = 0.7
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced quadratic base with fractal-like conditioning
        result = 0.0
        for i in range(self.dim):
            condition = self.conditioning * (1 + 0.7 * np.sin(i * 0.8) * np.cos(i * 0.3))
            result += condition * x[i]**2
            
        # Fractal exponential decay with chaotic modulation
        exp_decay = 0.0
        for i in range(self.dim):
            mod = 1 + 0.6 * np.sin(self.modulation_freq * x[i] + 0.5 * i + np.sin(i * 0.2))
            exp_decay += np.exp(-self.decay_rate * np.abs(x[i])) * mod * (1 + 0.3 * np.sin(x[i] * 10))
            
        # Hyper-coupled cross-dimensional interactions with chaotic phases
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1 + 0.8 * np.sin(0.9 * (x[i] + x[j]) + 0.3 * i * j + np.cos(i + j))
                cross_term += coupling * np.exp(-0.3 * (x[i]**2 + x[j]**2)) * (1 + 0.4 * np.sin(x[i] * x[j]))
                
        # Chaotic high-frequency oscillations with fractal scaling
        oscillation = 0.0
        for i in range(self.dim):
            freq = 10 + 5 * np.sin(i * 0.7) + 3 * np.cos(i * 0.4)
            oscillation += np.sin(freq * x[i]) * np.cos(5.0 * x[i]) * (1 + 0.2 * np.sin(x[i] * 15))
            
        # Complex polynomial-exponential mixture with chaotic scaling
        poly_exp = 0.0
        for i in range(self.dim):
            scale = 1 + 0.6 * np.sin(i * 1.5 + np.cos(i * 0.3))
            poly_exp += (x[i]**5 + x[i]**6) * np.exp(-0.4 * np.abs(x[i])) * scale * (1 + 0.3 * np.sin(x[i] * 8))
            
        # Hyper-chaotic phase-shifted interactions
        phase_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(0.7 * (x[i] - x[j]) + 0.2 * (i - j) + np.cos(i * j * 0.1))
                phase_interaction += np.exp(-0.9 * (x[i] - x[j])**2) * phase * (1 + 0.25 * np.sin(x[i] + x[j]))
                
        # Fractal global scaling with chaotic modulation
        global_scale = 1 + 0.5 * np.sin(np.sum(x) * 0.6 + np.cos(np.sum(x) * 0.3))
        
        return global_scale * (result + 0.7 * exp_decay + 0.6 * cross_term + 0.8 * oscillation + 0.7 * poly_exp + 0.5 * phase_interaction)