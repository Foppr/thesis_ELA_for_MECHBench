import numpy as np

class ChaoticLogarithmicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logarithmic potential terms with varying scales
        f1 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(0.7 * i)
            if x[i] == 0:
                f1 += 10.0
            else:
                f1 += scale * np.log(np.abs(x[i]) + 1e-8) * np.exp(-0.1 * x[i]**2)
                
        # Radial saddle point with enhanced chaotic modulation
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            mod = 1.0 + 0.5 * np.sin(0.6 * i * r)  # Increased modulation strength
            f2 += mod * x[i]**2 * (x[i]**2 - 1.0) * np.exp(-0.05 * r**2)
            
        # Cross-dimensional cubic coupling with adaptive weights
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.7 + 0.3 * np.cos(0.4 * (i + j))  # Adjusted weight range
                f3 += weight * x[i]**3 * x[j] * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Boundary-repelling harmonic terms with increased penalty
        f4 = 0.0
        for i in range(self.dim):
            if x[i] < -4.0:
                f4 += 3.0 * np.cos(3.0 * (x[i] + 5.0)) * np.exp(-0.1 * (x[i] + 5.0)**2)  # Increased amplitude
            elif x[i] > 4.0:
                f4 += 3.0 * np.cos(3.0 * (x[i] - 5.0)) * np.exp(-0.1 * (x[i] - 5.0)**2)
                
        # Multi-scale chaotic oscillations with altered frequencies
        f5 = 0.0
        for i in range(self.dim):
            freq = 2.5 + 1.2 * np.sin(0.4 * i)  # Slightly increased base frequency
            amp = 1.0 + 0.9 * np.cos(0.3 * i)
            f5 += amp * np.sin(freq * x[i]) * np.exp(-0.03 * np.abs(x[i]))
            
        # Asymmetric radial harmonic with chaotic amplitude
        f6 = 0.0
        for k in range(1, 6):
            amp = 0.6 + 0.4 * np.sin(0.6 * k)  # Adjusted amplitude range
            phase = 0.25 * np.cos(0.4 * k)
            f6 += amp * np.cos(k * r + phase) * np.exp(-0.04 * r**2)
            
        # Saddle-point inducing quartic terms with boundary effects
        f7 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                f7 += 0.6 * (x[i]**4 - 2.0 * x[i]**2) * np.exp(-0.02 * x[i]**2)  # Slightly increased coefficient
            else:
                f7 += 0.6 * (x[i]**4 - 2.0 * x[i]**2) * np.exp(-0.02 * x[i]**2)
                
        # Cross-dimensional chaotic interaction with exponential scaling
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos_factor = 1.0 + 0.5 * np.sin(0.5 * i * j)  # Increased chaos factor
                coupling = np.exp(-0.12 * (x[i]**2 + x[j]**2)) * chaos_factor  # Slightly increased decay
                f8 += coupling * (x[i] * x[j])**2
                
        # Adaptive conditioning with logarithmic scaling
        f9 = 0.0
        for i in range(self.dim):
            cond = 1.0 + 0.4 * np.sin(0.6 * i)  # Increased conditioning
            f9 += cond * np.log(np.abs(x[i]) + 1.0) * np.exp(-0.05 * x[i]**2)
            
        # Fractal-like radial component with chaotic frequency modulation
        f10 = 0.0
        for k in range(1, 8):
            freq_mod = 1.0 + 0.4 * np.sin(0.7 * k)  # Increased modulation
            f10 += np.cos(freq_mod * r) * np.exp(-0.03 * r**2) / (k + 1.0)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10