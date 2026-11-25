import numpy as np

class HybridFractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spherical component with adaptive radius
        spherical = np.sum(x_norm**2 * (1 + 0.3 * np.sin(5 * np.pi * x_norm)))
        
        # Saddle point structure with varying curvature
        saddle = np.sum((x_norm[:-1]**2 - x_norm[1:]**2) * 
                       (1 + 0.2 * np.cos(3 * np.pi * x_norm[:-1])) * 
                       (1 + 0.1 * np.sin(4 * np.pi * x_norm[1:])))
        
        # Fractal-like correlation with self-similarity
        fractal = 0.0
        for i in range(self.dim - 1):
            for j in range(i + 1, self.dim):
                distance = np.abs(x_norm[i] - x_norm[j])
                fractal += np.exp(-distance**2 / (0.1 + 0.1 * np.sin(10 * np.pi * (x_norm[i] + x_norm[j]))))
        
        # Dynamic conditioning based on position
        dynamic_cond = np.sum((1 + 0.5 * np.sin(2 * np.pi * x_norm)) * 
                             np.cos(3 * np.pi * x_norm) * 
                             np.exp(-0.1 * np.abs(x_norm)))
        
        # Non-separable cross-dimensional interaction
        cross_dim = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                          np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                          (1 + 0.3 * np.sin(2 * np.pi * x_norm[:-1])) * 
                          (1 + 0.2 * np.cos(2 * np.pi * x_norm[1:])))
        
        # Multi-scale periodic modulation
        periodic = np.sum(np.sin(8 * x_norm) * np.cos(6 * x_norm) * 
                         (1 + 0.25 * np.sin(4 * x_norm)) * 
                         (1 + 0.2 * np.cos(3 * x_norm)))
        
        # Asymmetric valley structure
        asym_valley = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.2 * np.sin(7 * np.pi * x_norm))) * 
                           (1 + 0.1 * np.cos(5 * np.pi * x_norm)))
        
        # Combined function with different weights
        return 2.0 * spherical + 1.5 * saddle + 0.8 * fractal + 1.2 * dynamic_cond + \
               1.0 * cross_dim + 0.9 * periodic + 1.1 * asym_valley