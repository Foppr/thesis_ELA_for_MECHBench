import numpy as np

class ChaoticRadialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basin structure with chaotic modulation
        radial_basins = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm)) * 
                              np.exp(-0.5 * np.sum(x_norm**2, axis=0)))
        
        # Sinusoidal modulated saddle points with asymmetric curvature
        saddle_points = np.sum(np.sin(3 * x_norm) * np.cos(5 * x_norm) * 
                              (1 + 0.3 * np.sin(7 * x_norm)) * 
                              (1 - 0.2 * np.cos(4 * x_norm)))
        
        # Chaotic cross-dimensional interactions
        chaotic_corr = np.sum(np.sin(np.pi * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                             np.cos(np.pi * (x_norm[:-1] * x_norm[1:])) * 
                             (1 + 0.25 * np.sin(6 * x_norm[:-1])) * 
                             (1 + 0.15 * np.cos(8 * x_norm[1:])))
        
        # Asymmetric Gaussian-like valleys with position-dependent scaling
        asymmetric_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.7 * np.abs(x_norm))) * 
                                   (1 + 0.4 * np.sin(2 * x_norm)) * 
                                   (1 - 0.3 * np.cos(3 * x_norm)))
        
        # Multi-scale harmonic interference
        harmonic_interference = np.sum(np.sin(8 * x_norm) * np.cos(6 * x_norm) * 
                                     np.exp(-0.1 * np.abs(x_norm)) * 
                                     (1 + 0.2 * np.sin(4 * x_norm)))
        
        # Power-law conditioned regions with exponential scaling
        power_law_scaling = np.sum(np.abs(x_norm)**1.7 * np.exp(-0.5 * x_norm**2) * 
                                  (1 + 0.3 * np.cos(9 * x_norm)))
        
        # Fractal-like radial structure with varying density
        fractal_radial = np.sum(np.exp(-np.abs(x_norm) / (0.2 + 0.8 * np.sin(5 * x_norm))) * 
                               (1 + 0.3 * np.cos(3 * x_norm)) * 
                               (1 - 0.2 * np.sin(7 * x_norm)))
        
        # Combined chaotic landscape
        return 2.0 * (radial_basins + saddle_points + chaotic_corr + 
                     asymmetric_valleys + harmonic_interference + power_law_scaling + 
                     fractal_radial)