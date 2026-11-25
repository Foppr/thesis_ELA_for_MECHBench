import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.delay = 2
        self.adaptation_factor = 0.1
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = 0.0
        for i in range(self.dim):
            result += (x[i] ** 2) * (1 + self.adaptation_factor * np.sin(i))
            
        # Chaotic component using delayed feedback
        chaotic_term = 0.0
        for i in range(self.dim):
            delayed_idx = (i - self.delay) % self.dim
            if delayed_idx < 0:
                delayed_idx += self.dim
            chaotic_term += np.sin(x[i] + 0.5 * x[delayed_idx]) * np.cos(2 * x[i])
            
        # Adaptive frequency modulation with exponential decay
        freq_mod = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 4) * (1 + 0.3 * np.sin(x[i]))
            freq_mod += np.sin(freq * x[i]) * np.cos(freq * x[(i + 2) % self.dim])
            
        # Cross-dimensional interaction with time-delayed components
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                delayed_i = (i - self.delay) % self.dim
                delayed_j = (j - self.delay) % self.dim
                if delayed_i < 0:
                    delayed_i += self.dim
                if delayed_j < 0:
                    delayed_j += self.dim
                    
                cross_term += (x[i] * x[j] + 0.1 * x[delayed_i] * x[delayed_j]) * \
                             np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(3 * (x[i] + x[j]))
                
        # Penalty term with multiple local optima
        penalty = 0.0
        for i in range(self.dim):
            penalty += (x[i]**8 + x[i]**6 + x[i]**4 + x[i]**2) * (1 + 0.5 * np.cos(i))
            
        return result + 0.3 * chaotic_term + 0.2 * freq_mod + 0.15 * cross_term + 0.25 * penalty