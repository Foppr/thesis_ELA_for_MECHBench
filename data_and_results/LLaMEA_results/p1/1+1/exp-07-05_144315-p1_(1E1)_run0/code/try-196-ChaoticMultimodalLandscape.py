import numpy as np

class ChaoticMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameter generation for increased complexity
        np.random.seed(42)
        self.conditioning_factors = np.random.uniform(0.3, 2.5, dim)
        self.frequency_modulators = np.random.uniform(0.5, 3.0, dim)
        self.peak_centers = np.linspace(-4.5, 4.5, 9)
        self.peak_widths = np.random.uniform(0.4, 1.2, len(self.peak_centers))
        self.peak_heights = np.random.uniform(0.8, 1.8, len(self.peak_centers))
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with chaotic conditioning
        poly = 0.0
        for i in range(self.dim):
            degree = 2 + (i % 4)
            poly += (x[i] ** degree) * self.conditioning_factors[i]
        
        # Chaotic exponential decay with dynamic rates
        exp_decay = 0.0
        for i in range(self.dim):
            rate = 0.02 + 0.6 * np.sin(i * 1.3 + np.pi/4) * np.cos(i * 0.7)
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.sin(x[i] * 1.5)
        
        # Chaotic sinusoidal modulation with dynamic frequencies
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * self.frequency_modulators[i]
            amp = 0.4 + 0.8 * np.sin(i * 0.9 + np.pi/3)
            sin_mod += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8)
        
        # Chaotic valley component with dynamic steepness
        valley = 0.0
        for i in range(self.dim):
            steepness = 0.8 + 0.9 * np.sin(i * 1.1 + np.pi/2)
            if x[i] >= 0:
                valley += (x[i] ** 2.5) * steepness
            else:
                valley += (x[i] ** 3.5) * steepness
        
        # Cross-dimensional interaction with chaotic distance weighting
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                weight = np.sin(i * 0.5 + j * 0.3) * np.cos(i * 0.4 + j * 0.6)
                cross += weight * np.sin(x[i] * x[j]) * np.exp(-0.2 * dist)
        
        # Chaotic multimodal peaks with dynamic parameters
        peaks = 0.0
        for i, (center, width, height) in enumerate(zip(self.peak_centers, self.peak_widths, self.peak_heights)):
            peaks += height * np.exp(-0.5 * np.sum(((x - center) / width) ** 2))
        
        # Chaotic fractional power and logarithmic component
        frac_log = 0.0
        for i in range(self.dim):
            if x[i] != 0:
                frac_log += (np.abs(x[i]) ** 1.9) * np.log(np.abs(x[i]) + 1.0) * np.sin(i * 0.7)
        
        # Combine all components with chaotic weights
        weights = np.random.uniform(0.5, 1.5, 6)
        components = np.array([poly, exp_decay, sin_mod, valley, cross, peaks])
        return np.sum(weights * components) + frac_log