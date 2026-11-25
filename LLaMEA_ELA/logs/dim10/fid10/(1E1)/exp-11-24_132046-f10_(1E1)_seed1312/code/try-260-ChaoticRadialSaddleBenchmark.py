import numpy as np

class ChaoticRadialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basin structure with chaotic modulation
        radial_basin = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm)) * 
                             np.exp(-0.5 * np.sum(x_norm**2, axis=0)))
        
        # Sinusoidal modulation with chaotic phase shifts
        sinusoidal_mod = np.sum(np.sin(8 * x_norm) * np.cos(6 * x_norm) * 
                               (1 + 0.3 * np.sin(15 * x_norm)) * 
                               (1 + 0.2 * np.cos(12 * x_norm)))
        
        # Asymmetric saddle points with varying curvature
        saddle_points = np.sum((x_norm**4 - 2 * x_norm**2) * 
                              (1 + 0.2 * np.sin(5 * x_norm)) * 
                              (1 + 0.15 * np.cos(7 * x_norm)))
        
        # Cross-dimensional chaotic interaction
        cross_dim_interaction = np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * 
                                     np.cos(x_norm[:-1] + x_norm[1:]) * 
                                     (1 + 0.25 * np.sin(3 * x_norm[:-1])) * 
                                     (1 + 0.2 * np.cos(4 * x_norm[1:])))
        
        # Power-law conditioned regions with exponential scaling
        power_law_conditioning = np.sum(np.abs(x_norm)**1.7 * 
                                       np.exp(-0.3 * np.abs(x_norm)) * 
                                       (1 + 0.3 * np.sin(9 * x_norm)))
        
        # Fractal-like chaotic structure
        fractal_structure = np.sum(np.exp(-np.abs(x_norm) / (0.1 + 0.1 * np.cos(8 * x_norm))) * 
                                 np.sin(5 * x_norm) * np.cos(3 * x_norm))
        
        # Combined landscape with varying conditioning and chaotic behavior
        return 2.0 * (radial_basin + sinusoidal_mod + saddle_points + 
                     cross_dim_interaction + power_law_conditioning + fractal_structure)