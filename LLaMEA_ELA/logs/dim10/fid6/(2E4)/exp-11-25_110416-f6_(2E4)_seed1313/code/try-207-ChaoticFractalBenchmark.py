import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate chaotic sequence for dynamic conditioning
        self.chaos_seq = np.array([0.1])
        for _ in range(dim * 100):
            self.chaos_seq = np.append(self.chaos_seq, 3.9 * self.chaos_seq[-1] * (1 - self.chaos_seq[-1]))
            
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Enhanced polynomial base with chaotic conditioning
        for i in range(self.dim):
            cond = 1.0 + 2.0 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 80)
            result += cond * (x[i]**6 - 3*x[i]**4 + 3*x[i]**2 - 1)
            
        # Multi-frequency trigonometric interference
        for i in range(self.dim):
            freq1 = 1.5 + 4.0 * np.sin(self.chaos_seq[(i*7) % len(self.chaos_seq)] * 100)
            freq2 = 2.0 + 2.5 * np.cos(self.chaos_seq[(i*11) % len(self.chaos_seq)] * 90)
            result += 3.0 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i] * 0.3)
            
        # Fractal-like component with recursive scaling and chaos modulation
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, min(15, self.dim + 1)):
                scale = 1.0 / (k**3.0)
                chaos_factor = 0.5 + 1.5 * np.sin(self.chaos_seq[(i*k*2) % len(self.chaos_seq)] * 120)
                fractal_sum += scale * np.sin(k**2.0 * x[i]) * chaos_factor
            result += 2.0 * fractal_sum
            
        # Cross-dimensional coupling with chaotic strengths and exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+10, self.dim)):
                coupling = 1.5 + 3.0 * np.sin(self.chaos_seq[(i*j*5) % len(self.chaos_seq)] * 110)
                exp_decay = np.exp(-0.3 * abs(x[i] - x[j]))
                result += coupling * exp_decay * (x[i]**4 + x[j]**4)
                
        # Multi-modal sinusoidal components with varying amplitudes and frequencies
        for i in range(self.dim):
            multimodal_sum = 0.0
            for k in range(1, min(12, self.dim + 1)):
                amp = 0.3 + 2.0 * np.sin(self.chaos_seq[(i+k*7) % len(self.chaos_seq)] * 95)
                freq = k * (2.0 + 0.8 * np.cos(self.chaos_seq[(i+k*13) % len(self.chaos_seq)]))
                multimodal_sum += amp * np.sin(freq * x[i]**3)
            result += 1.8 * multimodal_sum
            
        # Enhanced basin boundary with fractal characteristics and chaotic modulation
        for i in range(self.dim):
            if abs(x[i]) < 2.5:
                result += 1.2 * (x[i]**2 - 3)**6
            else:
                chaos_mod = 0.8 + 1.2 * np.sin(self.chaos_seq[(i*17) % len(self.chaos_seq)] * 130)
                result += 2.0 * chaos_mod * np.abs(x[i] - np.sign(x[i]) * 2.5)**8
                
        # Adaptive noise with chaotic modulation and multiple frequency components
        for i in range(self.dim):
            noise_amp = 0.2 + 0.8 * np.sin(self.chaos_seq[(i*13) % len(self.chaos_seq)] * 140)
            result += noise_amp * (np.sin(60 * x[i]) + 0.5 * np.sin(120 * x[i]))
            
        # Exponential coupling with dynamic strength and chaos modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+8, self.dim)):
                exp_coupling = np.exp(-0.7 * abs(x[i] - x[j]))
                chaos_mod = 1.0 + 2.0 * np.sin(self.chaos_seq[(i+j*3) % len(self.chaos_seq)] * 150)
                result += 1.2 * exp_coupling * chaos_mod * (x[i]**3 + x[j]**3)
                
        # Enhanced fractal dimensionality with multiple recursive components
        for i in range(self.dim):
            recursive_sum = 0.0
            for k in range(1, min(10, self.dim + 1)):
                recursive_sum += (1.0 / k**3.5) * np.cos(k**2.8 * x[i])
            result += 1.5 * recursive_sum
            
        # Additional chaotic modulation with higher frequency components
        for i in range(self.dim):
            chaos_mod = 0.4 + 1.6 * np.sin(self.chaos_seq[(i*23) % len(self.chaos_seq)] * 160)
            result += chaos_mod * np.cos(50 * x[i]**3)
            
        # Additional high-frequency oscillation component
        for i in range(self.dim):
            result += 0.5 * np.sin(100 * x[i]) * np.cos(80 * x[i])
            
        return result