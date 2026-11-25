import numpy as np

class ChaoticRadialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basin structure with chaotic modulation
        radial_basins = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm)) * 
                              np.exp(-0.5 * (x_norm**2)))
        
        # Sinusoidal modulations creating chaotic peaks and valleys
        chaotic_modulation = np.sum(np.sin(7 * x_norm) * np.cos(5 * x_norm) * 
                                   (1 + 0.3 * np.sin(3 * x_norm)) * 
                                   (1 + 0.2 * np.cos(4 * x_norm)))
        
        # Asymmetric saddle points with varying curvature
        asymmetric_saddles = np.sum((x_norm**3 - 0.5 * x_norm**2) * 
                                   np.exp(-0.1 * np.abs(x_norm)) * 
                                   (1 + 0.4 * np.sin(6 * x_norm)))
        
        # Multi-scale harmonic interference
        harmonic_interference = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm) * 
                                     np.exp(-0.05 * x_norm**2) * 
                                     (1 + 0.1 * np.sin(9 * x_norm)))
        
        # Cross-dimensional coupling with chaotic interaction
        cross_dim_coupling = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                                   np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                   np.exp(-0.2 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Power-law conditioned regions with irregular scaling
        power_law_conditioning = np.sum(np.abs(x_norm)**1.7 * 
                                       (1 + 0.3 * np.sin(8 * x_norm)) * 
                                       np.exp(-0.1 * x_norm**2))
        
        # Fractal-like ridge structure with irregular peaks
        fractal_ridges = np.sum(np.exp(-np.abs(x_norm) / (0.2 + 0.1 * np.cos(7 * x_norm))) * 
                               np.sin(4 * x_norm) * 
                               (1 + 0.25 * np.sin(5 * x_norm)))
        
        # Combined landscape with mixed curvature and chaotic behavior
        return 2.0 * (radial_basins + chaotic_modulation + asymmetric_saddles + 
                     harmonic_interference + cross_dim_coupling + power_law_conditioning + 
                     fractal_ridges)