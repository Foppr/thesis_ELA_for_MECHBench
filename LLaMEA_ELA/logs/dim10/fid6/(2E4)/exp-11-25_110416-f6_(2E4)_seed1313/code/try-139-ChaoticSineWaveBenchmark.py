import numpy as np

class ChaoticSineWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic modulation
        self.chaos_seq = np.array([0.1])
        for _ in range(dim * 50):
            self.chaos_seq = np.append(self.chaos_seq, 3.8 * self.chaos_seq[-1] * (1 - self.chaos_seq[-1]))
            
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic sine-wave component
        result = 0.0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 10)
            amp = 1.5 + 0.5 * np.cos(self.chaos_seq[(i+10) % len(self.chaos_seq)] * 7)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
            
        # Add adaptive polynomial conditioning
        for i in range(self.dim):
            poly_exp = 2 + 2 * np.sin(self.chaos_seq[(i*5) % len(self.chaos_seq)] * 5)
            result += 0.8 * (x[i]**poly_exp) * np.sin(3 * x[i])
            
        # Add dynamic cross-dimensional coupling
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(i+1, min(i+5, self.dim)):
                strength = 1.2 + 0.8 * np.sin(self.chaos_seq[(i*j*3) % len(self.chaos_seq)] * 8)
                coupling_sum += strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
            result += 0.5 * coupling_sum
            
        # Add multi-scale chaotic oscillations
        for i in range(self.dim):
            osc_sum = 0.0
            for k in range(1, min(7, self.dim + 1)):
                scale_factor = 1.0 / (k**1.5)
                freq_mod = 1 + 0.3 * np.sin(self.chaos_seq[(i+k*2) % len(self.chaos_seq)] * 4)
                osc_sum += scale_factor * np.sin(freq_mod * k * x[i]) * np.cos(freq_mod * k * x[i] * 0.5)
            result += 0.6 * osc_sum
            
        # Add chaotic ridge structures
        for i in range(self.dim):
            ridge_amp = 0.5 + 0.5 * np.sin(self.chaos_seq[(i*8) % len(self.chaos_seq)] * 12)
            result += ridge_amp * np.exp(-0.3 * x[i]**2) * np.sin(4 * x[i])
            
        # Add basin boundary effects
        for i in range(self.dim):
            if abs(x[i]) < 1.0:
                result += 0.7 * (x[i]**2 - 1)**4
            else:
                result += 0.4 * np.abs(x[i] - np.sign(x[i]) * 1.0)**5
                
        # Add fractal-like harmonic components
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, min(6, self.dim + 1)):
                freq_factor = k**1.3
                fractal_sum += (0.2 / k) * np.sin(freq_factor * x[i]) * np.cos(freq_factor * x[i] * 0.7)
            result += 0.5 * fractal_sum
            
        # Add chaotic noise modulation
        for i in range(self.dim):
            noise_freq = 10 + 5 * np.sin(self.chaos_seq[(i*13) % len(self.chaos_seq)] * 15)
            result += 0.3 * np.sin(noise_freq * x[i]) * np.cos(noise_freq * x[i] * 0.2)
            
        return result