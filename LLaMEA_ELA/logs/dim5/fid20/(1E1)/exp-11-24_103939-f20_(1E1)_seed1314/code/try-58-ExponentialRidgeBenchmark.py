import numpy as np

class ExponentialRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Exponentially decaying sinusoidal components
        f1 = 0.0
        for i in range(self.dim):
            frequency = 2 ** (i % 4)
            decay = np.exp(-0.1 * i)
            f1 += decay * np.sin(frequency * x_scaled[i]) * np.cos(frequency * x_scaled[i])
        
        # Adaptive ridge structure with varying heights
        f2 = 0.0
        for i in range(self.dim):
            ridge_height = 2.0 + 0.5 * np.sin(i)
            ridge_width = 0.1 + 0.2 * np.cos(i)
            f2 += ridge_height * np.exp(-0.5 * ((x_scaled[i] - 0.5) / ridge_width)**2)
        
        # Cross-dimensional interaction with exponential decay
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay_factor = np.exp(-0.05 * (i + j))
                f3 += decay_factor * np.sin(x_scaled[i]) * np.cos(x_scaled[j])
        
        # Asymmetric multimodal components
        f4 = 0.0
        for i in range(self.dim):
            asymmetry = 0.3 * np.sin(i)
            f4 += (x_scaled[i]**2 + asymmetry * x_scaled[i])**3
        
        # Boundary attraction with exponential penalty
        f5 = 0.0
        for i in range(self.dim):
            f5 += 0.5 * np.exp(2 * np.abs(x_scaled[i]) - 1)
        
        # High-frequency oscillation with dimension-dependent amplitude
        f6 = 0.0
        for i in range(self.dim):
            amplitude = 1.0 + 0.2 * np.sin(i)
            f6 += amplitude * np.sin(20 * x_scaled[i])
        
        return f1 + f2 + f3 + f4 + f5 + f6