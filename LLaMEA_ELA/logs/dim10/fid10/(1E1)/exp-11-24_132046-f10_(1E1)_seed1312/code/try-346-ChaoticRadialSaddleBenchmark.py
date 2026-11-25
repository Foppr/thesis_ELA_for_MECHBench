import numpy as np

class ChaoticRadialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basin structure with chaotic depth modulation
        radial_basins = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm)) * 
                              np.exp(-0.5 * (x_norm**2)))
        
        # Sinusoidal modulation with chaotic frequency and amplitude
        chaotic_modulation = np.sum(np.sin(5 * x_norm + np.sin(3 * x_norm)) * 
                                   np.cos(7 * x_norm + np.cos(4 * x_norm)) * 
                                   (1 + 0.3 * np.sin(2 * x_norm)))
        
        # Asymmetric saddle points with varying steepness
        asymmetric_saddles = np.sum(np.abs(x_norm) * np.exp(-0.5 * x_norm**2) * 
                                   (1 + 0.4 * np.cos(6 * x_norm)) * 
                                   (1 - 0.3 * np.sin(8 * x_norm)))
        
        # Multi-scale harmonic interference
        interference = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm) * 
                             np.exp(-0.1 * np.abs(x_norm)) * 
                             (1 + 0.2 * np.sin(9 * x_norm)))
        
        # Fractal-like irregularity in curvature
        fractal_irregularity = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / 
                                           (0.05 + 0.05 * np.sin(7 * x_norm[:-1]))))
        
        # Local conditioning with chaotic scaling
        local_conditioning = np.sum((1 + 0.5 * np.sin(4 * x_norm)) * 
                                   np.exp(-0.2 * x_norm**2) * 
                                   (1 + 0.3 * np.cos(5 * x_norm)))
        
        # Cross-dimensional coupling with chaotic interaction
        cross_coupling = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               (1 + 0.2 * np.sin(3 * x_norm[:-1])) * 
                               (1 + 0.25 * np.cos(4 * x_norm[1:])))
        
        # Combined chaotic landscape
        return 2.0 * (radial_basins + chaotic_modulation + asymmetric_saddles + 
                     interference + fractal_irregularity + local_conditioning + 
                     cross_coupling)