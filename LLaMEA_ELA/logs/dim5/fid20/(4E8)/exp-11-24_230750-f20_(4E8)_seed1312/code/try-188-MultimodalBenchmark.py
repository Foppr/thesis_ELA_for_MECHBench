import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested harmonic oscillations with increasing frequency
        harmonics = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 4)
            harmonics += np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Exponential attraction basins towards multiple local minima
        attraction = 0.0
        centers = np.linspace(-4, 4, 5)
        for center in centers:
            dist = np.sum((x - center) ** 2)
            attraction += np.exp(-0.3 * dist) * np.cos(3 * np.pi * dist)
        
        # Dynamic penalty landscape with varying severity
        penalty = 0.0
        for i in range(self.dim):
            penalty += (np.abs(x[i]) - 2.5) ** 3 * np.exp(-0.15 * x[i]**2)
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        r = 3.8
        for i in range(self.dim):
            if i == 0:
                chaotic += x[i] * (r * (1 - x[i]))
            else:
                chaotic += x[i] * (r * (1 - x[i-1]))
        
        # Multi-scale sinusoidal modulation with adaptive amplitude
        multiscale = 0.0
        for scale in [0.3, 0.7, 1.5]:
            multiscale += np.sum(np.sin(scale * x) * np.cos(scale * x) * 
                               np.exp(-0.08 * np.abs(x)))
        
        # Combined fitness with weighted components
        return 0.4 * harmonics + 0.35 * attraction + 0.25 * penalty + 0.15 * chaotic + multiscale