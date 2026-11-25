import numpy as np

class ChaoticRadialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basin structure with chaotic modulation
        radial_basin = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm)) * 
                             np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Sinusoidal modulations creating chaotic interference patterns
        sinusoidal_mod = np.sum(np.sin(7 * x_norm) * np.cos(5 * x_norm) * 
                               (1 + 0.3 * np.sin(3 * x_norm)) * 
                               (1 + 0.2 * np.cos(4 * x_norm)))
        
        # Asymmetric saddle points with varying curvature
        saddle_points = np.sum((x_norm**4 - 2 * x_norm**2) * 
                              (1 + 0.5 * np.sin(6 * x_norm)) * 
                              np.exp(-0.1 * np.abs(x_norm)))
        
        # Multi-scale fractal-like structure with chaotic scaling
        fractal_structure = np.sum(np.exp(-np.abs(x_norm) / (0.1 + 0.2 * np.cos(8 * x_norm))) * 
                                  np.sin(3 * x_norm)**2)
        
        # Cross-dimensional coupling with chaotic interaction
        cross_dim_coupling = np.sum(np.sin(np.pi * x_norm[:-1]) * 
                                   np.cos(np.pi * x_norm[1:]) * 
                                   (1 + 0.4 * np.sin(2 * np.pi * x_norm[:-1])) * 
                                   (1 + 0.3 * np.cos(3 * np.pi * x_norm[1:])))
        
        # Power-law conditioned regions with chaotic fluctuations
        power_law_conditioning = np.sum(np.abs(x_norm)**1.7 * 
                                       (1 + 0.25 * np.sin(9 * x_norm)) * 
                                       (1 + 0.2 * np.cos(6 * x_norm)))
        
        # Combined landscape with chaotic curvature variations
        return 2.0 * (radial_basin + sinusoidal_mod + saddle_points + 
                     fractal_structure + cross_dim_coupling + power_law_conditioning)