import numpy as np

class TrigonometricFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial conditioning with exponential decay and sine modulation
        r = np.sqrt(np.sum(x**2))
        radial_factor = np.exp(-0.1 * r) * (1.0 + 0.5 * np.sin(0.3 * r))
        
        # Trigonometric chaos with nested sine and cosine interactions
        f1 = 0.0
        for i in range(self.dim):
            f1 += np.sin(x[i])**2 + np.cos(x[i])**2 + 0.3 * np.sin(2 * x[i]) * np.cos(3 * x[i])
            
        # Fractal-like cross-dimensional interactions with recursive coupling
        f2 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.5 * np.sin(0.2 * (i * j) + 0.1 * r)
                interaction = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                f2 += coupling * interaction * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Dynamic phase-shifted harmonic oscillations
        f3 = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(0.1 * i + 0.2 * r)
            freq = 1.0 + 0.8 * np.cos(0.3 * i)
            amp = 1.0 + 0.3 * np.sin(0.2 * i)
            f3 += amp * np.sin(freq * x[i] + phase_shift) * np.exp(-0.05 * np.abs(x[i]))
            
        # Polynomial irregularities with chaotic coefficients
        f4 = 0.0
        for i in range(self.dim):
            coeff1 = 0.2 + 0.4 * np.sin(0.1 * i + 0.1 * r)
            coeff2 = 0.3 + 0.5 * np.cos(0.2 * i)
            coeff3 = 0.1 + 0.3 * np.sin(0.3 * i)
            f4 += coeff1 * x[i]**4 + coeff2 * x[i]**3 + coeff3 * x[i]**2
            
        # Boundary penalty with logarithmic scaling and exponential repulsion
        f5 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                penalty = 2.0 * np.log(1.0 - x[i]/5.0)**2
            else:
                penalty = 2.0 * np.log(1.0 + x[i]/5.0)**2
            f5 += penalty * np.exp(-0.08 * x[i]**2)
            
        # Chaotic cubic terms with radial coupling
        f6 = 0.0
        for i in range(self.dim):
            coeff = 0.6 + 0.4 * np.sin(0.4 * i + 0.1 * r)
            f6 += coeff * x[i]**3 * np.exp(-0.03 * x[i]**2)
            
        # Cross-dimensional sine modulation with dynamic strength
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.4 + 0.6 * np.sin(0.1 * (i + j) + 0.2 * r)
                f7 += strength * np.sin(x[i] + x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Additional chaotic cosine interactions with radial influence
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 1.0 + 0.4 * np.cos(0.15 * (i * j) + 0.2 * r)
                f8 += mod * np.cos(x[i] * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        return radial_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)