import numpy as np

class ExponentialSinusoidalSymmetryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Radial component with exponential decay and modified frequency
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-0.12 * r) * np.sin(7 * r)
        
        # Sinusoidal modulations with frequency shifts and phase adjustments
        sin_mod = 0.0
        for i in range(self.dim):
            sin_mod += np.sin(3.0 * (i + 1) * x[i] + 0.7) * np.cos(4.0 * (i + 1) * x[i] + 1.2)
        
        # Exponential decay with adaptive scaling per dimension and enhanced nonlinearity
        exp_decay = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + np.exp(-x[i] + 0.3))
            exp_decay += scale * np.exp(-0.5 * (x[i] - 1.0)**2) * np.sin(5.0 * x[i])
        
        # Cross-dimensional exponential interaction with modified scaling and coupling strength
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_exp += np.exp(-0.25 * (x[i]**2 + x[j]**2)) * np.cos(3.0 * x[i] * x[j])
        
        # Adaptive harmonic landscape with varying frequencies and amplitudes
        harmonic = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.4)
            amp = 0.8 + 0.2 * np.cos(i * 0.5)
            harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Multi-scale oscillatory behavior with radial dependence and modified decay
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += np.sin(12 * x[i]) * np.cos(10 * x[i]) * np.exp(-0.15 * np.abs(x[i]))
        
        # Asymmetric potential wells with radial symmetry and shifted minima
        wells = 0.0
        for i in range(self.dim):
            wells += (x[i]**2 - 2.0 * x[i] + 1.0) * np.exp(-0.5 * (x[i] - 1.0)**2)
        
        # Final combination with altered weights and added coupling term
        return 0.4 * radial + 0.5 * sin_mod + 0.6 * exp_decay + 0.7 * cross_exp + \
               0.8 * harmonic + 0.9 * oscillatory + 1.0 * wells