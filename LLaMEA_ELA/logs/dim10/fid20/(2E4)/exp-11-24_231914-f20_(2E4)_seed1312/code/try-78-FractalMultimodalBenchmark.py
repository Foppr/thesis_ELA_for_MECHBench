import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors for different dimensions
        self.scaling_factors = [0.2, 0.6, 1.0, 1.4, 1.8][:min(dim, 5)]
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        base = np.sum(x**2) / self.dim
        
        # Enhanced fractal chaotic component with self-similar patterns
        fractal = 0.0
        for i in range(self.dim):
            scale = self.scaling_factors[i % len(self.scaling_factors)]
            # Multi-scale sinusoidal pattern with varying frequencies and amplitudes
            fractal += (np.sin(scale * x[i]) * np.cos(scale**2 * x[i]) + 
                       np.sin(scale**1.5 * x[i]) * np.cos(scale**3 * x[i]) + 
                       0.5 * np.sin(scale**2.5 * x[i]) * np.cos(scale**4 * x[i])) * np.exp(-0.1 * np.abs(x[i]))
        
        # Multi-scale interference with adaptive weights and phase shifts
        interference = 0.0
        for i in range(self.dim):
            # Create interference patterns at different scales with phase modulation
            interference += (np.sin(2 * x[i] + 0.5) * np.cos(3 * x[i] + 1.0) + 
                           0.5 * np.sin(4 * x[i] + 0.3) * np.cos(6 * x[i] + 0.7) + 
                           0.3 * np.sin(8 * x[i] + 0.1) * np.cos(12 * x[i] + 0.9)) * np.exp(-0.2 * x[i]**2)
        
        # Dimensionally adaptive complexity with exponential scaling and dynamic weights
        adaptive = 0.0
        for i in range(self.dim):
            # Increase complexity based on dimension index with dynamic weighting
            dim_factor = (i + 1) / self.dim
            adaptive += (np.sin(5 * x[i]) * np.cos(4 * x[i]) + 
                        0.8 * np.sin(7 * x[i]) * np.cos(5 * x[i]) + 
                        0.6 * np.sin(9 * x[i]) * np.cos(7 * x[i]) + 
                        0.4 * np.sin(11 * x[i]) * np.cos(9 * x[i])) * np.exp(-0.3 * dim_factor * x[i]**2)
        
        # Coupled fractal oscillators with enhanced phase modulation and interaction
        coupled = 0.0
        for i in range(self.dim - 1):
            # Enhanced phase-modulated coupling between adjacent dimensions
            coupled += (np.sin(x[i] + x[i+1] + 0.5) * np.cos(x[i] - x[i+1] + 1.0) + 
                       np.cos(2 * x[i] + x[i+1] + 0.3) * np.sin(2 * x[i] - x[i+1] + 0.7) + 
                       0.5 * np.sin(x[i] + 2 * x[i+1] + 0.2) * np.cos(2 * x[i] + x[i+1] + 0.8)) * np.exp(-0.15 * (x[i]**2 + x[i+1]**2))
        
        # Enhanced multi-scale chaotic gradient fields with higher frequency components
        chaotic_gradient = 0.0
        for i in range(self.dim):
            scale = self.scaling_factors[i % len(self.scaling_factors)]
            chaotic_gradient += (np.sin(scale**2 * x[i]) * np.cos(scale * x[i]**3) + 
                               np.sin(scale * x[i]**2) * np.cos(scale**3 * x[i]) + 
                               0.7 * np.sin(scale**4 * x[i]) * np.cos(scale**5 * x[i])) * np.exp(-0.25 * np.abs(x[i]))
        
        # Additional high-frequency chaotic component for increased complexity
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += (np.sin(15 * x[i]) * np.cos(13 * x[i]) + 
                         0.9 * np.sin(17 * x[i]) * np.cos(16 * x[i]) + 
                         0.8 * np.sin(19 * x[i]) * np.cos(18 * x[i])) * np.exp(-0.1 * x[i]**2)
        
        # Combine all components with optimized weights to create complex fractal landscape
        return base + 2.0 * fractal + 1.5 * interference + 1.3 * adaptive + 1.0 * coupled + 0.8 * chaotic_gradient + 0.6 * high_freq