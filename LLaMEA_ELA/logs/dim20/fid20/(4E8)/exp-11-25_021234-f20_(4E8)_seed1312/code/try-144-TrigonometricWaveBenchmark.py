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
            
        # Chaotic radial component with fractal-like scaling
        f8 = 0.0
        for i in range(self.dim):
            r_i = np.abs(x[i])
            f8 += (1.0 + 0.2 * np.sin(10.0 * r_i)) * np.exp(-0.5 * r_i**2) * np.cos(3.0 * r_i)
            
        # Enhanced cross-dimensional coupling with chaotic modulation
        f9 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_mod = 1.0 + 0.3 * np.sin(2.0 * i * j)
                coupling = 0.1 * np.cos(0.5 * (i + j)) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                f9 += coupling * np.sin(chaos_mod * (x[i]**2 + x[j]**2)) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Multi-scale harmonic interference with adaptive frequencies
        f10 = 0.0
        for k in range(1, 10):
            freq_k = 2.0 + 1.5 * np.sin(0.1 * k)
            amp_k = 0.5 + 0.5 * np.cos(0.2 * k)
            f10 += amp_k * np.sin(freq_k * r) * np.exp(-0.03 * r**2)
            
        # Additional fractal-like harmonic components
        f11 = 0.0
        for i in range(self.dim):
            for k in range(1, 5):
                freq = 3.0 + 2.0 * np.sin(0.1 * i * k)
                amp = 0.3 + 0.2 * np.cos(0.15 * i * k)
                f11 += amp * np.sin(freq * x[i]) * np.exp(-0.02 * x[i]**2)
                
        # Enhanced radial fractal component with multi-scale modulation
        f12 = 0.0
        for k in range(1, 6):
            scale = 0.5 + 0.5 * np.sin(0.2 * k)
            f12 += scale * np.cos(k * r) * np.exp(-0.01 * r**2) * np.sin(2.0 * r)
            
        # Cross-dimensional chaotic coupling with time-varying weights
        f13 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                time_weight = 1.0 + 0.4 * np.sin(0.5 * (i + j) * r)
                f13 += time_weight * np.cos(2.0 * (x[i] - x[j])) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # High-dimensional harmonic interference with non-linear scaling
        f14 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(0.3 * i)
            f14 += scale * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.03 * x[i]**2)
            
        # Multi-modal boundary effect with exponential scaling
        f15 = 0.0
        for i in range(self.dim):
            if x[i] < -4.0 or x[i] > 4.0:
                f15 += 2.0 * np.exp(-0.5 * (x[i] - 5.0)**2) + 2.0 * np.exp(-0.5 * (x[i] + 5.0)**2)
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15