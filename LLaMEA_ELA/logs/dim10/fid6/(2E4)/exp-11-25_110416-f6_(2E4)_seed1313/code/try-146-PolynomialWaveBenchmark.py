import numpy as np

class PolynomialWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for adaptive conditioning
        self.chaos_seq = np.array([0.5])
        for _ in range(dim * 30):
            self.chaos_seq = np.append(self.chaos_seq, 4 * self.chaos_seq[-1] * (1 - self.chaos_seq[-1]))
            
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with adaptive conditioning
        result = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.9 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 30)
            result += cond_factor * x[i]**5 - 2.5 * x[i]**3
        
        # Add trigonometric wave interference patterns with higher frequency components
        for i in range(self.dim):
            wave_sum = 0.0
            for k in range(1, min(9, self.dim + 1)):
                freq = k * (1.2 + 0.6 * np.cos(self.chaos_seq[(i+k) % len(self.chaos_seq)]))
                wave_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
            result += 1.5 * wave_sum
            
        # Add polynomial chaos components with varying exponents and fractal-like scaling
        for i in range(min(20, self.dim)):
            exp_factor = 3 + 6 * np.sin(self.chaos_seq[(i*9) % len(self.chaos_seq)])
            result += 0.6 * (x[i] ** exp_factor) * np.cos(4.0 * x[i])
            
        # Add cross-dimensional coupling with chaotic interaction strengths and fractal scaling
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):
                coupling = 1.2 + 0.8 * np.sin(self.chaos_seq[(i*j) % len(self.chaos_seq)] * 15)
                result += coupling * x[i]**3 * x[j]**3
                
        # Add multi-scale oscillatory components with fractal-like scaling
        for i in range(self.dim):
            osc_sum = 0.0
            for k in range(1, min(12, self.dim + 1)):
                scale = 1.0 / (k**2.1)
                osc_sum += scale * np.sin(k * x[i]) * np.cos(k * x[i] * 0.5)
            result += 0.7 * osc_sum
            
        # Add adaptive noise with chaotic amplitude modulation and fractal scaling
        for i in range(self.dim):
            noise_amp = 0.4 + 0.3 * np.sin(self.chaos_seq[(i*17) % len(self.chaos_seq)] * 65)
            result += noise_amp * np.sin(40 * x[i])
            
        # Add basin boundary regions with varying steepness and fractal-like characteristics
        for i in range(self.dim):
            if abs(x[i]) < 1.5:
                result += 1.0 * (x[i]**2 - 1)**3
            else:
                result += 0.6 * np.abs(x[i] - np.sign(x[i]) * 1.5)**4
                
        # Add fractal-like component with self-similar patterns
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, min(6, self.dim + 1)):
                fractal_sum += (0.5 / k) * np.sin(k**2 * x[i]) * np.cos(k**1.5 * x[i])
            result += 0.8 * fractal_sum
            
        # Add small mutation: increased complexity in cross-dimensional couplings and altered noise characteristics
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling = 1.5 + 0.7 * np.sin(self.chaos_seq[(i*j*2) % len(self.chaos_seq)] * 20)
                result += coupling * x[i]**4 * x[j]**2
                
        # Slightly modified noise with different frequency and amplitude
        for i in range(self.dim):
            noise_amp = 0.3 + 0.25 * np.sin(self.chaos_seq[(i*19) % len(self.chaos_seq)] * 70)
            result += noise_amp * np.sin(45 * x[i])
            
        return result