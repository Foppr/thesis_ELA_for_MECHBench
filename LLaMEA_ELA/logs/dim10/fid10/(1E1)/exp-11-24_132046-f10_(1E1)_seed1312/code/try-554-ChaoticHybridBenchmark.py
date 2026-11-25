import numpy as np

class ChaoticHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basin structure with chaotic modulation
        radial_basins = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm)) * 
                              np.exp(-0.5 * (x_norm**2)))
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_modulation = np.sum(np.sin(2 * np.pi * x_norm) * 
                               np.cos(3 * np.pi * x_norm) * 
                               (1 + 0.3 * np.sin(5 * np.pi * x_norm)))
        
        # Asymmetric saddle points with polynomial scaling
        saddle_points = np.sum((x_norm**4 - 2 * x_norm**2) * 
                              (1 + 0.2 * np.cos(4 * np.pi * x_norm)) * 
                              np.exp(-0.1 * np.abs(x_norm)))
        
        # Multi-scale chaotic structure with fractal-like behavior
        chaotic_structure = np.sum(np.sin(np.pi * x_norm) * 
                                  np.cos(np.pi * x_norm) * 
                                  np.exp(-np.abs(x_norm)) * 
                                  (1 + 0.1 * np.sin(8 * np.pi * x_norm)))
        
        # Cross-dimensional interaction with asymmetric coupling
        cross_dim_interaction = np.sum((x_norm[:-1]**3 + x_norm[1:]**3) * 
                                      np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                      (1 + 0.15 * np.sin(6 * np.pi * x_norm[:-1])))
        
        # Power-law conditioned regions with local scaling
        power_law_conditioning = np.sum(np.abs(x_norm)**1.7 * 
                                       (1 + 0.25 * np.cos(7 * np.pi * x_norm)) * 
                                       np.exp(-0.3 * x_norm**2))
        
        # Combined chaotic landscape with varying curvature
        return 2.0 * (radial_basins + sin_modulation + saddle_points + 
                     chaotic_structure + cross_dim_interaction + power_law_conditioning)