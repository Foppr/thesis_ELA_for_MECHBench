import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial quadratic component with exponential decay
        r = np.sqrt(np.sum(x**2))
        f1 = np.exp(-0.1 * r) * (0.5 * r**2)
        
        # Chaotic sine potentials along each dimension with adaptive amplitude
        f2 = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.3 * np.sin(0.7 * i)
            f2 += amp * np.sin(10.0 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Cross-dimensional interaction terms with adaptive coupling strengths
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.4 + 0.6 * np.sin(0.5 * (i + j) + np.pi/4)
                f3 += coupling * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Multi-scale harmonic oscillations with amplitude modulation and phase shifts
        f4 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.5 * np.sin(0.3 * i)
            amp = 1.0 + 0.6 * np.cos(0.2 * i)
            phase = 0.5 * np.sin(0.4 * i)
            f4 += amp * np.sin(freq * x[i] + phase) * np.exp(-0.1 * np.abs(x[i]))
            
        # Asymmetric penalty near boundaries with logarithmic scaling
        f5 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                penalty = 2.0 * np.log(1.0 - x[i]/5.0)
            else:
                penalty = 2.0 * np.log(1.0 + x[i]/5.0)
            f5 += penalty * np.exp(-0.03 * x[i]**2)
            
        # Saddle-point inducing cross-terms with randomized phase shifts and adaptive weights
        f6 = 0.0
        for i in range(self.dim):
            phase = np.random.uniform(0, 2*np.pi)
            weight = 0.5 + 0.5 * np.sin(0.3 * i)
            for j in range(i+1, self.dim):
                f6 += weight * np.sin(x[i] + phase) * np.cos(x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Global irregularity through radial polynomial terms with adaptive exponents
        f7 = 0.0
        for i in range(self.dim):
            exp = 4.0 + 1.0 * np.sin(0.5 * i)
            f7 += 0.1 * x[i]**exp - 0.5 * x[i]**2
            
        # Adaptive conditioning to improve conditioning and convergence
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.1 * np.abs(x[i]))
            
        return (f1 + f2 + f3 + f4 + f5 + f6 + f7) * condition_factor