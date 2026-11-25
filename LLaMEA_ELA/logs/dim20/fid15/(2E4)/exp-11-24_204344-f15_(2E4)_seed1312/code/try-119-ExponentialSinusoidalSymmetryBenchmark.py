import numpy as np

class ExponentialSinusoidalSymmetryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Chaotic radial component with irregular exponential decay and multi-scale oscillations
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-0.15 * r) * (np.sin(10 * r + np.sin(4 * r)) + 0.3 * np.cos(7 * r)) + 0.15 * np.sin(3 * r)
        
        # Irregular sinusoidal modulations with chaotic frequency shifts and amplitude variations
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 2.5 + 1.5 * np.sin(i * 0.6) + 0.8 * np.cos(i * 1.2)
            amp = 0.8 + 0.4 * np.sin(i * 0.8) + 0.2 * np.cos(i * 1.0)
            phase = 0.8 + 0.3 * np.sin(i * 0.9)
            sin_mod += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase * 0.6)
        
        # Complex exponential decay with chaotic scaling and multiple peaks
        exp_decay = 0.0
        for i in range(self.dim):
            scale = 1.2 / (1.0 + np.exp(-x[i] + 0.8)) + 0.3 * np.sin(x[i] * 3.0)
            exp_decay += scale * np.exp(-0.6 * (x[i] - 1.2)**2) * np.sin(6.0 * x[i] + np.cos(x[i]))
        
        # Cross-dimensional chaotic interaction with non-linear coupling and asymmetric interactions
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.3 * (x[i]**2 + x[j]**2)) * np.cos(4.0 * x[i] * x[j] + np.sin(x[i] + x[j]))
                cross_exp += coupling * (1.0 + 0.3 * np.sin(i * j * 0.6) + 0.2 * np.cos(i * j * 0.4))
        
        # Multi-scale harmonic landscape with irregular amplitudes and frequencies
        harmonic = 0.0
        for i in range(self.dim):
            freq = 1.2 + 0.9 * np.sin(i * 0.5) + 0.4 * np.cos(i * 0.7)
            amp = 1.2 + 0.3 * np.sin(i * 0.6) + 0.15 * np.cos(i * 0.8)
            harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] + np.sin(x[i]))
        
        # Oscillatory behavior with chaotic decay and irregular frequencies
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 15 + 5 * np.sin(i * 0.4)
            oscillatory += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.2 * np.abs(x[i])) * (1.0 + 0.2 * np.sin(x[i] * 4))
        
        # Asymmetric potential wells with chaotic minima and irregular energy barriers
        wells = 0.0
        for i in range(self.dim):
            min_pos = 1.2 + 0.6 * np.sin(i * 0.7)
            well_depth = 1.3 + 0.4 * np.cos(i * 0.5)
            wells += (x[i]**2 - 2.2 * x[i] + min_pos) * np.exp(-0.4 * (x[i] - min_pos)**2) * well_depth
        
        # Fractional calculus enhancement for increased complexity
        fractional = 0.0
        for i in range(self.dim):
            fractional += np.sin(x[i] * np.pi / 2) * np.cos(x[i] * np.pi / 3) * (1.0 + 0.1 * np.sin(x[i] * 0.5))
        
        # Adaptive coupling strengths based on dimensionality
        adaptive = 0.0
        for i in range(self.dim):
            adaptive += (i + 1) * np.exp(-0.5 * x[i]**2) * np.sin(x[i] * (i + 1) * 0.3)
        
        # Final combination with chaotic weights and additional complexity
        return 0.5 * radial + 0.6 * sin_mod + 0.7 * exp_decay + 0.8 * cross_exp + \
               0.9 * harmonic + 1.0 * oscillatory + 1.1 * wells + 0.2 * np.sum(np.abs(x)) + \
               0.3 * fractional + 0.4 * adaptive