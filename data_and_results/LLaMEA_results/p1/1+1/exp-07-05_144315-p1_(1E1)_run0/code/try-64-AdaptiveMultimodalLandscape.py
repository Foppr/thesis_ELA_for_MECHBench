import numpy as np

class AdaptiveMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal wave component with varying frequencies
        sin_wave = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x))
        
        # Gaussian peaks with adaptive positions and widths
        gaussian = 0.0
        for i in range(1, 6):
            center = np.full(self.dim, (-1)**i * i * 0.5)
            width = 0.5 + 0.1 * i
            gaussian += np.exp(-0.5 * np.sum(((x - center) / width)**2)) * np.sin(2 * np.pi * np.sum(x - center))
        
        # Polynomial terms with increasing degree
        poly = 0.0
        for i in range(1, 5):
            poly += (0.1 * i) * np.sum(x**(i+1))
        
        # Cross-dimensional interaction terms
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(0.5 * x[i]) * np.cos(0.3 * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Adaptive scaling based on distance from origin
        distance = np.sqrt(np.sum(x**2))
        scale = 1.0 + 0.2 * np.sin(0.5 * distance) + 0.1 * np.cos(0.3 * distance)
        
        # Chaotic modulation using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Combine all components with different weights
        return 0.8 * sin_wave + 1.2 * gaussian + 0.5 * poly + 0.3 * cross + scale + 0.4 * chaotic