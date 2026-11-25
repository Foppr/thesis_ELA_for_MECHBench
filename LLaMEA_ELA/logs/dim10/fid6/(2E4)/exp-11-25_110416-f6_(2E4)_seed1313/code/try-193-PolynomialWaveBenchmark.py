import numpy as np

class PolynomialWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for adaptive conditioning
        self.chaos_seq = np.array([0.5])
        for _ in range(dim * 150):
            self.chaos_seq = np.append(self.chaos_seq, 4 * self.chaos_seq[-1] * (1 - self.chaos_seq[-1]))
            
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with adaptive conditioning
        result = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 3.0 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 80)
            result += cond_factor * x[i]**11 - 5.0 * x[i]**6
        
        # Add trigonometric wave interference patterns with higher frequency components
        for i in range(self.dim):
            wave_sum = 0.0
            for k in range(1, min(25, self.dim + 1)):
                freq = k * (4.0 + 2.0 * np.cos(self.chaos_seq[(i+k) % len(self.chaos_seq)]))
                wave_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.9)
            result += 4.0 * wave_sum
            
        # Add polynomial chaos components with varying exponents and fractal-like scaling
        for i in range(min(50, self.dim)):
            exp_factor = 8 + 20 * np.sin(self.chaos_seq[(i*19) % len(self.chaos_seq)])
            result += 2.0 * (x[i] ** exp_factor) * np.cos(10.0 * x[i])
            
        # Add cross-dimensional coupling with chaotic interaction strengths and fractal scaling
        for i in range(self.dim):
            for j in range(i+1, min(i+20, self.dim)):
                coupling = 3.0 + 3.0 * np.sin(self.chaos_seq[(i*j) % len(self.chaos_seq)] * 40)
                result += coupling * x[i]**7 * x[j]**7
                
        # Add multi-scale oscillatory components with fractal-like scaling
        for i in range(self.dim):
            osc_sum = 0.0
            for k in range(1, min(30, self.dim + 1)):
                scale = 1.0 / (k**2.5)
                osc_sum += scale * np.sin(k * x[i]) * np.cos(k * x[i] * 0.7)
            result += 2.2 * osc_sum
            
        # Add adaptive noise with chaotic amplitude modulation and fractal scaling
        for i in range(self.dim):
            noise_amp = 1.5 + 1.0 * np.sin(self.chaos_seq[(i*41) % len(self.chaos_seq)] * 120)
            result += noise_amp * np.sin(90 * x[i])
            
        # Add basin boundary regions with varying steepness and fractal-like characteristics
        for i in range(self.dim):
            if abs(x[i]) < 2.5:
                result += 4.0 * (x[i]**2 - 1)**6
            else:
                result += 2.0 * np.abs(x[i] - np.sign(x[i]) * 2.5)**9
                
        # Add fractal-like component with self-similar patterns
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, min(20, self.dim + 1)):
                fractal_sum += (0.8 / k) * np.sin(k**3.5 * x[i]) * np.cos(k**2.8 * x[i])
            result += 2.5 * fractal_sum
            
        # Add enhanced chaotic modulation with higher frequency and complexity
        for i in range(self.dim):
            chaos_mod = 0.8 + 1.5 * np.sin(self.chaos_seq[(i*47) % len(self.chaos_seq)] * 200)
            result += chaos_mod * np.sin(100 * x[i]**2) * np.cos(80 * x[i])
            
        # Add multi-modal sinusoidal components with varying amplitudes and frequencies
        for i in range(self.dim):
            multimodal_sum = 0.0
            for k in range(1, min(20, self.dim + 1)):
                amp = 1.5 + 1.5 * np.sin(self.chaos_seq[(i+k*9) % len(self.chaos_seq)] * 50)
                freq = k * (3.0 + 1.5 * np.cos(self.chaos_seq[(i+k*12) % len(self.chaos_seq)]))
                multimodal_sum += amp * np.sin(freq * x[i]**2) * np.cos(freq * x[i])
            result += 3.2 * multimodal_sum
            
        # Add complex cross-dimensional interactions with exponential coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+15, self.dim)):
                exp_coupling = np.exp(-0.4 * abs(x[i] - x[j]))
                result += 2.5 * exp_coupling * (x[i]**3 + x[j]**3) * np.sin(6 * x[i] * x[j])
                
        # Add enhanced fractal dimensionality with recursive scaling
        for i in range(self.dim):
            recursive_sum = 0.0
            for k in range(1, min(15, self.dim + 1)):
                recursive_sum += (1.0 / k**4.2) * np.sin(k**7 * x[i])
            result += 2.8 * recursive_sum
            
        # Add a new component to improve algorithmic performance
        for i in range(self.dim):
            result += 0.7 * np.sin(12 * x[i]) * np.cos(18 * x[i]) * (1 + 0.15 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 60))
            
        # Add additional cross-dimensional coupling with dynamic strength - modified version
        for i in range(self.dim):
            for j in range(i+1, min(i+12, self.dim)):
                dynamic_strength = 2.5 + 0.8 * np.sin(self.chaos_seq[(i+j*4) % len(self.chaos_seq)] * 50)
                # Modified interaction: changed coupling to x[i]**4 * x[j]**4
                result += dynamic_strength * (x[i]**4) * (x[j]**4) * np.sin(3 * x[i] * x[j])
                
        return result