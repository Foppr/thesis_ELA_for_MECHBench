import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors for different dimensions
        self.scaling_factors = [0.3, 0.7, 1.1, 1.5, 2.0][:min(dim, 5)]
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        base = np.sum(x**2) / self.dim
        
        # Fractal chaotic component with self-similar patterns
        fractal = 0.0
        for i in range(self.dim):
            scale = self.scaling_factors[i % len(self.scaling_factors)]
            # Multi-scale sinusoidal pattern with varying frequencies
            fractal += (np.sin(scale * x[i]) * np.cos(scale**2 * x[i]) + 
                       np.sin(scale**1.5 * x[i]) * np.cos(scale**3 * x[i])) * np.exp(-0.1 * np.abs(x[i]))
        
        # Multi-scale interference with adaptive weights
        interference = 0.0
        for i in range(self.dim):
            # Create interference patterns at different scales
            interference += (np.sin(2 * x[i]) * np.cos(3 * x[i]) + 
                           0.5 * np.sin(4 * x[i]) * np.cos(6 * x[i]) + 
                           0.3 * np.sin(8 * x[i]) * np.cos(12 * x[i])) * np.exp(-0.2 * x[i]**2)
        
        # Dimensionally adaptive complexity with exponential scaling
        adaptive = 0.0
        for i in range(self.dim):
            # Increase complexity based on dimension index
            dim_factor = (i + 1) / self.dim
            adaptive += (np.sin(5 * x[i]) * np.cos(4 * x[i]) + 
                        0.8 * np.sin(7 * x[i]) * np.cos(5 * x[i]) + 
                        0.6 * np.sin(9 * x[i]) * np.cos(7 * x[i])) * np.exp(-0.3 * dim_factor * x[i]**2)
        
        # Coupled fractal oscillators with phase modulation
        coupled = 0.0
        for i in range(self.dim - 1):
            # Phase-modulated coupling between adjacent dimensions
            coupled += (np.sin(x[i] + x[i+1]) * np.cos(x[i] - x[i+1]) + 
                       np.cos(2 * x[i] + x[i+1]) * np.sin(2 * x[i] - x[i+1])) * np.exp(-0.15 * (x[i]**2 + x[i+1]**2))
        
        # Multi-scale chaotic gradient fields
        chaotic_gradient = 0.0
        for i in range(self.dim):
            scale = self.scaling_factors[i % len(self.scaling_factors)]
            chaotic_gradient += (np.sin(scale**2 * x[i]) * np.cos(scale * x[i]**3) + 
                               np.sin(scale * x[i]**2) * np.cos(scale**3 * x[i])) * np.exp(-0.25 * np.abs(x[i]))
        
        # Combine all components with different weights to create complex fractal landscape
        return base + 1.8 * fractal + 1.4 * interference + 1.2 * adaptive + 0.9 * coupled + 0.7 * chaotic_gradient