import numpy as np

class PolynomialWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for adaptive conditioning
        self.chaos_seq = np.array([0.5])
        for _ in range(dim * 100):
            self.chaos_seq = np.append(self.chaos_seq, 4 * self.chaos_seq[-1] * (1 - self.chaos_seq[-1]))
            
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with adaptive conditioning
        result = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 2.0 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 70)
            result += cond_factor * x[i]**9 - 4.0 * x[i]**5
        
        # Add trigonometric wave interference patterns with higher frequency components
        for i in range(self.dim):
            wave_sum = 0.0
            for k in range(1, min(20, self.dim + 1)):
                freq = k * (3.0 + 1.5 * np.cos(self.chaos_seq[(i+k) % len(self.chaos_seq)]))
                wave_sum += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8)
            result += 3.0 * wave_sum
            
        # Add polynomial chaos components with varying exponents and fractal-like scaling
        for i in range(min(40, self.dim)):
            exp_factor = 7 + 15 * np.sin(self.chaos_seq[(i*17) % len(self.chaos_seq)])
            result += 1.5 * (x[i] ** exp_factor) * np.cos(8.0 * x[i])
            
        # Add cross-dimensional coupling with chaotic interaction strengths and fractal scaling
        for i in range(self.dim):
            for j in range(i+1, min(i+15, self.dim)):
                coupling = 3.0 + 2.0 * np.sin(self.chaos_seq[(i*j) % len(self.chaos_seq)] * 35)
                result += coupling * x[i]**6 * x[j]**6
                
        # Add multi-scale oscillatory components with fractal-like scaling
        for i in range(self.dim):
            osc_sum = 0.0
            for k in range(1, min(25, self.dim + 1)):
                scale = 1.0 / (k**3.2)
                osc_sum += scale * np.sin(k * x[i]) * np.cos(k * x[i] * 0.6)
            result += 1.8 * osc_sum
            
        # Add adaptive noise with chaotic amplitude modulation and fractal scaling
        for i in range(self.dim):
            noise_amp = 1.2 + 0.8 * np.sin(self.chaos_seq[(i*37) % len(self.chaos_seq)] * 110)
            result += noise_amp * np.sin(80 * x[i])
            
        # Add basin boundary regions with varying steepness and fractal-like characteristics
        for i in range(self.dim):
            if abs(x[i]) < 2.0:
                result += 3.0 * (x[i]**2 - 1)**5
            else:
                result += 1.5 * np.abs(x[i] - np.sign(x[i]) * 2.0)**8
                
        # Add fractal-like component with self-similar patterns
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, min(15, self.dim + 1)):
                fractal_sum += (0.9 / k) * np.sin(k**3.2 * x[i]) * np.cos(k**3.0 * x[i])
            result += 2.0 * fractal_sum
            
        # Add enhanced chaotic modulation with higher frequency and complexity
        for i in range(self.dim):
            chaos_mod = 0.7 + 1.3 * np.sin(self.chaos_seq[(i*41) % len(self.chaos_seq)] * 180)
            result += chaos_mod * np.sin(90 * x[i]**2) * np.cos(70 * x[i])
            
        # Add multi-modal sinusoidal components with varying amplitudes and frequencies
        for i in range(self.dim):
            multimodal_sum = 0.0
            for k in range(1, min(15, self.dim + 1)):
                amp = 1.2 + 1.0 * np.sin(self.chaos_seq[(i+k*7) % len(self.chaos_seq)] * 40)
                freq = k * (2.8 + 1.2 * np.cos(self.chaos_seq[(i+k*10) % len(self.chaos_seq)]))
                multimodal_sum += amp * np.sin(freq * x[i]**2) * np.cos(freq * x[i])
            result += 2.8 * multimodal_sum
            
        # Add complex cross-dimensional interactions with exponential coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+12, self.dim)):
                exp_coupling = np.exp(-0.3 * abs(x[i] - x[j]))
                result += 2.0 * exp_coupling * (x[i]**2 + x[j]**2) * np.sin(5 * x[i] * x[j])
                
        # Add enhanced fractal dimensionality with recursive scaling
        for i in range(self.dim):
            recursive_sum = 0.0
            for k in range(1, min(12, self.dim + 1)):
                recursive_sum += (1.0 / k**3.8) * np.sin(k**6 * x[i])
            result += 2.2 * recursive_sum
            
        # Add a new component to improve algorithmic performance
        for i in range(self.dim):
            result += 0.5 * np.sin(10 * x[i]) * np.cos(15 * x[i]) * (1 + 0.1 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 50))
            
        # Add additional cross-dimensional coupling with dynamic strength
        for i in range(self.dim):
            for j in range(i+1, min(i+10, self.dim)):
                dynamic_strength = 2.0 + np.sin(self.chaos_seq[(i+j*3) % len(self.chaos_seq)] * 45)
                result += dynamic_strength * np.sin(x[i] * x[j]) * (x[i]**2 + x[j]**2)
                
        # Add new chaotic modulation with enhanced complexity and multi-scale interference
        for i in range(self.dim):
            chaos_mod = 1.0 + 1.5 * np.sin(self.chaos_seq[(i*53) % len(self.chaos_seq)] * 200)
            result += chaos_mod * np.sin(110 * x[i]**3) * np.cos(90 * x[i]**2)
            
        # Add higher-order polynomial coupling with exponential scaling
        for i in range(self.dim):
            for j in range(i+1, min(i+8, self.dim)):
                poly_coupling = 1.5 + 0.5 * np.sin(self.chaos_seq[(i*j*2) % len(self.chaos_seq)] * 60)
                result += poly_coupling * x[i]**7 * x[j]**5
                
        # Add a new multi-scale fractal component with recursive exponential decay
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, min(20, self.dim + 1)):
                fractal_sum += (1.0 / k**4.5) * np.sin(k**4.0 * x[i]) * np.cos(k**3.5 * x[i])
            result += 1.7 * fractal_sum
            
        # Add a new sinusoidal interference pattern with dynamic phase modulation
        for i in range(self.dim):
            phase_mod = 1.0 + 0.8 * np.sin(self.chaos_seq[(i*67) % len(self.chaos_seq)] * 150)
            result += 2.3 * np.sin(60 * x[i]) * np.cos(phase_mod * x[i])
            
        # Add enhanced basin boundary with exponential steepness
        for i in range(self.dim):
            if abs(x[i]) < 1.5:
                result += 4.0 * (x[i]**2 - 0.5)**7
            else:
                result += 2.0 * np.abs(x[i] - np.sign(x[i]) * 1.5)**10
                
        return result