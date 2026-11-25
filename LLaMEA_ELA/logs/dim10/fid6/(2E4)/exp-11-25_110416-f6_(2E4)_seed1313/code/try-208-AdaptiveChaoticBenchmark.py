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
        
        # Polynomial base with adaptive conditioning
        for i in range(self.dim):
            cond = 1.0 + 2.0 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 40)
            result += cond * (x[i]**6 - 3*x[i]**4 + 3*x[i]**2 - 1)
            
        # Trigonometric interference with adaptive frequencies
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.cos(self.chaos_seq[(i*5) % len(self.chaos_seq)] * 50)
            result += 1.5 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
            
        # Chaotic fractal component with recursive scaling
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, min(8, self.dim + 1)):
                scale = 1.0 / (k**2.0)
                fractal_sum += scale * np.sin(k**1.5 * x[i])
            result += 1.0 * fractal_sum
            
        # Cross-dimensional coupling with adaptive strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                coupling = 1.0 + 1.5 * np.cos(self.chaos_seq[(i*j*2) % len(self.chaos_seq)] * 70)
                result += coupling * x[i]**2 * x[j]**2
                
        # Multi-modal sinusoidal components with varying amplitudes
        for i in range(self.dim):
            multimodal_sum = 0.0
            for k in range(1, min(6, self.dim + 1)):
                amp = 0.8 + 1.2 * np.cos(self.chaos_seq[(i+k*3) % len(self.chaos_seq)] * 60)
                freq = k * (1.0 + 0.5 * np.sin(self.chaos_seq[(i+k*7) % len(self.chaos_seq)]))
                multimodal_sum += amp * np.cos(freq * x[i]**2)
            result += 1.0 * multimodal_sum
            
        # Enhanced basin boundary with chaotic characteristics
        for i in range(self.dim):
            if abs(x[i]) < 2.5:
                result += 0.6 * (x[i]**2 - 1)**3
            else:
                result += 1.2 * np.abs(x[i] - np.sign(x[i]) * 2.5)**5
                
        # Adaptive noise with chaotic modulation
        for i in range(self.dim):
            noise_amp = 0.2 + 0.8 * np.cos(self.chaos_seq[(i*11) % len(self.chaos_seq)] * 90)
            result += noise_amp * np.cos(40 * x[i])
            
        # Exponential coupling with dynamic strength
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                exp_coupling = np.exp(-0.3 * abs(x[i] - x[j]))
                result += 0.6 * exp_coupling * (x[i]**2 + x[j]**2)
                
        # Enhanced chaotic dimensionality
        for i in range(self.dim):
            recursive_sum = 0.0
            for k in range(1, min(6, self.dim + 1)):
                recursive_sum += (1.0 / k**2.5) * np.sin(k**2.0 * x[i])
            result += 0.8 * recursive_sum
            
        # Additional chaotic modulation with enhanced complexity
        for i in range(self.dim):
            chaos_mod = 0.5 + 1.5 * np.cos(self.chaos_seq[(i*17) % len(self.chaos_seq)] * 80)
            result += chaos_mod * np.sin(30 * x[i]**2)
            
        # Additional hyper-chaotic component for increased complexity
        for i in range(self.dim):
            hyper_chaos = 0.3 + 0.7 * np.sin(self.chaos_seq[(i*13) % len(self.chaos_seq)] * 100)
            result += hyper_chaos * np.cos(50 * x[i]**3)
            
        # Enhanced multi-modal structure with additional sinusoidal components
        for i in range(self.dim):
            extra_modal = 0.0
            for k in range(1, min(5, self.dim + 1)):
                amp = 0.5 + 1.0 * np.cos(self.chaos_seq[(i+k*4) % len(self.chaos_seq)] * 70)
                freq = k * (1.0 + 0.3 * np.sin(self.chaos_seq[(i+k*9) % len(self.chaos_seq)]))
                extra_modal += amp * np.sin(freq * x[i]**3)
            result += 0.5 * extra_modal
            
        return result