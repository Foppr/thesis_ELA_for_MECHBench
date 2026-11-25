import numpy as np

class FractalWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like sequence for conditioning
        self.frac_seq = np.array([0.1])
        for _ in range(dim * 50):
            self.frac_seq = np.append(self.frac_seq, 0.5 + 0.5 * np.sin(self.frac_seq[-1] * 7))
            
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base exponential decay with fractal conditioning
        result = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.8 * np.sin(self.frac_seq[i % len(self.frac_seq)] * 20)
            result += cond_factor * np.exp(-0.5 * x[i]**2) * (x[i]**4 - 2*x[i]**2 + 1)
            
        # Add trigonometric wave interference with varying frequencies and amplitudes
        for i in range(self.dim):
            wave_sum = 0.0
            for k in range(1, min(8, self.dim + 1)):
                freq = k * (1.0 + 0.3 * np.cos(self.frac_seq[(i+k) % len(self.frac_seq)] * 15))
                amp = 1.0 + 0.5 * np.sin(self.frac_seq[(i+k*2) % len(self.frac_seq)] * 10)
                wave_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8)
            result += 1.2 * wave_sum
            
        # Add fractal-based polynomial interactions
        for i in range(min(15, self.dim)):
            exp_factor = 2 + 4 * np.sin(self.frac_seq[(i*7) % len(self.frac_seq)] * 25)
            result += 0.7 * (x[i]**exp_factor) * np.cos(3.0 * x[i])
            
        # Add cross-dimensional coupling with fractal scaling
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                scale = 1.0 / (1 + np.exp(-0.5 * (x[i] - x[j])**2))
                result += scale * x[i]**2 * x[j]**2
                
        # Add nested multi-modal components with varying depths
        for i in range(self.dim):
            nested_sum = 0.0
            for k in range(1, min(6, self.dim + 1)):
                depth = 1.0 / (k**1.8)
                nested_sum += depth * np.sin(k * x[i])**2 * np.cos(k * x[i] * 0.3)
            result += 0.9 * nested_sum
            
        # Add chaotic modulation with recursive scaling
        for i in range(self.dim):
            chaos_mod = 0.4 + 0.6 * np.sin(self.frac_seq[(i*13) % len(self.frac_seq)] * 50)
            result += chaos_mod * np.sin(30 * x[i]) * np.cos(20 * x[i]**2)
            
        # Add boundary attraction with fractal-like scaling
        for i in range(self.dim):
            if abs(x[i]) < 2.0:
                result += 0.5 * (x[i]**2 - 4)**2
            else:
                result += 0.3 * np.abs(x[i] - np.sign(x[i]) * 2.0)**3
                
        # Add self-similar oscillatory components with recursive frequency scaling
        for i in range(self.dim):
            osc_sum = 0.0
            for k in range(1, min(10, self.dim + 1)):
                freq = k * (1.0 + 0.2 * np.sin(self.frac_seq[(i+k*4) % len(self.frac_seq)] * 30))
                osc_sum += (1.0 / k**1.5) * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.6)
            result += 1.0 * osc_sum
            
        return result