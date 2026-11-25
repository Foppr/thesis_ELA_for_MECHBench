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
        
        # Sinusoidal modulation with chaotic phase interactions
        chaotic_modulation = np.sum(np.sin(20 * x_norm + np.sin(5 * x_norm)) * 
                                   np.cos(15 * x_norm + np.cos(7 * x_norm)))
        
        # Asymmetric saddle points with varying steepness
        asymmetric_saddles = np.sum((x_norm**4 - 2 * x_norm**2) * 
                                   (1 + 0.3 * np.sin(8 * x_norm)) * 
                                   np.exp(-0.1 * np.abs(x_norm)))
        
        # Multi-scale oscillatory structure with frequency mixing
        multi_scale_osc = np.sum(np.sin(5 * x_norm) * np.cos(3 * x_norm) * 
                                (1 + 0.2 * np.sin(12 * x_norm)) * 
                                (1 + 0.15 * np.cos(9 * x_norm)))
        
        # Power-law conditioned regions with fractal-like behavior
        power_law_conditioning = np.sum(np.abs(x_norm)**1.7 * 
                                       (1 + 0.3 * np.sin(25 * x_norm)) * 
                                       np.exp(-0.2 * x_norm**2))
        
        # Cross-dimensional coupling with non-linear interaction terms
        cross_dim_coupling = np.sum((x_norm[:-1]**2 + x_norm[1:]**2) * 
                                   np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                                   np.cos(np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Sharp transition regions with discontinuous curvature
        sharp_transitions = np.sum(0.5 * np.abs(x_norm) * 
                                 (1 + np.sin(30 * x_norm)) * 
                                 np.exp(-0.5 * np.abs(x_norm)))
        
        # Combined landscape with chaotic and structured components
        return 2.0 * (radial_basins + chaotic_modulation + asymmetric_saddles + 
                     multi_scale_osc + power_law_conditioning + cross_dim_coupling + 
                     sharp_transitions)