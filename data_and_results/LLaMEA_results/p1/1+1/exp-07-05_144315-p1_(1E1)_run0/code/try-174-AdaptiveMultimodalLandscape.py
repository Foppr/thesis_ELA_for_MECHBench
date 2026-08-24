import numpy as np

class AdaptiveMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute parameters for adaptive conditioning
        self.conditioning_factors = np.linspace(0.3, 2.5, dim)
        self.frequency_modulators = np.cos(np.linspace(0, np.pi/2, dim)) + 1.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with varying degrees and conditioning
        poly = 0.0
        for i in range(self.dim):
            degree = 2 + (i % 4)
            poly += (x[i] ** degree) * self.conditioning_factors[i] * (1.0 + 0.3 * np.sin(i * 0.7))
        
        # Improved exponential decay component with adaptive rates
        exp_decay = 0.0
        for i in range(self.dim):
            rate = 0.05 + 0.4 * np.cos(i * 0.6)
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.sin(x[i] * 0.5)
        
        # Enhanced sinusoidal modulation with varying frequencies and amplitudes
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 0.5 + 3.0 * self.frequency_modulators[i]
            amp = 0.3 + 0.7 * np.sin(i * 0.4)
            sin_mod += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8)
        
        # Enhanced asymmetric hill-climbing valleys with adaptive steepness
        valley = 0.0
        for i in range(self.dim):
            steepness = 0.8 + 0.7 * np.cos(i * 0.5)
            if x[i] >= 0:
                valley += (x[i] ** 2.5) * steepness
            else:
                valley += (x[i] ** 3.5) * steepness
        
        # Novel cross-dimensional interaction with correlation-based weighting
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross += np.cos(x[i] * x[j]) * np.exp(-0.15 * dist) * (1.0 + 0.2 * np.sin(i * j * 0.3))
        
        # Enhanced multimodal peaks with varying heights, widths, and positions
        peaks = 0.0
        peak_centers = np.linspace(-4.5, 4.5, 9)
        for center in peak_centers:
            width = 0.6 + 0.5 * np.cos(center * 0.4)
            height = 0.8 + 0.6 * np.sin(center * 0.2)
            peaks += height * np.exp(-0.5 * np.sum(((x - center) / width) ** 2))
        
        # Enhanced fractional power and logarithmic component for additional nonlinearity
        frac_log = 0.0
        for i in range(self.dim):
            if x[i] != 0:
                frac_log += (np.abs(x[i]) ** 1.8) * np.log(np.abs(x[i]) + 1.2)
        
        # Combine all components with optimized weights
        weights = np.array([0.9, 0.5, 0.8, 0.6, 0.7, 0.3])
        components = np.array([poly, exp_decay, sin_mod, valley, cross, peaks])
        return np.sum(weights * components) + frac_log