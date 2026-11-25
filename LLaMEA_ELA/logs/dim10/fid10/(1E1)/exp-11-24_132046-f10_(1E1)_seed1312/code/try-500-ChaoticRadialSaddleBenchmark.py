import numpy as np

class ChaoticRadialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basin structure with chaotic perturbations
        radial_basin = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm)) * 
                             np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sinusoidal_mod = np.sum(np.sin(2 * np.pi * x_norm) * 
                               np.cos(3 * np.pi * x_norm) * 
                               (1 + 0.3 * np.sin(5 * np.pi * x_norm)))
        
        # Asymmetric saddle points with chaotic interactions
        saddle_points = np.sum((x_norm**2 - 1)**2 * 
                              (1 + 0.2 * np.cos(4 * np.pi * x_norm)) * 
                              np.exp(-0.1 * np.abs(x_norm)))
        
        # Multi-scale chaotic oscillations
        chaotic_oscillations = np.sum(np.sin(15 * x_norm) * 
                                     np.cos(7 * x_norm) * 
                                     np.exp(-0.05 * x_norm**2) * 
                                     (1 + 0.1 * np.sin(12 * x_norm)))
        
        # Cross-dimensional coupling with non-linear interaction
        cross_dim_interaction = np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                                      (1 + 0.3 * np.sin(6 * np.pi * x_norm[:-1])) * 
                                      (1 + 0.2 * np.cos(5 * np.pi * x_norm[1:])))
        
        # Power-law conditioned regions with irregular scaling
        power_law_scaling = np.sum(np.abs(x_norm)**1.7 * 
                                  (1 + 0.25 * np.sin(8 * x_norm)) * 
                                  np.exp(-0.3 * np.abs(x_norm)))
        
        # Combined chaotic landscape with mixed curvature and conditioning
        return 2.0 * (radial_basin + sinusoidal_mod + saddle_points + 
                     chaotic_oscillations + cross_dim_interaction + power_law_scaling)