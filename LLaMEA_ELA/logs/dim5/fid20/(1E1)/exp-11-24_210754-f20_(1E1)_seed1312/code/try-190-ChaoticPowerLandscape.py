import numpy as np

class ChaoticPowerLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term with exponential scaling
        f1 = np.sum(np.exp(0.5 * x**2) - 1.0) / self.dim
        
        # Trigonometric interference with chaotic frequency modulation
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 10.0 * (1.0 + 0.5 * np.sin(i * 0.7)) * (1.0 + 0.3 * np.cos(i * 0.9))
            f2 += np.sin(freq * xi) * np.cos(freq * xi**1.5) * np.exp(-0.1 * xi**2)
        
        # Power-law scaling with multi-scale interaction
        f3 = 0.3 * np.sum(np.abs(x)**(1.7 + 0.3 * np.sin(x))) / self.dim
        
        # Exponential decay with sinusoidal modulation
        f4 = 0.2 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(8.0 * x) * np.cos(5.0 * x))
        
        # Asymmetric saddle points with fractional powers
        f5 = 0.15 * np.sum((x**3.2 + 0.4 * x**2.1 - 0.6 * x) * np.exp(-0.2 * np.abs(x)))
        
        # Cross-term interactions with varying coupling strength
        f6 = 0.1 * np.sum(np.sin(0.5 * x[:-1]) * np.cos(0.8 * x[1:]) * (x[:-1]**2 + x[1:]**2))
        
        # Fractal-like self-similarity through recursive scaling
        f7 = 0.25 * np.sum(np.sin(20.0 * np.sin(5.0 * x)) * np.cos(15.0 * np.cos(3.0 * x)))
        
        # Combined landscape with adjusted weights for chaotic behavior
        return f1 + f2 + f3 + f4 + f5 + f6 + f7