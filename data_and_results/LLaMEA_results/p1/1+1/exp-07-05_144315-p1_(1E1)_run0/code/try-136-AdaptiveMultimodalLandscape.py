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
        
        # Exponential decay component with adaptive rates
        exp_decay = 0.0
        for i in range(self.dim):
            rate = 0.5 + 0.8 * np.cos(i * 0.3)
            exp_decay += np.exp(-rate * np.abs(x[i])) * np.sin(x[i])
        
        # Sinusoidal modulation with frequency adaptation
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(i * 0.7)
            sin_mod += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
        
        # Cross-dimensional interaction with varying coupling strengths
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range coupling
                coupling = 0.3 + 0.7 * np.sin((i + j) * 0.2)
                cross += coupling * np.sin(x[i] + x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Multimodal peaks with varying heights and widths
        peaks = 0.0
        peak_centers = np.linspace(-4.0, 4.0, 7)
        for center in peak_centers:
            width = 0.8 + 0.4 * np.cos(center * 0.5)
            height = 1.5 + 1.0 * np.sin(center * 0.3)
            peaks += height * np.exp(-0.5 * np.sum(((x - center) / width) ** 2))
        
        # Asymmetric component with varying skewness
        skew = 0.0
        for i in range(self.dim):
            skew_factor = 0.5 + 0.5 * np.sin(i * 0.8)
            skew += (x[i] ** 3) * np.exp(-skew_factor * x[i] ** 2)
        
        # Adaptive scaling based on dimension
        scale_factor = 1.0 + 0.3 * np.sin(self.dim * 0.2)
        
        # Final combination with dynamic weights
        return (0.8 * poly + 0.6 * exp_decay + 0.5 * sin_mod + 
                0.7 * cross + 0.9 * peaks + 0.4 * skew) * scale_factor