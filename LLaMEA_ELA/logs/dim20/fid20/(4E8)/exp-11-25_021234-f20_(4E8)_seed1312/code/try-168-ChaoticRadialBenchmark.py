import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial quadratic component with exponential decay
        r = np.sqrt(np.sum(x**2))
        f1 = np.exp(-0.2 * r) * (0.5 * r**2)
        
        # Chaotic sine potentials along each dimension with varying frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.2 + 3.8 * np.sin(0.4 * i)
            f2 += np.sin(freq * x[i]) * np.exp(-0.08 * x[i]**2)
            
        # Cross-dimensional interaction terms with adaptive coupling strengths
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.4 + 0.6 * np.sin(0.35 * (i - j))
                f3 += coupling * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.025 * (x[i]**2 + x[j]**2))
                
        # Multi-scale harmonic oscillations with amplitude modulation and phase shifts
        f4 = 0.0
        for i in range(self.dim):
            freq = 1.3 + 2.7 * np.sin(0.25 * i)
            amp = 1.1 + 0.6 * np.cos(0.35 * i)
            phase = 0.3 * np.sin(0.15 * i)
            f4 += amp * np.sin(freq * x[i] + phase) * np.exp(-0.13 * np.abs(x[i]))
            
        # Asymmetric penalty near boundaries with logarithmic scaling and adaptive weights
        f5 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                penalty = 2.8 * np.log(1.0 - x[i]/5.0)
            else:
                penalty = 2.8 * np.log(1.0 + x[i]/5.0)
            f5 += penalty * np.exp(-0.07 * x[i]**2)
            
        # Saddle-point inducing cross-terms with randomized phase shifts and interaction strengths
        f6 = 0.0
        for i in range(self.dim):
            phase = np.random.uniform(0, 2*np.pi)
            for j in range(i+1, self.dim):
                strength = 0.35 + 0.65 * np.sin(0.25 * (i + j))
                f6 += strength * np.sin(x[i] + phase) * np.cos(x[j]) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        # Global irregularity through radial polynomial terms with mixed powers
        f7 = 0.0
        for i in range(self.dim):
            f7 += 0.15 * x[i]**4 - 0.75 * x[i]**2 + 0.28 * x[i]**3
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7