import numpy as np

class ExponentialSinusoidalSymmetryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Fractional chaotic radial component with irregular exponential decay and dynamic frequency
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-0.3 * r) * np.sin(10 * r + np.sin(4 * r)) + 0.15 * np.cos(6 * r)
        
        # Irregular sinusoidal modulations with fractional frequency shifts and dynamic phase
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 4.0 + 3.0 * np.sin(i * 0.8) + 0.7 * np.cos(i * 1.5) + 0.2 * np.sin(i * 0.3)
            phase = 1.2 + 0.4 * np.sin(i * 1.1) + 0.1 * np.cos(i * 0.9)
            sin_mod += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase * 0.6) * np.exp(-0.1 * np.abs(x[i]))
        
        # Complex exponential decay with fractional scaling, multiple peaks and dynamic amplitude
        exp_decay = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + np.exp(-x[i] + 0.8)) + 0.25 * np.sin(x[i] * 3.0)
            amp = 1.0 + 0.3 * np.sin(i * 0.7) + 0.1 * np.cos(i * 0.4)
            exp_decay += scale * np.exp(-0.6 * (x[i] - 1.2)**2) * np.sin(6.0 * x[i] + np.cos(x[i])) * amp
        
        # Cross-dimensional fractional interaction with adaptive coupling and dynamic strength
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.5 * (x[i]**2 + x[j]**2)) * np.cos(4.0 * x[i] * x[j] + np.sin(x[i] + x[j]))
                coupling *= (1.0 + 0.3 * np.sin(i * j * 0.6) + 0.2 * np.cos(i * j * 0.4))
                coupling *= (1.0 + 0.1 * np.sin(i * 0.5) * np.cos(j * 0.3))
                cross_exp += coupling
        
        # Multi-scale harmonic landscape with fractional amplitudes, frequencies and dynamic phase
        harmonic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.0 * np.sin(i * 0.5) + 0.4 * np.cos(i * 0.8) + 0.2 * np.sin(i * 0.2)
            amp = 1.2 + 0.3 * np.sin(i * 0.6) + 0.15 * np.cos(i * 0.9) + 0.1 * np.sin(i * 0.4)
            phase = 0.5 + 0.2 * np.sin(i * 0.3) + 0.1 * np.cos(i * 0.7)
            harmonic += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase + np.sin(x[i]))
        
        # Oscillatory behavior with fractional decay, irregular frequencies and dynamic damping
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 15 + 5 * np.sin(i * 0.4) + 2 * np.cos(i * 0.6)
            damp = 0.8 + 0.2 * np.sin(i * 0.3)
            oscillatory += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.2 * np.abs(x[i])) * damp * (1.0 + 0.15 * np.sin(x[i] * 4))
        
        # Asymmetric potential wells with fractional minima, irregular energy barriers and dynamic depth
        wells = 0.0
        for i in range(self.dim):
            min_pos = 1.2 + 0.6 * np.sin(i * 0.9) + 0.1 * np.cos(i * 0.5)
            well_depth = 1.5 + 0.4 * np.cos(i * 0.7) + 0.1 * np.sin(i * 0.8)
            wells += (x[i]**2 - 2.2 * x[i] + min_pos) * np.exp(-0.6 * (x[i] - min_pos)**2) * well_depth
        
        # Additional chaotic modulation with dynamic scaling factors
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaos_factor = 1.0 + 0.5 * np.sin(i * 0.3) * np.cos(i * 0.7)
            chaotic_mod += np.sin(x[i] * chaos_factor) * np.cos(x[i] * chaos_factor) * np.exp(-0.3 * x[i]**2)
        
        # Final combination with fractional weights and dynamic scaling
        return (0.5 * radial + 0.6 * sin_mod + 0.7 * exp_decay + 0.8 * cross_exp + 
                0.9 * harmonic + 1.0 * oscillatory + 1.1 * wells + 0.4 * chaotic_mod)