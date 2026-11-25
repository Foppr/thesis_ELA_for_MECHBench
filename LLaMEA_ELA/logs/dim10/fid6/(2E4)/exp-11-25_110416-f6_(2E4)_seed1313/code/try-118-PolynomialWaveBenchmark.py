import numpy as np

class PolynomialWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for adaptive conditioning
        self.chaos_seq = np.array([0.5])
        for _ in range(dim * 20):
            self.chaos_seq = np.append(self.chaos_seq, 4 * self.chaos_seq[-1] * (1 - self.chaos_seq[-1]))
            
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with adaptive conditioning
        result = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.5 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 20)
            result += cond_factor * x[i]**4 - 2 * x[i]**2
        
        # Add trigonometric wave interference patterns
        for i in range(self.dim):
            wave_sum = 0.0
            for k in range(1, min(6, self.dim + 1)):
                freq = k * (1 + 0.3 * np.cos(self.chaos_seq[(i+k) % len(self.chaos_seq)]))
                wave_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            result += 0.8 * wave_sum
            
        # Add polynomial chaos components with varying exponents
        for i in range(min(15, self.dim)):
            exp_factor = 2 + 3 * np.sin(self.chaos_seq[(i*7) % len(self.chaos_seq)])
            result += 0.3 * (x[i] ** exp_factor) * np.cos(3 * x[i])
            
        # Add cross-dimensional coupling with chaotic interaction strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = 0.5 + 0.5 * np.sin(self.chaos_seq[(i*j) % len(self.chaos_seq)] * 10)
                result += coupling * x[i]**2 * x[j]**2
                
        # Add multi-scale oscillatory components
        for i in range(self.dim):
            osc_sum = 0.0
            for k in range(1, min(8, self.dim + 1)):
                scale = 1.0 / (k**1.5)
                osc_sum += scale * np.sin(k * x[i]) * np.cos(k * x[i] * 0.3)
            result += 0.4 * osc_sum
            
        # Add adaptive noise with chaotic amplitude modulation
        for i in range(self.dim):
            noise_amp = 0.2 + 0.1 * np.sin(self.chaos_seq[(i*13) % len(self.chaos_seq)] * 50)
            result += noise_amp * np.sin(25 * x[i])
            
        # Add basin boundary regions with varying steepness
        for i in range(self.dim):
            if abs(x[i]) < 1.0:
                result += 0.6 * (x[i]**2 - 1)**2
            else:
                result += 0.3 * np.abs(x[i] - np.sign(x[i]) * 1.0)**3
                
        return result