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
            cond = 1.0 + 0.4 * np.sin(0.5 * i)
            f1 += cond * (x[i]**4 - 2.0 * x[i]**2 + 0.5 * x[i])
            
        # Trigonometric wave interference pattern
        f2 = 0.0
        for i in range(self.dim):
            wave = 0.0
            for k in range(1, 7):
                wave += np.sin(k * x[i]) * np.cos(k * x[i] / 2.0)
            f2 += wave * np.exp(-0.15 * x[i]**2)
            
        # Cross-dimensional interference with frequency modulation
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_mod = 1.0 + 0.6 * np.sin(0.4 * (i + j))
                coupling = 0.3 + 0.7 * np.cos(0.25 * i) * np.sin(0.25 * j)
                f3 += coupling * np.sin(freq_mod * (x[i] + x[j])) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        # Radial harmonic potential with amplitude modulation
        r = np.sqrt(np.sum(x**2))
        f4 = 0.0
        for k in range(1, 10):
            amp = 1.0 + 0.4 * np.sin(0.6 * k)
            f4 += amp * np.cos(k * r) * np.exp(-0.03 * r**2)
            
        # Asymmetric boundary attraction with logarithmic scaling
        f5 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                f5 -= 2.0 * np.log(1.0 - x[i]/5.0) * np.exp(-0.05 * x[i]**2)
            else:
                f5 -= 2.0 * np.log(1.0 + x[i]/5.0) * np.exp(-0.05 * x[i]**2)
                
        # Saddle-point inducing cross-terms with adaptive weights
        f6 = 0.0
        for i in range(self.dim):
            weight = 0.6 + 0.4 * np.sin(0.35 * i)
            for j in range(i+1, self.dim):
                f6 += weight * (x[i]**2 - x[j]**2) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # High-frequency oscillatory component
        f7 = 0.0
        for i in range(self.dim):
            freq = 6.0 + 4.0 * np.sin(0.25 * i)
            amp = 1.2 + 0.5 * np.cos(0.35 * i)
            f7 += amp * np.sin(freq * x[i]) * np.exp(-0.015 * np.abs(x[i]))
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7