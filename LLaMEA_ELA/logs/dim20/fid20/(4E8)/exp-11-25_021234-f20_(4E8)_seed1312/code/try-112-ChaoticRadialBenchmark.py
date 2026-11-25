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
        
        # Chaotic sine potentials along each dimension
        f2 = 0.0
        for i in range(self.dim):
            f2 += np.sin(10.0 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Cross-dimensional interaction terms with varying coupling strengths
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.7 * np.sin(0.5 * (i + j))
                f3 += coupling * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Multi-scale harmonic oscillations with amplitude modulation
        f4 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(0.3 * i)
            amp = 1.0 + 0.5 * np.cos(0.2 * i)
            f4 += amp * np.sin(freq * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Asymmetric penalty near boundaries with logarithmic scaling
        f5 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                penalty = 2.0 * np.log(1.0 - x[i]/5.0)
            else:
                penalty = 2.0 * np.log(1.0 + x[i]/5.0)
            f5 += penalty * np.exp(-0.03 * x[i]**2)
            
        # Saddle-point inducing cross-terms with random phase shifts
        f6 = 0.0
        for i in range(self.dim):
            phase = np.random.uniform(0, 2*np.pi)
            for j in range(i+1, self.dim):
                f6 += np.sin(x[i] + phase) * np.cos(x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Global irregularity through radial polynomial terms
        f7 = 0.0
        for i in range(self.dim):
            f7 += 0.1 * x[i]**4 - 0.5 * x[i]**2
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7