import numpy as np

class TrigonometricRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric oscillation terms with varying frequencies and amplitudes
        f1 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.5 * i)
            amp = 1.0 + 0.8 * np.cos(0.3 * i)
            f1 += amp * np.sin(freq * x[i]) * np.exp(-0.02 * x[i]**2)
            
        # Radial conditioning with exponential decay
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            cond = 1.0 + 0.6 * np.sin(0.4 * i)
            f2 += cond * x[i]**2 * np.exp(-0.03 * r**2)
            
        # Cross-dimensional cubic coupling with adaptive phase shifts
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = 0.5 * np.sin(0.3 * (i + j))
                weight = 0.8 + 0.4 * np.cos(0.2 * (i - j))
                f3 += weight * x[i]**3 * x[j] * np.exp(-0.01 * (x[i]**2 + x[j]**2)) * np.sin(phase_shift)
                
        # Multi-scale harmonic interference with boundary effects
        f4 = 0.0
        for i in range(self.dim):
            if x[i] < -4.5:
                f4 += 2.0 * np.cos(4.0 * (x[i] + 5.0)) * np.exp(-0.05 * (x[i] + 5.0)**2)
            elif x[i] > 4.5:
                f4 += 2.0 * np.cos(4.0 * (x[i] - 5.0)) * np.exp(-0.05 * (x[i] - 5.0)**2)
                
        # Asymmetric quartic terms with radial influence
        f5 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                f5 += 0.7 * x[i]**4 * np.exp(-0.01 * r**2)
            else:
                f5 += 0.7 * x[i]**4 * np.exp(-0.01 * r**2)
                
        # Fractal-like radial component with trigonometric modulation
        f6 = 0.0
        for k in range(1, 10):
            freq_mod = 1.0 + 0.5 * np.sin(0.6 * k)
            f6 += np.sin(freq_mod * r) * np.exp(-0.04 * r**2) / (k + 1.0)
            
        # Adaptive conditioning with oscillating weights
        f7 = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.5 * np.sin(0.7 * i)
            f7 += weight * x[i]**2 * np.exp(-0.03 * x[i]**2)
            
        # Cross-dimensional exponential coupling with chaotic modulation
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_mod = 1.0 + 0.3 * np.sin(0.4 * i * j)
                f8 += chaos_mod * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * (x[i] * x[j])**2
                
        # Boundary-repelling cosine terms with increasing amplitude
        f9 = 0.0
        for i in range(self.dim):
            if x[i] < -4.0:
                f9 += 1.5 * np.cos(3.0 * (x[i] + 5.0)) * np.exp(-0.08 * (x[i] + 5.0)**2)
            elif x[i] > 4.0:
                f9 += 1.5 * np.cos(3.0 * (x[i] - 5.0)) * np.exp(-0.08 * (x[i] - 5.0)**2)
                
        # Sine wave radial component with varying phase
        f10 = 0.0
        for k in range(1, 7):
            phase = 0.3 * np.cos(0.5 * k)
            f10 += np.sin(k * r + phase) * np.exp(-0.02 * r**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10