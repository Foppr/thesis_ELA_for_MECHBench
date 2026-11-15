import numpy as np

class AdaptiveMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute parameters for adaptive conditioning
        self.conditioning_factors = np.linspace(0.5, 2.0, dim)
        self.frequency_modulators = np.sin(np.linspace(0, np.pi, dim)) + 1.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with varying degrees and conditioning
        poly = 0.0
        for i in range(self.dim):
            degree = 2 + i % 3
            poly += (x[i] ** degree) * self.conditioning_factors[i]
        
        # Exponential decay component with modified rates
        exp_decay = 0.0
        for i in range(self.dim):
            rate = 0.05 + 0.4 * np.sin(i * 0.6)  # Slightly different rates
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.cos(x[i])
        
        # Sinusoidal modulation with altered frequencies and amplitudes
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 1.5 + 2.5 * self.frequency_modulators[i]  # Increased base frequency
            amp = 0.3 + 0.7 * np.cos(i * 0.4)  # Modified amplitude
            sin_mod += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Asymmetric hill-climbing valleys with adaptive steepness
        valley = 0.0
        for i in range(self.dim):
            steepness = 1.0 + 0.6 * np.sin(i * 0.4)  # Increased steepness
            if x[i] >= 0:
                valley += (x[i] ** 2) * steepness
            else:
                valley += (x[i] ** 3) * steepness
        
        # Cross-dimensional interaction with distance-based weighting
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross += np.sin(x[i] * x[j]) * np.exp(-0.15 * dist)  # Slightly stronger decay
        
        # Multimodal peaks with modified heights and widths
        peaks = 0.0
        peak_centers = np.linspace(-4.0, 4.0, 7)
        for center in peak_centers:
            width = 0.6 + 0.5 * np.sin(center * 0.6)  # Different width modulation
            height = 1.2 + 0.4 * np.cos(center * 0.4)  # Modified peak heights
            peaks += height * np.exp(-0.5 * np.sum(((x - center) / width) ** 2))
        
        # Fractional power and logarithmic component for additional nonlinearity
        frac_log = 0.0
        for i in range(self.dim):
            if x[i] != 0:
                frac_log += (np.abs(x[i]) ** 1.8) * np.log(np.abs(x[i]) + 1.0)
        
        # Combine all components with modified weights
        weights = np.array([0.7, 0.5, 0.8, 0.6, 0.8, 0.5])  # Slightly different weights
        components = np.array([poly, exp_decay, sin_mod, valley, cross, peaks])
        return np.sum(weights * components) + frac_log