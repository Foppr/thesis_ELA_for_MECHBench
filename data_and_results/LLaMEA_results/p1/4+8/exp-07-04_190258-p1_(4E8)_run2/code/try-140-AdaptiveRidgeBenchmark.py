import numpy as np

class AdaptiveRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base with adaptive conditioning
        quadratic = 0.5 * np.sum(x**2)
        
        # Sinusoidal modulation with varying frequencies
        sinusoidal = 0
        for i in range(self.dim):
            sinusoidal += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Gaussian ridges with adaptive width and height
        gaussian_ridges = 0
        for i in range(self.dim):
            gaussian_ridges += np.exp(-0.5 * ((x[i] - 1.0) / 0.5)**2) * np.sin(5 * x[i]) + \
                               np.exp(-0.5 * ((x[i] + 1.0) / 0.3)**2) * np.cos(4 * x[i])
        
        # Sharp ridge structure with exponential decay
        sharp_ridge = 0
        for i in range(self.dim):
            sharp_ridge += np.exp(-10 * np.abs(x[i] - 2.0)) * np.sin(2 * x[i]) + \
                          np.exp(-10 * np.abs(x[i] + 2.0)) * np.cos(2 * x[i])
        
        # Cross-dimensional interaction with polynomial coupling
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.1 * (x[i]**2 + x[j]**2) * np.sin(0.5 * x[i] * x[j])
        
        # Adaptive noise component with varying intensity
        noise = 0
        for i in range(self.dim):
            noise += 0.05 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Fractal-like structure with recursive pattern
        fractal = 0
        for i in range(self.dim):
            fractal += np.sin(8 * x[i]) * np.cos(6 * x[i]) * np.exp(-0.02 * x[i]**2) * \
                      np.sin(0.1 * np.sum(x**2))
        
        # Asymmetric penalty for out-of-bounds regions
        penalty = 0
        for i in range(self.dim):
            if x[i] < -4.5 or x[i] > 4.5:
                penalty += 100 * (np.abs(x[i]) - 4.5)**2
        
        return quadratic + sinusoidal + gaussian_ridges + sharp_ridge + coupling + noise + fractal + penalty