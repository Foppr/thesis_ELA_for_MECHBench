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
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_modulation = np.sum(np.sin(2 * np.pi * x_norm) * 
                               np.cos(3 * np.pi * x_norm) * 
                               (1 + 0.3 * np.sin(5 * np.pi * x_norm)))
        
        # Asymmetric saddle points with exponential scaling
        asymmetric_saddles = np.sum(np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                   (x_norm[:-1] - 0.5 * x_norm[1:])**2 * 
                                   (1 + 0.2 * np.cos(4 * np.pi * x_norm[:-1])))
        
        # Multi-scale chaotic structure with power-law interactions
        chaotic_structure = np.sum(np.abs(x_norm)**1.7 * 
                                  np.sin(8 * np.pi * x_norm) * 
                                  np.cos(6 * np.pi * x_norm))
        
        # Cross-dimensional coupling with nonlinear interaction
        cross_coupling = np.sum((x_norm[:-1]**2 + x_norm[1:]**2) * 
                               np.exp(-0.1 * (x_norm[:-1] - x_norm[1:])**2) * 
                               (1 + 0.4 * np.sin(3 * np.pi * (x_norm[:-1] + x_norm[1:]))))
        
        # Fractal-like irregularity with varying smoothness
        fractal_irregularity = np.sum(np.exp(-np.abs(x_norm)**0.7) * 
                                     np.sin(15 * x_norm) * 
                                     (1 + 0.3 * np.cos(12 * x_norm)))
        
        # Combined chaotic landscape
        return 2.0 * (radial_basins + sin_modulation + asymmetric_saddles + 
                     chaotic_structure + cross_coupling + fractal_irregularity)