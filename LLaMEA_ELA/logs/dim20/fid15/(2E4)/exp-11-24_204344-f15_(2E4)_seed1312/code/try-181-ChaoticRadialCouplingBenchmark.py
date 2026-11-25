import numpy as np

class ChaoticRadialCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Enhanced radial polynomial chaos with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial = (r**5 + 0.7 * r**4 - 1.8 * r**3 + 1.2 * r**2 + 0.9 * r + 0.6) * np.exp(-0.15 * r)
        
        # Modified symmetric polynomial landscape with increased local minima density
        poly = 0.0
        for i in range(self.dim):
            poly += (x[i]**7 - 2.5 * x[i]**5 + 1.8 * x[i]**3) * np.cos(0.6 * x[i])
        
        # Adaptive cross-dimensional coupling with time-varying interaction strengths
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.6 + 0.4 * np.sin(i * j * 0.8 + r * 0.3)
                cross += coupling_strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Dynamic scaling with enhanced frequency modulation
        dynamic_scale = 0.0
        for i in range(self.dim):
            scale_factor = 1.2 + 0.3 * np.sin(i * 1.5 + r * 0.4)
            dynamic_scale += scale_factor * np.exp(-0.6 * (x[i] - 0.3)**2) * np.sin(3.5 * x[i])
        
        # Enhanced harmonic components with fractional frequency coupling
        harmonic = 0.0
        for i in range(self.dim):
            freq = 2.5 + 1.2 * np.sin(i * 0.9 + r * 0.2)
            amp = 1.8 + 0.6 * np.cos(i * 0.7 + r * 0.3)
            harmonic += amp * np.sin(freq * x[i] + np.sin(x[i])) * np.cos(freq * x[i])
        
        # Improved noise injection with chaotic phase modulation
        noise = 0.0
        for i in range(self.dim):
            noise_amp = 0.4 + 0.15 * np.sin(i * 2.3 + r * 0.1)
            noise += noise_amp * np.sin(x[i] * np.pi * (1 + 0.15 * np.sin(i + r)))
        
        # Fractional dimensionality interaction with irregular coupling and enhanced conditioning
        frac_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i + j > 0:
                    frac_interaction += (x[i]**3 + x[j]**3) / (i + j + 0.5) * np.exp(-0.4 * (x[i] - x[j])**2)
        
        # Final combination with adjusted weights for improved difficulty
        return 0.7 * radial + 0.9 * poly + 0.8 * cross + 1.0 * dynamic_scale + \
               1.2 * harmonic + 0.6 * noise + 0.5 * frac_interaction