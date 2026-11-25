import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basin structure with varying depth
        radial_basins = np.sum((x_norm**2 + 0.1) * np.exp(-0.5 * (x_norm**2)))
        
        # Sinusoidal oscillation with chaotic modulation
        sin_oscillations = np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm) * 
                                 (1 + 0.3 * np.sin(15 * x_norm)) * 
                                 (1 + 0.2 * np.cos(12 * x_norm)))
        
        # Asymmetric saddle points with varying steepness
        asymmetric_saddles = np.sum(np.abs(x_norm)**1.7 * np.sin(3 * x_norm) * 
                                   np.cos(5 * x_norm) * 
                                   (1 + 0.4 * np.sin(8 * x_norm)))
        
        # Cross-dimensional interaction with chaotic coupling
        cross_coupling = np.sum(np.sin(np.pi * x_norm[:-1]) * np.cos(np.pi * x_norm[1:]) * 
                               (1 + 0.25 * np.sin(4 * np.pi * x_norm[:-1])) * 
                               (1 + 0.3 * np.cos(6 * np.pi * x_norm[1:])))
        
        # Multi-scale chaotic modulation
        chaotic_modulation = np.sum(np.sin(20 * x_norm) * np.cos(18 * x_norm) * 
                                   np.exp(-0.1 * np.abs(x_norm)) * 
                                   (1 + 0.3 * np.sin(25 * x_norm)))
        
        # Power-law conditioned regions with irregular scaling
        power_law_conditioning = np.sum(np.abs(x_norm)**1.5 * (1 + 0.3 * np.cos(10 * x_norm)) * 
                                       np.exp(-0.2 * x_norm**2))
        
        # Fractal-like structure with irregular spacing
        fractal_structure = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.05 + 0.05 * np.sin(3 * x_norm[:-1]))))
        
        # Combined landscape with chaotic curvature variation
        return 2.0 * (radial_basins + sin_oscillations + asymmetric_saddles + 
                     cross_coupling + chaotic_modulation + power_law_conditioning + 
                     fractal_structure)