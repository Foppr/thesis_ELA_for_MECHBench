import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with nested exponential potentials and fractal-like conditioning
        r = np.sqrt(np.sum(x**2))
        f1 = (np.exp(-0.2 * r) + 0.5 * np.exp(-0.5 * r) + 0.3 * np.exp(-r)) * (0.4 * r**2 + 0.1 * r**3)
        
        # Chaotic sine potentials with fractal frequency distributions and stochastic amplitudes
        f2 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i + 0.3 * np.sin(0.7 * i))
            amp = 1.0 + 0.5 * np.cos(0.4 * i + 0.2 * np.sin(0.6 * i))
            f2 += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Cross-dimensional interaction terms with fractal coupling strengths and dynamic phase shifts
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.6 + 0.4 * np.sin(0.5 * (i - j) + 0.3 * np.cos(0.4 * (i + j)))
                phase_shift = 0.2 * np.sin(0.3 * i + 0.4 * j)
                f3 += coupling * np.sin(x[i] + phase_shift) * np.cos(x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Multi-scale harmonic oscillations with chaotic amplitude modulation and fractal phase patterns
        f4 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 4.0 * np.sin(0.3 * i + 0.2 * np.cos(0.5 * i))
            amp = 1.5 + 0.8 * np.sin(0.4 * i + 0.3 * np.cos(0.6 * i))
            phase = 0.5 * np.sin(0.2 * i + 0.1 * np.cos(0.3 * i))
            f4 += amp * np.sin(freq * x[i] + phase) * np.exp(-0.15 * np.abs(x[i]))
            
        # Enhanced boundary penalties with logarithmic scaling and chaotic weight distributions
        f5 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                penalty = 4.0 * np.log(1.0 - x[i]/5.0 + 0.1 * np.sin(0.3 * i))
            else:
                penalty = 4.0 * np.log(1.0 + x[i]/5.0 + 0.1 * np.cos(0.3 * i))
            f5 += penalty * np.exp(-0.1 * x[i]**2)
            
        # Saddle-point inducing terms with chaotic interaction strengths and fractal phase couplings
        f6 = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.sin(0.4 * i + 0.3 * np.cos(0.5 * i))
            for j in range(i+1, self.dim):
                strength = 0.7 + 0.3 * np.sin(0.3 * (i + j) + 0.2 * np.cos(0.4 * (i - j)))
                f6 += strength * np.sin(x[i] + phase) * np.cos(x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Global irregularity through radial polynomial terms with chaotic coefficients and cubic contributions
        f7 = 0.0
        for i in range(self.dim):
            coeff1 = 0.15 + 0.05 * np.sin(0.4 * i)
            coeff2 = 0.8 + 0.2 * np.cos(0.3 * i)
            coeff3 = 0.3 + 0.1 * np.sin(0.5 * i)
            f7 += coeff1 * x[i]**4 - coeff2 * x[i]**2 + coeff3 * x[i]**3
            
        # Additional chaotic cubic terms for enhanced multimodality
        f8 = 0.0
        for i in range(self.dim):
            f8 += 0.2 * np.sin(3.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8