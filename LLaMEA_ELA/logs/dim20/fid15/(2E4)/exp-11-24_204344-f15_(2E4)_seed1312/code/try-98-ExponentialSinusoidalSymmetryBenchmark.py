import numpy as np

class ExponentialSinusoidalSymmetryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Radial component with exponential decay and chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-0.1 * r) * np.sin(5 * r) * np.cos(0.5 * r)
        
        # Sinusoidal modulations with dimensionally varying frequencies
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i * 0.7)
            sin_mod += np.sin(freq * x[i]) * np.cos(3 * x[i])
        
        # Exponential decay with chaotic scaling and asymmetric potentials
        exp_decay = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + np.exp(-x[i] * 0.5))
            exp_decay += scale * np.exp(-0.3 * (x[i] - 1.0)**2) * np.sin(4 * x[i]) * np.cos(2 * x[i])
        
        # Cross-dimensional exponential interaction with chaotic coupling
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.3 * (x[i]**2 + x[j]**2)) * np.cos(3 * x[i] * x[j])
                chaotic_factor = 1.0 + 0.2 * np.sin(i * j * 0.3)
                cross_exp += coupling * chaotic_factor
        
        # Adaptive harmonic landscape with dynamic frequencies and amplitudes
        harmonic = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(i * 0.5)
            amp = 0.9 + 0.1 * np.cos(i * 0.6)
            harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Multi-scale oscillatory behavior with chaotic radial dependence
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += np.sin(12 * x[i]) * np.cos(9 * x[i]) * np.exp(-0.15 * np.abs(x[i])) * np.sin(0.3 * r)
        
        # Asymmetric potential wells with chaotic depth and location
        wells = 0.0
        for i in range(self.dim):
            well_depth = 1.0 + 0.3 * np.sin(i * 0.4)
            well_location = 1.0 + 0.2 * np.cos(i * 0.5)
            wells += (x[i]**2 - 2 * well_location * x[i] + well_location**2) * \
                     np.exp(-0.4 * (x[i] - well_location)**2) * well_depth
        
        # Chaotic gradient component to increase saddle-point density
        chaotic_grad = 0.0
        for i in range(self.dim):
            chaotic_grad += np.sin(7 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.2 * x[i]**2) * \
                           (1.0 + 0.3 * np.sin(i * 0.8))
        
        # Final combination with enhanced non-convexity and chaotic weighting
        return 0.4 * radial + 0.5 * sin_mod + 0.6 * exp_decay + 0.7 * cross_exp + \
               0.8 * harmonic + 0.9 * oscillatory + 1.0 * wells + 0.5 * chaotic_grad