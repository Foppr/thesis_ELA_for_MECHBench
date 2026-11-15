import numpy as np

class ExponentialTrigonometricPenalty:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay components with oscillating amplitudes
        exp_decay = 0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 0.6)
            exp_decay += amp * np.exp(-0.5 * (x[i] / (1.0 + 0.1 * i))**2)
        
        # Trigonometric wave interactions with varying frequencies and phases
        wave_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 1.0 + 0.3 * np.sin(i * 0.4 + j * 0.3)
                phase = 0.2 * np.cos(i * 0.5 + j * 0.4)
                wave_interaction += np.sin(freq * (x[i] + x[j]) + phase) * np.cos(freq * (x[i] - x[j]))
        
        # Adaptive penalty terms based on distance from center points
        penalty = 0
        center_points = np.linspace(-3.0, 3.0, min(8, self.dim))
        for i in range(self.dim):
            if i < len(center_points):
                dist = np.abs(x[i] - center_points[i])
                penalty += 0.5 * dist**2 * np.exp(-0.1 * dist)
        
        # Dynamic dimensionality scaling with chaotic modulation
        scale_factor = 1.0
        for i in range(self.dim):
            scale_factor *= (1.0 + 0.2 * np.sin(i * 0.7))
        
        # Cross-dimensional coupling with polynomial interactions
        coupling = 0
        for i in range(self.dim - 1):
            coupling += (x[i]**2 + x[i+1]**2) * (x[i] * x[i+1])**0.5
        
        # High-order polynomial with chaotic coefficients
        poly_high = 0
        for i in range(self.dim):
            coeff = 0.8 + 0.4 * np.sin(i * 0.9)
            poly_high += coeff * x[i]**5
        
        # Fractal-like recursive structure with self-similarity
        fractal = 0
        if self.dim >= 3:
            for i in range(0, self.dim - 2, 3):
                fractal += (x[i]**2 + x[i+1]**2 + x[i+2]**2)**(1.3 + 0.1 * np.sin(i * 0.2))
        
        # Combined fitness with refined weights
        return 0.8 * exp_decay + 0.6 * wave_interaction + 0.4 * penalty + 0.3 * coupling + 0.2 * poly_high + 0.15 * fractal