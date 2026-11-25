import numpy as np

class TrigonometricRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic trigonometric oscillation terms with dynamic frequencies and amplitudes
        f1 = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.7 * i + 1.5)
            amp = 1.5 + 1.2 * np.cos(0.4 * i + 0.8)
            f1 += amp * np.sin(freq * x[i]) * np.exp(-0.03 * x[i]**2)
            
        # Radial saddle point conditioning with exponential decay
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            cond = 1.0 + 0.8 * np.sin(0.5 * i + 1.2)
            f2 += cond * x[i]**2 * np.exp(-0.04 * r**2)
            
        # Cross-dimensional quintic coupling with dynamic phase shifts
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = 0.8 * np.sin(0.5 * (i + j) + 0.9)
                weight = 1.0 + 0.6 * np.cos(0.3 * (i - j) + 1.1)
                f3 += weight * x[i]**5 * x[j] * np.exp(-0.02 * (x[i]**2 + x[j]**2)) * np.sin(phase_shift)
                
        # Multi-scale harmonic interference with boundary effects
        f4 = 0.0
        for i in range(self.dim):
            if x[i] < -4.5:
                f4 += 3.0 * np.cos(5.0 * (x[i] + 5.0)) * np.exp(-0.06 * (x[i] + 5.0)**2)
            elif x[i] > 4.5:
                f4 += 3.0 * np.cos(5.0 * (x[i] - 5.0)) * np.exp(-0.06 * (x[i] - 5.0)**2)
                
        # Asymmetric sextic terms with radial influence
        f5 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                f5 += 1.0 * x[i]**6 * np.exp(-0.015 * r**2)
            else:
                f5 += 1.0 * x[i]**6 * np.exp(-0.015 * r**2)
                
        # Fractal-like radial component with chaotic modulation
        f6 = 0.0
        for k in range(1, 15):
            freq_mod = 1.5 + 0.8 * np.sin(0.7 * k + 1.3)
            f6 += np.sin(freq_mod * r) * np.exp(-0.05 * r**2) / (k + 2.0)
            
        # Adaptive conditioning with oscillating weights and chaotic modulation
        f7 = 0.0
        for i in range(self.dim):
            weight = 1.5 + 0.8 * np.sin(0.9 * i + 1.4)
            f7 += weight * x[i]**2 * np.exp(-0.04 * x[i]**2)
            
        # Cross-dimensional exponential coupling with chaotic modulation and quintic interactions
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_mod = 1.0 + 0.5 * np.sin(0.6 * i * j + 1.7)
                f8 += chaos_mod * np.exp(-0.15 * (x[i]**2 + x[j]**2)) * (x[i] * x[j])**3
                
        # Boundary-repelling cosine terms with increasing amplitude and chaotic phases
        f9 = 0.0
        for i in range(self.dim):
            if x[i] < -4.0:
                f9 += 2.0 * np.cos(4.0 * (x[i] + 5.0) + 0.5) * np.exp(-0.1 * (x[i] + 5.0)**2)
            elif x[i] > 4.0:
                f9 += 2.0 * np.cos(4.0 * (x[i] - 5.0) + 0.5) * np.exp(-0.1 * (x[i] - 5.0)**2)
                
        # Sine wave radial component with varying phase and stochastic modulation
        f10 = 0.0
        for k in range(1, 10):
            phase = 0.5 * np.cos(0.6 * k + 1.8)
            f10 += np.sin(k * r + phase) * np.exp(-0.03 * r**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10