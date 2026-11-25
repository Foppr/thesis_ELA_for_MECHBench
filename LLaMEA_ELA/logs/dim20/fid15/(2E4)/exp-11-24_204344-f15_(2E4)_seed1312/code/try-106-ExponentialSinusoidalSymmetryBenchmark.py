import numpy as np

class ExponentialSinusoidalSymmetryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Radial component with enhanced non-linearity
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-0.2 * r) * np.sin(7 * r) * np.cos(1.5 * r)
        
        # Sinusoidal modulations in each dimension
        sin_mod = 0.0
        for i in range(self.dim):
            sin_mod += np.sin(3.0 * (i + 1) * x[i]) * np.cos(4.0 * (i + 1) * x[i])
        
        # Exponential decay with adaptive scaling per dimension
        exp_decay = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + np.exp(-1.0 * x[i]))
            exp_decay += scale * np.exp(-0.5 * (x[i] - 1.0)**2) * np.sin(5.0 * x[i])
        
        # Cross-dimensional exponential interaction with stronger coupling
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_exp += np.exp(-0.4 * (x[i]**2 + x[j]**2)) * np.cos(3.0 * x[i] * x[j])
        
        # Adaptive harmonic landscape with varying frequencies
        harmonic = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.4)
            amp = 1.0 + 0.2 * np.cos(i * 0.5)
            harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Multi-scale oscillatory behavior with radial dependence
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += np.sin(12 * x[i]) * np.cos(10 * x[i]) * np.exp(-0.15 * np.abs(x[i]))
        
        # Asymmetric potential wells with radial symmetry
        wells = 0.0
        for i in range(self.dim):
            wells += (x[i]**2 - 2.0 * x[i] + 1.0) * np.exp(-0.5 * (x[i] - 1.0)**2)
        
        # Final combination with modified weights
        return 0.4 * radial + 0.5 * sin_mod + 0.6 * exp_decay + 0.7 * cross_exp + \
               0.8 * harmonic + 0.9 * oscillatory + 1.0 * wells