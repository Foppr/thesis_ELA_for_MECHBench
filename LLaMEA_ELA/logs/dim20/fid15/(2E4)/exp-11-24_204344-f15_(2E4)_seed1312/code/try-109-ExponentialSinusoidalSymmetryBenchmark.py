import numpy as np

class ExponentialSinusoidalSymmetryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Chaotic radial component with irregular exponential decay
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-0.2 * r) * np.sin(8 * r + np.sin(3 * r)) + 0.1 * np.cos(5 * r)
        
        # Irregular sinusoidal modulations with chaotic frequency shifts
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(i * 0.7) + 0.5 * np.cos(i * 1.3)
            phase = 1.0 + 0.3 * np.sin(i * 0.9)
            sin_mod += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase * 0.5)
        
        # Complex exponential decay with chaotic scaling and multiple peaks
        exp_decay = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + np.exp(-x[i] + 0.7)) + 0.2 * np.sin(x[i] * 2.5)
            exp_decay += scale * np.exp(-0.5 * (x[i] - 1.0)**2) * np.sin(5.0 * x[i] + np.cos(x[i]))
        
        # Cross-dimensional chaotic interaction with non-linear coupling
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.4 * (x[i]**2 + x[j]**2)) * np.cos(3.0 * x[i] * x[j] + np.sin(x[i] + x[j]))
                cross_exp += coupling * (1.0 + 0.2 * np.sin(i * j * 0.5))
        
        # Multi-scale harmonic landscape with irregular amplitudes and frequencies
        harmonic = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(i * 0.4) + 0.3 * np.cos(i * 0.6)
            amp = 1.0 + 0.2 * np.sin(i * 0.5) + 0.1 * np.cos(i * 0.7)
            harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] + np.sin(x[i]))
        
        # Oscillatory behavior with chaotic decay and irregular frequencies
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 12 + 4 * np.sin(i * 0.3)
            oscillatory += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.15 * np.abs(x[i])) * (1.0 + 0.1 * np.sin(x[i] * 3))
        
        # Asymmetric potential wells with chaotic minima and irregular energy barriers
        wells = 0.0
        for i in range(self.dim):
            min_pos = 1.0 + 0.5 * np.sin(i * 0.8)
            well_depth = 1.2 + 0.3 * np.cos(i * 0.6)
            wells += (x[i]**2 - 2.0 * x[i] + min_pos) * np.exp(-0.5 * (x[i] - min_pos)**2) * well_depth
        
        # Final combination with chaotic weights
        return 0.4 * radial + 0.5 * sin_mod + 0.6 * exp_decay + 0.7 * cross_exp + \
               0.8 * harmonic + 0.9 * oscillatory + 1.0 * wells