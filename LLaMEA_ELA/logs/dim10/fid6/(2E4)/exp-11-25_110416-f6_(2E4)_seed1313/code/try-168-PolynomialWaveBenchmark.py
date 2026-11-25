import numpy as np

class PolynomialWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for adaptive conditioning
        self.chaos_seq = np.array([0.5])
        for _ in range(dim * 70):
            self.chaos_seq = np.append(self.chaos_seq, 4 * self.chaos_seq[-1] * (1 - self.chaos_seq[-1]))
            
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with adaptive conditioning
        result = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 1.5 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 50)
            result += cond_factor * x[i]**7 - 3.5 * x[i]**4
        
        # Add trigonometric wave interference patterns with higher frequency components
        for i in range(self.dim):
            wave_sum = 0.0
            for k in range(1, min(15, self.dim + 1)):
                freq = k * (2.0 + 1.2 * np.cos(self.chaos_seq[(i+k) % len(self.chaos_seq)]))
                wave_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.9)
            result += 2.5 * wave_sum
            
        # Add polynomial chaos components with varying exponents and fractal-like scaling
        for i in range(min(30, self.dim)):
            exp_factor = 5 + 10 * np.sin(self.chaos_seq[(i*13) % len(self.chaos_seq)])
            result += 1.0 * (x[i] ** exp_factor) * np.cos(6.0 * x[i])
            
        # Add cross-dimensional coupling with chaotic interaction strengths and fractal scaling
        for i in range(self.dim):
            for j in range(i+1, min(i+12, self.dim)):
                coupling = 2.5 + 2.0 * np.sin(self.chaos_seq[(i*j) % len(self.chaos_seq)] * 25)  # Increased coupling
                result += coupling * x[i]**5 * x[j]**5
                
        # Add multi-scale oscillatory components with fractal-like scaling
        for i in range(self.dim):
            osc_sum = 0.0
            for k in range(1, min(18, self.dim + 1)):
                scale = 1.0 / (k**2.8)
                osc_sum += scale * np.sin(k * x[i]) * np.cos(k * x[i] * 0.7)
            result += 1.2 * osc_sum
            
        # Add adaptive noise with chaotic amplitude modulation and fractal scaling
        for i in range(self.dim):
            noise_amp = 0.8 + 0.6 * np.sin(self.chaos_seq[(i*29) % len(self.chaos_seq)] * 90)
            result += noise_amp * np.sin(60 * x[i])
            
        # Add basin boundary regions with varying steepness and fractal-like characteristics
        for i in range(self.dim):
            if abs(x[i]) < 2.5:
                result += 2.5 * (x[i]**2 - 1)**4  # Increased basin depth
            else:
                result += 1.0 * np.abs(x[i] - np.sign(x[i]) * 2.5)**6
                
        # Add fractal-like component with self-similar patterns
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, min(10, self.dim + 1)):
                fractal_sum += (0.7 / k) * np.sin(k**2.8 * x[i]) * np.cos(k**2.5 * x[i])
            result += 1.3 * fractal_sum
            
        # Add enhanced chaotic modulation with higher frequency and complexity
        for i in range(self.dim):
            chaos_mod = 0.6 + 1.2 * np.sin(self.chaos_seq[(i*37) % len(self.chaos_seq)] * 140)  # Increased modulation
            result += chaos_mod * np.sin(70 * x[i]**2) * np.cos(50 * x[i])
            
        # Add multi-modal sinusoidal components with varying amplitudes and frequencies
        for i in range(self.dim):
            multimodal_sum = 0.0
            for k in range(1, min(12, self.dim + 1)):
                amp = 0.9 + 0.8 * np.sin(self.chaos_seq[(i+k*5) % len(self.chaos_seq)] * 30)
                freq = k * (2.3 + 1.0 * np.cos(self.chaos_seq[(i+k*8) % len(self.chaos_seq)]))
                multimodal_sum += amp * np.sin(freq * x[i]**2) * np.cos(freq * x[i])
            result += 2.2 * multimodal_sum  # Increased amplitude
            
        # Add complex cross-dimensional interactions with exponential coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+9, self.dim)):
                exp_coupling = np.exp(-0.25 * abs(x[i] - x[j]))  # Slightly stronger coupling
                result += 1.6 * exp_coupling * (x[i]**2 + x[j]**2) * np.sin(4 * x[i] * x[j])
                
        # Add enhanced fractal dimensionality with recursive scaling
        for i in range(self.dim):
            recursive_sum = 0.0
            for k in range(1, min(9, self.dim + 1)):
                recursive_sum += (1.0 / k**3.2) * np.sin(k**5 * x[i])
            result += 1.4 * recursive_sum
            
        # Add a new sinusoidal modulation to increase basin complexity
        for i in range(self.dim):
            result += 0.8 * np.sin(100 * x[i]**3)  # New term added
            
        return result