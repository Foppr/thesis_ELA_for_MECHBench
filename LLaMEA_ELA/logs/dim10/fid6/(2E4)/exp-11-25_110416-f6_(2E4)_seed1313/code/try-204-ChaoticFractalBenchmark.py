import numpy as np

class ChaoticFractalBenchmark:
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
        
        # Polynomial base with chaotic conditioning
        for i in range(self.dim):
            cond = 1.0 + 2.0 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 70)
            result += cond * (x[i]**4 - 2*x[i]**2 + 1)
            
        # Trigonometric interference with dynamic frequencies
        for i in range(self.dim):
            freq = 1.5 + 4.0 * np.sin(self.chaos_seq[(i*7) % len(self.chaos_seq)] * 90)
            result += 1.5 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
            
        # Fractal-like component with modified scaling
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, min(12, self.dim + 1)):
                scale = 1.0 / (k**3.0)
                fractal_sum += scale * np.sin(k**2.2 * x[i])
            result += 2.0 * fractal_sum
            
        # Cross-dimensional coupling with altered strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                coupling = 0.5 + 3.0 * np.sin(self.chaos_seq[(i*j*4) % len(self.chaos_seq)] * 100)
                result += coupling * x[i]**2.5 * x[j]**2.5
                
        # Multi-modal sinusoidal components with varying amplitudes
        for i in range(self.dim):
            multimodal_sum = 0.0
            for k in range(1, min(10, self.dim + 1)):
                amp = 0.3 + 2.0 * np.sin(self.chaos_seq[(i+k*4) % len(self.chaos_seq)] * 80)
                freq = k * (2.0 + 0.3 * np.cos(self.chaos_seq[(i+k*9) % len(self.chaos_seq)]))
                multimodal_sum += amp * np.sin(freq * x[i]**1.5)
            result += 1.0 * multimodal_sum
            
        # Basin boundary with modified fractal characteristics
        for i in range(self.dim):
            if abs(x[i]) < 2.5:
                result += 1.0 * (x[i]**2 - 2)**4
            else:
                result += 2.0 * np.abs(x[i] - np.sign(x[i]) * 2.5)**7
                
        # Adaptive noise with altered modulation
        for i in range(self.dim):
            noise_amp = 0.2 + 0.8 * np.sin(self.chaos_seq[(i*11) % len(self.chaos_seq)] * 130)
            result += noise_amp * np.sin(60 * x[i])
            
        # Exponential coupling with modified strength
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                exp_coupling = np.exp(-0.3 * abs(x[i] - x[j]))
                result += 1.2 * exp_coupling * (x[i]**2 + x[j]**2)
                
        # Enhanced fractal dimensionality
        for i in range(self.dim):
            recursive_sum = 0.0
            for k in range(1, min(8, self.dim + 1)):
                recursive_sum += (1.0 / k**3.5) * np.cos(k**2.7 * x[i])
            result += 1.5 * recursive_sum
            
        # Additional chaotic modulation
        for i in range(self.dim):
            chaos_mod = 0.4 + 1.6 * np.sin(self.chaos_seq[(i*17) % len(self.chaos_seq)] * 110)
            result += chaos_mod * np.cos(50 * x[i]**2)
            
        return result