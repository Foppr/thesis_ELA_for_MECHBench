import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for adaptive conditioning
        self.chaos_seq = np.array([0.5])
        for _ in range(dim * 50):
            self.chaos_seq = np.append(self.chaos_seq, 4 * self.chaos_seq[-1] * (1 - self.chaos_seq[-1]))
            
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial chaos with varying exponents
        result = 0.0
        for i in range(self.dim):
            exp_factor = 2 + 3 * np.sin(self.chaos_seq[i % len(self.chaos_seq)] * 50)
            result += x[i]**exp_factor
            
        # Add trigonometric interference patterns with adaptive frequencies
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.cos(self.chaos_seq[(i*7) % len(self.chaos_seq)] * 30)
            result += 2.0 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Add radial basis function components with chaotic centers and widths
        for i in range(min(20, self.dim)):
            center = 5.0 * np.sin(self.chaos_seq[(i*13) % len(self.chaos_seq)] * 80)
            width = 0.5 + 1.5 * np.cos(self.chaos_seq[(i*23) % len(self.chaos_seq)] * 60)
            result += np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Add cross-dimensional coupling with chaotic interaction strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+8, self.dim)):
                coupling = 1.0 + 1.5 * np.sin(self.chaos_seq[(i*j*3) % len(self.chaos_seq)] * 40)
                result += coupling * (x[i] - x[j])**4
                
        # Add fractal-like scaling with recursive polynomial components
        for i in range(self.dim):
            fractal_sum = 0.0
            for k in range(1, min(10, self.dim + 1)):
                scale = 1.0 / (k**2.5)
                fractal_sum += scale * np.sin(k**2.0 * x[i]) * np.cos(k**1.8 * x[i])
            result += 1.5 * fractal_sum
            
        # Add chaotic noise with varying amplitude and frequency
        for i in range(self.dim):
            amp = 0.8 + 1.2 * np.sin(self.chaos_seq[(i*17) % len(self.chaos_seq)] * 90)
            freq = 3.0 + 4.0 * np.cos(self.chaos_seq[(i*29) % len(self.chaos_seq)] * 70)
            result += amp * np.sin(freq * x[i]**3)
            
        # Add basin boundary effects with varying steepness
        for i in range(self.dim):
            if abs(x[i]) < 1.5:
                result += 2.5 * (x[i]**2 - 0.5)**4
            else:
                result += 1.8 * np.abs(x[i] - np.sign(x[i]) * 1.5)**6
                
        # Add multi-scale oscillatory components with exponential decay
        for i in range(self.dim):
            osc_sum = 0.0
            for k in range(1, min(15, self.dim + 1)):
                scale = 1.0 / (k**2.8)
                osc_sum += scale * np.sin(k * x[i]) * np.cos(k * x[i] * 0.7)
            result += 2.0 * osc_sum
            
        # Add enhanced chaotic modulation with exponential coupling
        for i in range(self.dim):
            chaos_mod = 1.0 + 2.0 * np.sin(self.chaos_seq[(i*31) % len(self.chaos_seq)] * 120)
            result += chaos_mod * np.exp(-0.5 * x[i]**2) * np.sin(10 * x[i])
            
        return result