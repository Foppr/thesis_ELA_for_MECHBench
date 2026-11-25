import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested exponential potentials with radial scaling and adaptive exponents
        r = np.sqrt(np.sum(x**2))
        exp_base = 0.1 * r
        f1 = np.exp(-exp_base) * (0.3 * r**2 + 0.7 * r**4)
        
        # Chaotic sine potentials with dynamic frequencies and amplitude modulation
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.5 + 4.0 * np.sin(0.5 * i + 0.3 * r)
            amp = 1.0 + 0.5 * np.cos(0.4 * i)
            f2 += amp * np.sin(freq * x[i]) * np.exp(-0.03 * x[i]**2)
            
        # Fractal-like cross-dimensional interaction terms with recursive coupling
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.7 * np.sin(0.2 * (i + j) + 0.1 * r)
                f3 += coupling * np.sin(x[i] * x[j]) * np.exp(-0.01 * (x[i]**2 + x[j]**2))
                
        # Dynamic harmonic oscillations with time-varying phases and multi-scale modulation
        f4 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 2.5 * np.sin(0.3 * i)
            amp = 1.2 + 0.8 * np.cos(0.2 * i + 0.1 * r)
            phase = 0.4 * np.sin(0.1 * i + 0.2 * r)
            f4 += amp * np.sin(freq * x[i] + phase) * np.exp(-0.05 * np.abs(x[i]))
            
        # Enhanced boundary penalty with logarithmic and power scaling
        f5 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                penalty = 3.0 * np.log(1.0 - x[i]/5.0)**2
            else:
                penalty = 3.0 * np.log(1.0 + x[i]/5.0)**2
            f5 += penalty * np.exp(-0.06 * x[i]**2)
            
        # Stochastic phase-coupled cross-terms with dynamic interaction strengths
        f6 = 0.0
        for i in range(self.dim):
            phase = np.random.uniform(0, 2*np.pi) + 0.1 * r
            for j in range(i+1, self.dim):
                strength = 0.6 + 0.4 * np.sin(0.3 * (i - j) + 0.2 * r)
                f6 += strength * np.cos(x[i] + phase) * np.sin(x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Global irregularity through nested polynomial terms with chaotic coefficients
        f7 = 0.0
        for i in range(self.dim):
            coeff1 = 0.1 + 0.3 * np.sin(0.2 * i)
            coeff2 = 0.5 + 0.5 * np.cos(0.3 * i)
            coeff3 = 0.2 + 0.4 * np.sin(0.4 * i)
            f7 += coeff1 * x[i]**4 + coeff2 * x[i]**3 + coeff3 * x[i]**2
            
        # Additional chaotic cubic terms for increased multimodality
        f8 = 0.0
        for i in range(self.dim):
            coeff = 0.8 + 0.4 * np.sin(0.5 * i + 0.1 * r)
            f8 += coeff * x[i]**3 * np.exp(-0.02 * x[i]**2)
            
        # Cross-dimensional chaotic coupling with sine modulation
        f9 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 1.0 + 0.3 * np.sin(0.1 * (i * j) + 0.2 * r)
                f9 += mod * np.sin(x[i] + x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9