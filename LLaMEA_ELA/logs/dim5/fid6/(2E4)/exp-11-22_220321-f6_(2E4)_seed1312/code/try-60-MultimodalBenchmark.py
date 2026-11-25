import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.delay = 2
        self.adaptation_factor = 0.2
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = 0.0
        for i in range(self.dim):
            result += (x[i] ** 2) * (1 + self.adaptation_factor * np.sin(i * 0.5))
            
        # Chaotic component using delayed feedback with altered amplitude
        chaotic_term = 0.0
        for i in range(self.dim):
            delayed_idx = (i - self.delay) % self.dim
            if delayed_idx < 0:
                delayed_idx += self.dim
            chaotic_term += np.sin(x[i] + 0.5 * x[delayed_idx]) * np.cos(1.2 * x[i])
            
        # Adaptive frequency modulation with modified exponential decay
        freq_mod = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 3) * (1 + 0.2 * np.sin(x[i]))  # Changed base and amplitude
            freq_mod += np.sin(freq * x[i]) * np.cos(freq * x[(i + 2) % self.dim])
            
        # Cross-dimensional interaction with modified weights and delayed components
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                delayed_i = (i - self.delay) % self.dim
                delayed_j = (j - self.delay) % self.dim
                if delayed_i < 0:
                    delayed_i += self.dim
                if delayed_j < 0:
                    delayed_j += self.dim
                    
                cross_term += (x[i] * x[j] + 0.15 * x[delayed_i] * x[delayed_j]) * \
                             np.exp(-0.15 * (x[i] - x[j])**2) * np.sin(2.0 * (x[i] + x[j]))
                
        # Penalty term with altered polynomial powers and modified coefficients
        penalty = 0.0
        for i in range(self.dim):
            penalty += (x[i]**10 + x[i]**8 + x[i]**6 + x[i]**4) * (1 + 0.3 * np.cos(i * 0.7))
            
        return result + 0.35 * chaotic_term + 0.25 * freq_mod + 0.3 * cross_term + 0.3 * penalty