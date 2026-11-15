import numpy as np

class AdaptiveMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute parameters for adaptive conditioning
        self.conditioning_factors = np.linspace(0.3, 2.5, dim)
        self.frequency_modulators = np.sin(np.linspace(0, np.pi, dim)) + 1.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with varying degrees and conditioning
        poly = 0.0
        for i in range(self.dim):
            degree = 2 + (i % 4)
            poly += (x[i] ** degree) * self.conditioning_factors[i] * np.cos(i * 0.3)
        
        # Modified exponential decay component with adaptive rates
        exp_decay = 0.0
        for i in range(self.dim):
            rate = 0.05 + 0.4 * np.sin(i * 0.6)
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.sin(x[i] * 0.5)
        
        # Enhanced sinusoidal modulation with varying frequencies and amplitudes
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 0.5 + 3.0 * self.frequency_modulators[i]
            amp = 0.3 + 0.7 * np.cos(i * 0.4)
            sin_mod += amp * np.sin(freq * x[i]) * np.sin(freq * x[i] * 0.8)
        
        # Asymmetric hill-climbing valleys with adaptive steepness
        valley = 0.0
        for i in range(self.dim):
            steepness = 0.8 + 0.7 * np.sin(i * 0.5)
            if x[i] >= 0:
                valley += (x[i] ** 2.5) * steepness
            else:
                valley += (x[i] ** 3.5) * steepness
        
        # Enhanced cross-dimensional interaction with angle-based weighting
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = np.arctan2(x[j], x[i])
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross += np.sin(x[i] * x[j] * angle) * np.exp(-0.15 * dist)
        
        # Enhanced multimodal peaks with varying heights and widths
        peaks = 0.0
        peak_centers = np.linspace(-4.5, 4.5, 9)
        for center in peak_centers:
            width = 0.6 + 0.5 * np.sin(center * 0.4)
            height = 0.8 + 0.6 * np.cos(center * 0.2)
            peaks += height * np.exp(-0.3 * np.sum(((x - center) / width) ** 2))
        
        # Additional fractional power and logarithmic component for nonlinearity
        frac_log = 0.0
        for i in range(self.dim):
            if x[i] != 0:
                frac_log += (np.abs(x[i]) ** 1.8) * np.log(np.abs(x[i]) + 1.5)
        
        # Combine all components with adaptive weights
        weights = np.array([0.7, 0.5, 0.8, 0.6, 0.9, 0.3])
        components = np.array([poly, exp_decay, sin_mod, valley, cross, peaks])
        return np.sum(weights * components) + frac_log