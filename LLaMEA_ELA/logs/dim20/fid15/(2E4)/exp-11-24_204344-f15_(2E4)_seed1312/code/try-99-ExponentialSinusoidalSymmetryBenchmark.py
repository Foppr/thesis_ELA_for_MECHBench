import numpy as np

class ExponentialSinusoidalSymmetryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-0.1 * r) * np.sin(5 * r)
        
        # Sinusoidal modulations in each dimension
        sin_mod = 0.0
        for i in range(self.dim):
            sin_mod += np.sin(2 * (i + 1) * x[i]) * np.cos(3 * (i + 1) * x[i])
        
        # Exponential decay with adaptive scaling per dimension
        exp_decay = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + np.exp(-x[i]))
            exp_decay += scale * np.exp(-0.5 * (x[i] - 1.0)**2) * np.sin(4 * x[i])
        
        # Cross-dimensional exponential interaction
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_exp += np.exp(-0.2 * (x[i]**2 + x[j]**2)) * np.cos(2 * x[i] * x[j])
        
        # Adaptive harmonic landscape with varying frequencies
        harmonic = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.3)
            amp = 0.8 + 0.2 * np.cos(i * 0.4)
            harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Multi-scale oscillatory behavior with radial dependence
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        
        # Asymmetric potential wells with radial symmetry
        wells = 0.0
        for i in range(self.dim):
            wells += (x[i]**2 - 2 * x[i] + 1) * np.exp(-0.5 * (x[i] - 1.0)**2)
        
        # Final combination with weighted components
        return 0.3 * radial + 0.4 * sin_mod + 0.5 * exp_decay + 0.6 * cross_exp + \
               0.7 * harmonic + 0.8 * oscillatory + 0.9 * wells