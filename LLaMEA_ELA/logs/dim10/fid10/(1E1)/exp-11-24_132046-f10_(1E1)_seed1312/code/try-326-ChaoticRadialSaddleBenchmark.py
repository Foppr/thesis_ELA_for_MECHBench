import numpy as np

class ChaoticRadialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basin structure with multiple local minima
        radial_basins = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm)) * 
                              np.exp(-0.5 * (x_norm**2)))
        
        # Sinusoidal modulation creating chaotic terrain
        chaotic_terrain = np.sum(np.sin(8 * x_norm) * np.cos(6 * x_norm) * 
                                np.exp(-0.1 * np.abs(x_norm)) * 
                                (1 + 0.3 * np.sin(4 * x_norm)))
        
        # Asymmetric saddle points with varying curvature
        asymmetric_saddles = np.sum((x_norm**4 - 2 * x_norm**2) * 
                                   (1 + 0.2 * np.cos(5 * x_norm)) * 
                                   np.exp(-0.3 * x_norm**2))
        
        # Cross-dimensional coupling with chaotic interaction
        cross_coupling = np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * 
                               np.cos(x_norm[:-1] + x_norm[1:]) * 
                               (1 + 0.1 * np.sin(3 * x_norm[:-1])) * 
                               (1 + 0.1 * np.cos(2 * x_norm[1:])))
        
        # Multi-scale oscillatory structure
        multi_scale = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm) * 
                            (1 + 0.2 * np.sin(8 * x_norm)) * 
                            (1 + 0.15 * np.cos(6 * x_norm)))
        
        # Fractal-like ridge structure
        fractal_ridges = np.sum(np.exp(-np.abs(x_norm) / (0.1 + 0.1 * np.cos(7 * x_norm))) * 
                               np.sin(5 * x_norm))
        
        # Local conditioning with varying steepness
        local_conditioning = np.sum((1 + 0.4 * np.sin(3 * x_norm)) * 
                                  np.exp(-0.2 * x_norm**2) * 
                                  (x_norm**2 + 0.5 * np.cos(4 * x_norm)))
        
        # Combined landscape
        return 2.0 * (radial_basins + chaotic_terrain + asymmetric_saddles + 
                     cross_coupling + multi_scale + fractal_ridges + 
                     local_conditioning)