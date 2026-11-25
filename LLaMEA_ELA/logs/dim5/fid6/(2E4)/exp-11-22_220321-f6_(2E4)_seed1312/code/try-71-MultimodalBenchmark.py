import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.delay = 3
        self.adaptation_factor = 0.6
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with enhanced adaptive scaling
        result = 0.0
        for i in range(self.dim):
            result += (x[i] ** 2) * (1 + self.adaptation_factor * np.sin(i * 0.9))
            
        # Enhanced chaotic component using delayed feedback with increased amplitude
        chaotic_term = 0.0
        for i in range(self.dim):
            delayed_idx = (i - self.delay) % self.dim
            if delayed_idx < 0:
                delayed_idx += self.dim
            chaotic_term += np.sin(x[i] + 0.9 * x[delayed_idx]) * np.cos(2.5 * x[i])
            
        # Enhanced frequency modulation with exponential decay and higher harmonics
        freq_mod = 0.0
        for i in range(self.dim):
            freq = 5 ** (i % 4) * (1 + 0.5 * np.sin(x[i]))  # Increased base and amplitude
            freq_mod += np.sin(freq * x[i]) * np.cos(freq * x[(i + 2) % self.dim]) * np.sin(3.5 * x[i])
            
        # Stronger cross-dimensional interaction with delayed components and higher-order terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                delayed_i = (i - self.delay) % self.dim
                delayed_j = (j - self.delay) % self.dim
                if delayed_i < 0:
                    delayed_i += self.dim
                if delayed_j < 0:
                    delayed_j += self.dim
                    
                cross_term += (x[i] * x[j] + 0.4 * x[delayed_i] * x[delayed_j]) * \
                             np.exp(-0.2 * (x[i] - x[j])**2) * np.sin(5.0 * (x[i] + x[j]))
                
        # Enhanced penalty term with higher polynomial powers and modified coefficients
        penalty = 0.0
        for i in range(self.dim):
            penalty += (x[i]**16 + x[i]**14 + x[i]**12 + x[i]**10 + x[i]**8) * (1 + 0.6 * np.cos(i * 1.1))
            
        # Additional harmonic modulation component
        harm_term = 0.0
        for i in range(self.dim):
            harm_term += np.sin(3.0 * x[i]) * np.cos(4.0 * x[(i + 1) % self.dim]) * np.exp(-0.2 * x[i]**2)
            
        return result + 0.7 * chaotic_term + 0.6 * freq_mod + 0.6 * cross_term + 0.6 * penalty + 0.4 * harm_term