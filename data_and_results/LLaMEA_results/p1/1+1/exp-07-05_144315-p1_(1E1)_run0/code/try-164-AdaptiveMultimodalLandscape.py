import numpy as np

class AdaptiveMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base component with varying degrees
        poly = np.sum(x**4) + 0.5 * np.sum(x**3) + 0.1 * np.sum(x**2)
        
        # Exponential decay with adaptive rates
        exp_decay = 0.0
        for i in range(self.dim):
            rate = 0.3 + 0.7 * np.sin(i * 0.5)
            exp_decay += np.exp(-rate * np.abs(x[i]))
        
        # Sinusoidal modulation with frequency adaptation
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.cos(i * 0.3)
            sin_mod += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Cross-dimensional coupling with distance-based interaction
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                cross += np.exp(-0.5 * dist**2) * np.sin(3 * dist)
        
        # Adaptive peak components with dynamic positions
        peaks = 0.0
        peak_positions = np.linspace(-4.0, 4.0, 7)
        for i, pos in enumerate(peak_positions):
            width = 0.5 + 0.5 * np.cos(i * 0.4)
            peaks += np.exp(-0.5 * ((x - pos) / width)**2)
        
        # Asymmetric saddle with exponential weighting
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i]**2 - 2 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Fractional power component for nonlinearity
        frac_power = 0.0
        for i in range(self.dim):
            frac_power += (np.abs(x[i]) ** 1.7) * np.cos(1.5 * x[i])
        
        # Combined with adaptive weights
        return 0.8 * poly + 0.6 * exp_decay + 0.7 * sin_mod + 0.5 * cross + 0.9 * peaks + 0.4 * saddle + 0.3 * frac_power