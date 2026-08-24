import numpy as np

class AdaptiveMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with varying degrees
        poly = 0.0
        for i in range(self.dim):
            degree = 2 + int(3 * np.sin(i * 0.5))
            poly += (x[i] ** degree) * np.exp(-0.1 * np.abs(x[i]))
        
        # Exponential decay with adaptive rates
        exp_decay = 0.0
        for i in range(self.dim):
            rate = 0.5 + 0.8 * np.cos(i * 0.3)
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.sin(x[i])
        
        # Logarithmic barrier component
        log_barrier = 0.0
        for i in range(self.dim):
            log_barrier += np.log(1.0 + np.abs(x[i])) * np.cos(x[i] * 0.5)
        
        # Cross-dimensional interaction with adaptive coupling
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.7 * np.sin((i + j) * 0.2)
                cross += coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Adaptive multimodal peaks
        multimodal = 0.0
        num_peaks = 3
        for k in range(num_peaks):
            center = np.full(self.dim, (k - 1) * 2.0)
            peak_height = 1.0 + 2.0 * np.sin(k * 0.8)
            distance = np.sum((x - center) ** 2)
            multimodal += peak_height * np.exp(-0.5 * distance / (1.0 + k * 0.5))
        
        # Sine-cosine modulation with frequency adaptation
        modulated = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(i * 0.4)
            modulated += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Fractional power with adaptive exponents
        fractional = 0.0
        for i in range(self.dim):
            exponent = 1.2 + 0.8 * np.cos(i * 0.6)
            fractional += (np.abs(x[i]) ** exponent) * np.sin(x[i] * 0.5)
        
        # Combine all components with adaptive weights
        weights = np.array([0.8, 0.6, 0.7, 0.5, 0.9, 0.4, 0.3])
        components = np.array([poly, exp_decay, log_barrier, cross, multimodal, modulated, fractional])
        
        return np.sum(weights * components)