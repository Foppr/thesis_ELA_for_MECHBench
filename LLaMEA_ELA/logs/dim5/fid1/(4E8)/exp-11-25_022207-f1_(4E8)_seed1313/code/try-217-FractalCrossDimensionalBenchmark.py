import numpy as np

class FractalCrossDimensionalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like component with recursive harmonic structure
        fractal = 0.0
        for i in range(1, min(6, self.dim + 1)):
            freq = 2 ** i
            amplitude = 1.0 / (i * 2.0)
            fractal += amplitude * np.sin(freq * np.pi * x_norm[i-1]) * np.cos(freq * np.pi * x_norm[i-1])
        
        # Cross-dimensional coupling with varying interaction strengths
        cross_dim = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 1.0 / (1.0 + abs(i - j))
                cross_dim += strength * np.sin(np.pi * (x_norm[i] + x_norm[j])) * np.cos(np.pi * (x_norm[i] - x_norm[j]))
        
        # Adaptive conditioning based on position
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += (1.0 + 0.5 * np.sin(3.0 * np.pi * x_norm[i])) * x_norm[i]**2
        
        # Multi-scale Gaussian peaks with varying heights and widths
        peaks = 0.0
        peak_centers = np.linspace(-1, 1, 7)
        for center in peak_centers:
            peak_height = 1.0 / (1.0 + np.abs(center))
            peak_width = 0.2 + 0.3 * np.abs(center)
            peaks -= peak_height * np.exp(-0.5 * ((x_norm - center) / peak_width)**2)
        
        # Saddle-point structure with enhanced non-linearity
        saddle = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                saddle += (x_norm[i]**3 - x_norm[i+1]**3) * np.exp(-0.1 * (x_norm[i] + x_norm[i+1])**2)
        
        # Combined function with adaptive noise
        result = fractal + cross_dim + conditioning + peaks + saddle
        
        # Add robustness noise
        noise = 0.01 * np.random.rand() * (1.0 + 0.2 * np.abs(np.mean(x_norm)))
        
        return result + noise