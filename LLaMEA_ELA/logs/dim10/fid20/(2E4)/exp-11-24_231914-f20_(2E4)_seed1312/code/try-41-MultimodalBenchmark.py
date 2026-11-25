import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like structure using recursive sine modulation
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(2 ** (i + 1) * x[i]) * np.cos(2 ** (i + 1) * x[i])
        
        # Sine-wave modulation with adaptive frequency
        wave_mod = 0.0
        for i in range(self.dim):
            wave_mod += np.sin(10 * x[i] * (1 + 0.1 * np.sin(5 * x[i]))) ** 2
        
        # Adaptive curvature term that changes based on dimension
        curvature = 0.0
        for i in range(self.dim):
            curvature += (x[i] ** 4) * np.exp(-0.1 * (i + 1)) * np.cos(3 * x[i])
        
        # Multi-scale oscillation with exponential decay
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.exp(-0.05 * i)
        
        # Asymmetric Gaussian-like hills with varying width
        gaussian_hills = 0.0
        for i in range(self.dim):
            gaussian_hills += np.exp(-0.5 * ((x[i] - 2) / (1 + 0.1 * x[i])) ** 2) + \
                              np.exp(-0.5 * ((x[i] + 2) / (1 + 0.1 * x[i])) ** 2)
        
        # Combine all components
        return 0.1 * fractal + 0.3 * wave_mod + 0.2 * curvature + 0.25 * multi_scale + 0.15 * gaussian_hills