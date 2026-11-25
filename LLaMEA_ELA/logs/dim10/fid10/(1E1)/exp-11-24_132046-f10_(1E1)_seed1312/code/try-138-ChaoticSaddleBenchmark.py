import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.a = 3.9
        self.b = 0.5
        self.c = 2.0
        self.d = 1.5
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Chaotic component with logistic map
        chaotic = np.sum(np.log(1 + self.a * x_norm * (1 - x_norm)))
        
        # Saddle point structure with hyperbolic tangents
        saddle = np.sum(np.tanh(self.b * x_norm) * np.tanh(self.c * x_norm**2))
        
        # Fractal-like dimensionality with multi-scale oscillations
        fractal = np.sum(np.sin(2**self.dim * x_norm) * np.cos(3**self.dim * x_norm))
        
        # Time-varying fitness with sinusoidal modulation
        time_varying = np.sum(np.sin(self.d * x_norm + np.pi * self.dim / 10.0) * 
                             np.cos(self.d * x_norm + np.pi * self.dim / 5.0))
        
        # Embedded local minima with varying curvature
        local_min = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm)) * 
                          (1 + 0.3 * np.cos(5 * x_norm)))
        
        # Cross-dimensional coupling with exponential decay
        cross_dim = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * 
                          (1 + 0.2 * np.sin(4 * x_norm[:-1]) * np.cos(3 * x_norm[1:])))
        
        # Multi-modal structure with varying amplitudes
        multi_modal = np.sum(np.sin(8 * x_norm) * np.cos(6 * x_norm) * 
                           (1 + 0.5 * np.sin(4 * x_norm)) * 
                           (1 + 0.3 * np.cos(2 * x_norm)))
        
        # Combined fitness with weighted components
        return (0.8 * chaotic + 
                0.6 * saddle + 
                0.7 * fractal + 
                0.9 * time_varying + 
                0.5 * local_min + 
                0.4 * cross_dim + 
                0.6 * multi_modal)