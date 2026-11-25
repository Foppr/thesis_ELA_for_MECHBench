import numpy as np

class TrigonometricWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with adaptive conditioning
        f1 = 0.0
        for i in range(self.dim):
            cond = 1.0 + 0.2 * np.sin(0.5 * i)
            f1 += cond * (x[i]**4 - 2.0 * x[i]**2 + 0.3 * x[i])
            
        # Trigonometric wave interference pattern
        f2 = 0.0
        for i in range(self.dim):
            wave = 0.0
            for k in range(1, 7):
                wave += np.sin(k * x[i]) * np.cos(k * x[i] / 2.0)
            f2 += wave * np.exp(-0.1 * x[i]**2)
            
        # Cross-dimensional interference with frequency modulation
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_mod = 1.0 + 0.4 * np.sin(0.2 * (i + j))
                coupling = 0.15 + 0.7 * np.cos(0.25 * i) * np.sin(0.25 * j)
                f3 += coupling * np.sin(freq_mod * (x[i] + x[j])) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Radial harmonic potential with amplitude modulation
        r = np.sqrt(np.sum(x**2))
        f4 = 0.0
        for k in range(1, 7):
            amp = 1.0 + 0.25 * np.sin(0.6 * k)
            f4 += amp * np.cos(k * r) * np.exp(-0.015 * r**2)
            
        # Asymmetric boundary attraction with logarithmic scaling
        f5 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                f5 -= 1.2 * np.log(1.0 - x[i]/5.0) * np.exp(-0.03 * x[i]**2)
            else:
                f5 -= 1.2 * np.log(1.0 + x[i]/5.0) * np.exp(-0.03 * x[i]**2)
                
        # Saddle-point inducing cross-terms with adaptive weights
        f6 = 0.0
        for i in range(self.dim):
            weight = 0.4 + 0.4 * np.sin(0.25 * i)
            for j in range(i+1, self.dim):
                f6 += weight * (x[i]**2 - x[j]**2) * np.exp(-0.025 * (x[i]**2 + x[j]**2))
                
        # High-frequency oscillatory component
        f7 = 0.0
        for i in range(self.dim):
            freq = 6.0 + 2.0 * np.sin(0.15 * i)
            amp = 1.0 + 0.35 * np.cos(0.25 * i)
            f7 += amp * np.sin(freq * x[i]) * np.exp(-0.008 * np.abs(x[i]))
            
        # Chaotic radial component with fractal-like scaling
        f8 = 0.0
        for i in range(self.dim):
            r_i = np.abs(x[i])
            f8 += (1.0 + 0.15 * np.sin(12.0 * r_i)) * np.exp(-0.4 * r_i**2) * np.cos(2.5 * r_i)
            
        # Enhanced cross-dimensional coupling with chaotic modulation
        f9 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_mod = 1.0 + 0.25 * np.sin(2.5 * i * j)
                coupling = 0.08 * np.cos(0.4 * (i + j)) * np.exp(-0.09 * (x[i]**2 + x[j]**2))
                f9 += coupling * np.sin(chaos_mod * (x[i]**2 + x[j]**2)) * np.exp(-0.015 * (x[i]**2 + x[j]**2))
                
        # Multi-scale harmonic interference with adaptive frequencies
        f10 = 0.0
        for k in range(1, 9):
            freq_k = 2.5 + 1.2 * np.sin(0.12 * k)
            amp_k = 0.45 + 0.45 * np.cos(0.22 * k)
            f10 += amp_k * np.sin(freq_k * r) * np.exp(-0.025 * r**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10