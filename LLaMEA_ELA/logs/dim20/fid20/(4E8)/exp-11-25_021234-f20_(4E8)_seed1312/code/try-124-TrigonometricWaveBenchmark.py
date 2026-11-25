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
            cond = 1.0 + 0.3 * np.sin(0.4 * i)
            f1 += cond * (x[i]**4 - 2.0 * x[i]**2 + 0.5 * x[i])
            
        # Trigonometric wave interference pattern
        f2 = 0.0
        for i in range(self.dim):
            wave = 0.0
            for k in range(1, 6):
                wave += np.sin(k * x[i]) * np.cos(k * x[i] / 2.0)
            f2 += wave * np.exp(-0.1 * x[i]**2)
            
        # Cross-dimensional interference with frequency modulation
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_mod = 1.0 + 0.5 * np.sin(0.3 * (i + j))
                coupling = 0.2 + 0.8 * np.cos(0.2 * i) * np.sin(0.2 * j)
                f3 += coupling * np.sin(freq_mod * (x[i] + x[j])) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Radial harmonic potential with amplitude modulation
        r = np.sqrt(np.sum(x**2))
        f4 = 0.0
        for k in range(1, 8):
            amp = 1.0 + 0.3 * np.sin(0.5 * k)
            f4 += amp * np.cos(k * r) * np.exp(-0.02 * r**2)
            
        # Asymmetric boundary attraction with logarithmic scaling
        f5 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                f5 -= 1.5 * np.log(1.0 - x[i]/5.0) * np.exp(-0.04 * x[i]**2)
            else:
                f5 -= 1.5 * np.log(1.0 + x[i]/5.0) * np.exp(-0.04 * x[i]**2)
                
        # Saddle-point inducing cross-terms with adaptive weights
        f6 = 0.0
        for i in range(self.dim):
            weight = 0.5 + 0.5 * np.sin(0.3 * i)
            for j in range(i+1, self.dim):
                f6 += weight * (x[i]**2 - x[j]**2) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # High-frequency oscillatory component
        f7 = 0.0
        for i in range(self.dim):
            freq = 5.0 + 3.0 * np.sin(0.2 * i)
            amp = 1.0 + 0.4 * np.cos(0.3 * i)
            f7 += amp * np.sin(freq * x[i]) * np.exp(-0.01 * np.abs(x[i]))
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7