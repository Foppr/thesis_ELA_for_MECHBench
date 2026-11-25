import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basins with varying depths
        radial_basins = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm)) * 
                              (1 + 0.3 * np.cos(5 * x_norm)))
        
        # Sinusoidal oscillations in multiple dimensions
        sinusoidal_oscillations = np.sum(np.sin(2 * np.pi * x_norm) * 
                                        np.cos(3 * np.pi * x_norm) * 
                                        (1 + 0.2 * np.sin(4 * np.pi * x_norm)))
        
        # Cross-dimensional interaction with varying strength
        cross_dim_interaction = np.sum((x_norm[:-1]**2 + x_norm[1:]**2) * 
                                     np.exp(-0.5 * (x_norm[:-1] - x_norm[1:])**2) * 
                                     (1 + 0.1 * np.sin(6 * np.pi * x_norm[:-1])))
        
        # Adaptive conditioning based on distance from origin
        adaptive_conditioning = np.sum((1 + 0.5 * np.sin(3 * np.pi * x_norm)) * 
                                     np.exp(-0.2 * np.sum(x_norm**2)))
        
        # Multi-scale periodic structure
        multi_scale_periodic = np.sum(np.sin(8 * x_norm) * 
                                    np.cos(6 * x_norm) * 
                                    (1 + 0.25 * np.sin(4 * x_norm)) * 
                                    (1 + 0.15 * np.cos(2 * x_norm)))
        
        # Hybrid landscape with both convex and concave regions
        hybrid_regions = np.sum(np.abs(x_norm)**1.5 * (1 + 0.3 * np.sin(7 * x_norm)) + 
                               0.5 * np.cos(4 * np.pi * x_norm))
        
        # Combined function with weighted components
        return 2.0 * radial_basins + 1.5 * sinusoidal_oscillations + 1.2 * cross_dim_interaction + \
               1.8 * adaptive_conditioning + 1.0 * multi_scale_periodic + 1.3 * hybrid_regions