import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basin structure with chaotic modulation
        radial_basins = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm)) * 
                              np.exp(-0.5 * (x_norm**2)))
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sinusoidal_mod = np.sum(np.sin(5 * x_norm) * np.cos(7 * x_norm) * 
                               (1 + 0.3 * np.sin(3 * x_norm)) * 
                               (1 + 0.2 * np.cos(4 * x_norm)))
        
        # Asymmetric saddle points with chaotic perturbations
        saddle_points = np.sum(np.abs(x_norm) * np.sin(2 * x_norm) * 
                              (1 + 0.4 * np.sin(8 * x_norm)) * 
                              (1 + 0.3 * np.cos(6 * x_norm)))
        
        # Cross-dimensional chaotic interaction
        cross_dim_chaos = np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * 
                                np.cos(x_norm[:-1] + x_norm[1:]) * 
                                (1 + 0.25 * np.sin(3 * x_norm[:-1])) * 
                                (1 + 0.2 * np.cos(5 * x_norm[1:])))
        
        # Multi-scale fractal-like structure
        fractal_structure = np.sum(np.exp(-np.abs(x_norm) / (0.1 + 0.1 * np.sin(9 * x_norm))) * 
                                  (1 + 0.3 * np.cos(7 * x_norm)))
        
        # Power-law conditioned regions with exponential scaling
        power_law_scaling = np.sum(np.abs(x_norm)**1.7 * (1 + 0.5 * np.sin(11 * x_norm)) * 
                                  np.exp(-0.2 * x_norm**2))
        
        # Chaotic gradient modulation
        gradient_mod = np.sum(np.sin(4 * x_norm) * np.cos(6 * x_norm) * 
                             (1 + 0.3 * np.sin(9 * x_norm)) * 
                             (1 + 0.25 * np.cos(8 * x_norm)))
        
        # Combined landscape with chaotic and multi-scale features
        return 2.0 * (radial_basins + sinusoidal_mod + saddle_points + 
                     cross_dim_chaos + fractal_structure + power_law_scaling + 
                     gradient_mod)