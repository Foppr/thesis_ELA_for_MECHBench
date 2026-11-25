import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial exponential decay with oscillatory modulation
        r = np.sqrt(np.sum(x**2))
        f1 = np.exp(-0.1 * r) * (0.5 * r**2 + 0.3 * np.sin(3.0 * r))
        
        # Chaotic sine potentials with frequency modulation and adaptive amplitudes
        f2 = 0.0
        for i in range(self.dim):
            freq = 5.0 + 3.0 * np.sin(0.4 * i)
            amp = 1.0 + 0.7 * np.cos(0.3 * i)
            f2 += amp * np.sin(freq * x[i]) * np.exp(-0.08 * x[i]**2)
            
        # Cross-dimensional interaction terms with dynamic coupling strengths and phase shifts
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.5 * np.sin(0.7 * (i + j) + np.pi/4)
                phase_shift = 0.2 * np.sin(0.6 * i * j)
                f3 += coupling * np.sin(x[i] + phase_shift) * np.cos(x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Multi-scale harmonic oscillations with complex amplitude modulation
        f4 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 3.0 * np.sin(0.5 * i)
            amp = 1.0 + 1.5 * np.cos(0.4 * i) + 0.8 * np.sin(0.2 * i**2)
            f4 += amp * np.sin(freq * x[i]) * np.exp(-0.15 * np.abs(x[i]))
            
        # Asymmetric boundary penalty with piecewise logarithmic scaling and adaptive weights
        f5 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                penalty = 3.0 * np.log(1.0 - x[i]/5.0) + 0.5 * np.sin(2.0 * x[i])
            else:
                penalty = 3.0 * np.log(1.0 + x[i]/5.0) + 0.5 * np.cos(2.0 * x[i])
            f5 += penalty * np.exp(-0.04 * x[i]**2)
            
        # Saddle-point inducing cross-terms with randomized phase shifts and variable coupling
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.random.uniform(0, 2*np.pi) + 0.3 * np.sin(0.5 * (i + j))
                coupling = 0.4 + 0.6 * np.cos(0.3 * i * j)
                f6 += coupling * np.sin(x[i] + phase) * np.cos(x[j]) * np.exp(-0.06 * (x[i]**2 + x[j]**2))
                
        # Global irregularity through higher-order polynomial terms with random coefficients
        f7 = 0.0
        for i in range(self.dim):
            coeff1 = 0.1 + 0.05 * np.sin(0.3 * i)
            coeff2 = -0.5 + 0.2 * np.cos(0.4 * i)
            coeff3 = 0.05 + 0.03 * np.sin(0.6 * i)
            f7 += coeff1 * x[i]**4 + coeff2 * x[i]**2 + coeff3 * x[i]
            
        # Additional chaotic perturbation term with radial dependency
        f8 = 0.0
        for i in range(self.dim):
            f8 += 0.2 * np.sin(7.0 * x[i]) * np.exp(-0.1 * r) * np.cos(0.5 * i)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8