import numpy as np

class ExponentialSinusoidalSymmetryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Fractional chaotic radial component with irregular exponential decay
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-0.3 * r) * np.sin(10 * r + np.sin(4 * r)) + 0.15 * np.cos(6 * r)
        
        # Irregular sinusoidal modulations with fractional frequency shifts
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 4.0 + 3.0 * np.sin(i * 0.8) + 0.7 * np.cos(i * 1.5)
            phase = 1.2 + 0.4 * np.sin(i * 1.1)
            sin_mod += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase * 0.6)
        
        # Complex exponential decay with fractional scaling and multiple peaks
        exp_decay = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + np.exp(-x[i] + 0.8)) + 0.25 * np.sin(x[i] * 3.0)
            exp_decay += scale * np.exp(-0.6 * (x[i] - 1.2)**2) * np.sin(6.0 * x[i] + np.cos(x[i]))
        
        # Cross-dimensional fractional interaction with adaptive coupling
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.5 * (x[i]**2 + x[j]**2)) * np.cos(4.0 * x[i] * x[j] + np.sin(x[i] + x[j]))
                coupling *= (1.0 + 0.3 * np.sin(i * j * 0.6) + 0.2 * np.cos(i * j * 0.4))
                cross_exp += coupling
        
        # Multi-scale harmonic landscape with fractional amplitudes and frequencies
        harmonic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.0 * np.sin(i * 0.5) + 0.4 * np.cos(i * 0.8)
            amp = 1.2 + 0.3 * np.sin(i * 0.6) + 0.15 * np.cos(i * 0.9)
            harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] + np.sin(x[i]))
        
        # Oscillatory behavior with fractional decay and irregular frequencies
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 15 + 5 * np.sin(i * 0.4)
            oscillatory += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.2 * np.abs(x[i])) * (1.0 + 0.15 * np.sin(x[i] * 4))
        
        # Asymmetric potential wells with fractional minima and irregular energy barriers
        wells = 0.0
        for i in range(self.dim):
            min_pos = 1.2 + 0.6 * np.sin(i * 0.9)
            well_depth = 1.5 + 0.4 * np.cos(i * 0.7)
            wells += (x[i]**2 - 2.2 * x[i] + min_pos) * np.exp(-0.6 * (x[i] - min_pos)**2) * well_depth
        
        # Final combination with fractional weights
        return 0.5 * radial + 0.6 * sin_mod + 0.7 * exp_decay + 0.8 * cross_exp + \
               0.9 * harmonic + 1.0 * oscillatory + 1.1 * wells