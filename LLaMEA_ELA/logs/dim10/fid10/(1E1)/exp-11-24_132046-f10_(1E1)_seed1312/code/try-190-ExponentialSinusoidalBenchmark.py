import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay corridors with varying rates
        exp_corridors = np.sum(np.exp(-np.abs(x_norm) * (1 + 0.5 * np.sin(3 * x_norm))))
        
        # Sinusoidal modulation with adaptive frequency
        sin_modulation = np.sum(np.sin(2 * np.pi * x_norm) * 
                               np.cos(4 * np.pi * x_norm) * 
                               (1 + 0.3 * np.sin(6 * np.pi * x_norm)))
        
        # Radial symmetry with multi-scale peaks
        radial_symmetry = np.sum(np.exp(-0.5 * (x_norm**2)) * 
                                (1 + 0.4 * np.cos(8 * np.pi * x_norm)) * 
                                (1 + 0.3 * np.sin(12 * np.pi * x_norm)))
        
        # Adaptive conditioning with local scaling
        adaptive_conditioning = np.sum((1 + 0.6 * np.sin(2 * x_norm)) * 
                                     np.exp(-0.4 * x_norm**2) * 
                                     (1 + 0.2 * np.cos(5 * x_norm)))
        
        # Cross-dimensional interaction with chaotic coupling
        cross_dim_interaction = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                                     np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                     (1 + 0.25 * np.sin(4 * np.pi * x_norm[:-1])) * 
                                     (1 + 0.2 * np.cos(3 * np.pi * x_norm[1:])))
        
        # Multi-scale harmonic structure
        multi_harmonic = np.sum(np.sin(5 * x_norm) * np.cos(7 * x_norm) * 
                               (1 + 0.3 * np.sin(9 * x_norm)) * 
                               (1 + 0.25 * np.cos(11 * x_norm)))
        
        # Power-law conditioned regions with fractal-like behavior
        power_law = np.sum(np.abs(x_norm)**1.5 * (1 + 0.3 * np.sin(10 * x_norm)))
        
        # Combined landscape with different curvature regions
        return 2.0 * (exp_corridors + sin_modulation + radial_symmetry + 
                     adaptive_conditioning + cross_dim_interaction + 
                     multi_harmonic + power_law)