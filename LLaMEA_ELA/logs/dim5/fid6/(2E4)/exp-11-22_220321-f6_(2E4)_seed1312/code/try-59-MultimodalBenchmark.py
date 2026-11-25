import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.delay = 3
        self.adaptation_factor = 0.3
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with enhanced adaptive scaling
        result = 0.0
        for i in range(self.dim):
            result += (x[i] ** 2) * (1 + self.adaptation_factor * np.sin(i * 0.7))
            
        # Chaotic component using delayed feedback with altered amplitude and phase
        chaotic_term = 0.0
        for i in range(self.dim):
            delayed_idx = (i - self.delay) % self.dim
            if delayed_idx < 0:
                delayed_idx += self.dim
            chaotic_term += np.sin(x[i] + 0.4 * x[delayed_idx]) * np.cos(1.5 * x[i])
            
        # Adaptive frequency modulation with modified exponential decay and phase shift
        freq_mod = 0.0
        for i in range(self.dim):
            freq = 3 ** (i % 4) * (1 + 0.25 * np.sin(x[i] * 0.5))  # Changed base and amplitude
            freq_mod += np.sin(freq * x[i]) * np.cos(freq * x[(i + 3) % self.dim] + 0.3)
            
        # Cross-dimensional interaction with modified weights, delayed components, and enhanced coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                delayed_i = (i - self.delay) % self.dim
                delayed_j = (j - self.delay) % self.dim
                if delayed_i < 0:
                    delayed_i += self.dim
                if delayed_j < 0:
                    delayed_j += self.dim
                    
                cross_term += (x[i] * x[j] + 0.2 * x[delayed_i] * x[delayed_j]) * \
                             np.exp(-0.2 * (x[i] - x[j])**2) * np.sin(2.5 * (x[i] + x[j]))
                
        # Penalty term with altered polynomial powers, modified coefficients and additional harmonic components
        penalty = 0.0
        for i in range(self.dim):
            penalty += (x[i]**12 + x[i]**10 + x[i]**8 + x[i]**6 + x[i]**4) * (1 + 0.35 * np.cos(i * 0.8))
            
        # Additional harmonic component to increase multimodality
        harmonic = 0.0
        for i in range(self.dim):
            harmonic += np.sin(3 * x[i]) * np.cos(2 * x[(i + 1) % self.dim])
            
        return result + 0.4 * chaotic_term + 0.3 * freq_mod + 0.35 * cross_term + 0.35 * penalty + 0.2 * harmonic