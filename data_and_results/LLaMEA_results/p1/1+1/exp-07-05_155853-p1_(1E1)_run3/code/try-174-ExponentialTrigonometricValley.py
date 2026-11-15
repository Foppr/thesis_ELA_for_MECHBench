import numpy as np

class ExponentialTrigonometricValley:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay components with varying rates
        exp_decay = 0
        for i in range(self.dim):
            rate = 0.1 + 0.4 * np.sin(i * 0.5) + 0.2 * np.cos(i * 0.3)
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.cos(rate * x[i])
        
        # Trigonometric wave interference with dynamic frequencies and amplitudes
        wave_interference = 0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(i * 0.7)
            amp = 0.5 + 0.5 * np.cos(i * 0.4)
            wave_interference += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Adaptive parabolic valleys with dynamic curvature
        parabolic_valleys = 0
        for i in range(self.dim):
            curvature = 0.5 + 0.5 * np.sin(i * 0.6)
            valley_center = -3.0 + 6.0 * (i / max(1, self.dim - 1))
            parabolic_valleys += curvature * (x[i] - valley_center)**2
        
        # Dynamic conditioning with chaotic scaling factors
        conditioning = 0
        for i in range(self.dim):
            scale = 0.8 + 0.4 * np.sin(i * 0.8)
            conditioning += scale * x[i]**2
        
        # Cross-dimensional coupling with sine-based interactions
        cross_coupling = 0
        for i in range(self.dim - 1):
            coupling_strength = 0.3 + 0.2 * np.sin(i * 0.5)
            cross_coupling += coupling_strength * np.sin(x[i] + x[i+1]) * (x[i]**2 + x[i+1]**2)
        
        # Multi-scale periodic modulation with varying periods
        periodic_mod = 0
        for i in range(self.dim):
            period = 2.0 + 3.0 * np.sin(i * 0.9)
            periodic_mod += np.sin(2 * np.pi * x[i] / period) * np.cos(2 * np.pi * x[i] / (period * 0.5))
        
        # Asymmetric exponential terms for additional ruggedness
        asym_exp = 0
        for i in range(self.dim):
            asym_factor = 0.2 + 0.3 * np.sin(i * 0.6)
            asym_exp += asym_factor * np.exp(-np.abs(x[i]) / (1.0 + 0.1 * x[i]**2))
        
        # Combined fitness function with refined weights
        return 1.2 * exp_decay + 0.8 * wave_interference + 0.6 * parabolic_valleys + 0.4 * conditioning + 0.3 * cross_coupling + 0.2 * periodic_mod + 0.1 * asym_exp