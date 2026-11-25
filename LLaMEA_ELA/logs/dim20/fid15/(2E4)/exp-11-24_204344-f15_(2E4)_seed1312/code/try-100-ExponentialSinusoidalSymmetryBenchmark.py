import numpy as np

class ExponentialSinusoidalSymmetryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-0.15 * r) * np.sin(6 * r)
        
        # Sinusoidal modulations in each dimension
        sin_mod = 0.0
        for i in range(self.dim):
            sin_mod += np.sin(2.5 * (i + 1) * x[i]) * np.cos(3.5 * (i + 1) * x[i])
        
        # Exponential decay with adaptive scaling per dimension
        exp_decay = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + np.exp(-x[i] + 0.5))
            exp_decay += scale * np.exp(-0.4 * (x[i] - 1.2)**2) * np.sin(4.5 * x[i])
        
        # Cross-dimensional exponential interaction
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_exp += np.exp(-0.25 * (x[i]**2 + x[j]**2)) * np.cos(2.5 * x[i] * x[j])
        
        # Adaptive harmonic landscape with varying frequencies
        harmonic = 0.0
        for i in range(self.dim):
            freq = 1.2 + 0.4 * np.sin(i * 0.35)
            amp = 0.9 + 0.1 * np.cos(i * 0.45)
            harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Multi-scale oscillatory behavior with radial dependence
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += np.sin(11 * x[i]) * np.cos(9 * x[i]) * np.exp(-0.12 * np.abs(x[i]))
        
        # Asymmetric potential wells with radial symmetry
        wells = 0.0
        for i in range(self.dim):
            wells += (x[i]**2 - 2.2 * x[i] + 1.1) * np.exp(-0.55 * (x[i] - 1.1)**2)
        
        # Final combination with weighted components
        return 0.35 * radial + 0.45 * sin_mod + 0.55 * exp_decay + 0.65 * cross_exp + \
               0.75 * harmonic + 0.85 * oscillatory + 0.95 * wells