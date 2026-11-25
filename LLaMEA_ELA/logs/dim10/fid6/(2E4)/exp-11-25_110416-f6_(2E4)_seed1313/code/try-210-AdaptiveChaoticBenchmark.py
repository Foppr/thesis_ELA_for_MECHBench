import numpy as np

class AdaptiveChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate chaotic sequence for dynamic conditioning
        self.chaos_seq = np.array([0.1])
        for _ in range(dim * 50):
            self.chaos_seq = np.append(self.chaos_seq, 3.8 * self.chaos_seq[-1] * (1 - self.chaos_seq[-1]))
            
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Enhanced polynomial base with adaptive conditioning
        for i in range(self.dim):
            cond = 1.0 + 1.5 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 35)
            result += cond * (x[i]**6 - 3*x[i]**4 + 3*x[i]**2 - 1)
            
        # Improved trigonometric interference with adaptive frequencies
        for i in range(self.dim):
            freq = 1.0 + 1.8 * np.cos(self.chaos_seq[(i*7) % len(self.chaos_seq)] * 45)
            result += 1.2 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.6)
            
        # Enhanced chaotic fractal component with recursive scaling
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, min(7, self.dim + 1)):
                scale = 1.0 / (k**2.2)
                fractal_sum += scale * np.sin(k**1.3 * x[i])
            result += 0.9 * fractal_sum
            
        # Strengthened cross-dimensional coupling with adaptive strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling = 1.0 + 2.0 * np.cos(self.chaos_seq[(i*j*3) % len(self.chaos_seq)] * 65)
                result += coupling * x[i]**2 * x[j]**2
                
        # Refined multi-modal sinusoidal components with varying amplitudes
        for i in range(self.dim):
            multimodal_sum = 0.0
            for k in range(1, min(5, self.dim + 1)):
                amp = 0.7 + 1.3 * np.cos(self.chaos_seq[(i+k*4) % len(self.chaos_seq)] * 55)
                freq = k * (1.0 + 0.6 * np.sin(self.chaos_seq[(i+k*8) % len(self.chaos_seq)]))
                multimodal_sum += amp * np.cos(freq * x[i]**2)
            result += 0.9 * multimodal_sum
            
        # Modified basin boundary with enhanced chaotic characteristics
        for i in range(self.dim):
            if abs(x[i]) < 2.0:
                result += 0.5 * (x[i]**2 - 1)**3
            else:
                result += 1.0 * np.abs(x[i] - np.sign(x[i]) * 2.0)**4
                
        # Refined adaptive noise with chaotic modulation
        for i in range(self.dim):
            noise_amp = 0.15 + 0.7 * np.cos(self.chaos_seq[(i*13) % len(self.chaos_seq)] * 85)
            result += noise_amp * np.cos(35 * x[i])
            
        # Improved exponential coupling with dynamic strength
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                exp_coupling = np.exp(-0.25 * abs(x[i] - x[j]))
                result += 0.5 * exp_coupling * (x[i]**2 + x[j]**2)
                
        # Enhanced chaotic dimensionality
        for i in range(self.dim):
            recursive_sum = 0.0
            for k in range(1, min(5, self.dim + 1)):
                recursive_sum += (1.0 / k**2.3) * np.sin(k**1.8 * x[i])
            result += 0.7 * recursive_sum
            
        # Additional enhanced chaotic modulation
        for i in range(self.dim):
            chaos_mod = 0.4 + 1.6 * np.cos(self.chaos_seq[(i*19) % len(self.chaos_seq)] * 75)
            result += chaos_mod * np.sin(25 * x[i]**2)
            
        return result