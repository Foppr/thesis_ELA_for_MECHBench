import numpy as np

class HybridOscillatoryBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component with varying frequencies
        oscillations = np.sum(np.sin(8 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) + 
                             0.5 * np.sin(12 * np.pi * x_norm) * np.cos(10 * np.pi * x_norm))
        
        # Radial basin structure with varying depth
        radial_basins = np.sum((x_norm**2 + 0.1 * np.sin(4 * np.pi * x_norm)) * 
                              np.exp(-0.5 * (x_norm**2)))
        
        # Asymmetric saddle points with directional bias
        asymmetric_saddles = np.sum(np.abs(x_norm) * np.exp(-0.5 * (x_norm - 0.3)**2) + 
                                   0.8 * np.abs(x_norm) * np.exp(-0.5 * (x_norm + 0.4)**2))
        
        # Cross-dimensional interaction with directional coupling
        cross_dim_interaction = np.sum(np.sin(3 * np.pi * x_norm[:-1]) * 
                                      np.cos(3 * np.pi * x_norm[1:]) * 
                                      (1 + 0.3 * np.sin(2 * np.pi * x_norm[:-1])) * 
                                      (1 + 0.2 * np.cos(2 * np.pi * x_norm[1:])))
        
        # Multi-scale harmonic modulation with amplitude variation
        harmonic_modulation = np.sum(np.sin(5 * x_norm) * np.cos(7 * x_norm) * 
                                    (1 + 0.2 * np.sin(3 * x_norm)) * 
                                    (1 + 0.15 * np.cos(4 * x_norm)))
        
        # Power-law conditioned regions with non-uniform scaling
        power_law_conditioning = np.sum(np.abs(x_norm)**1.7 * (1 + 0.3 * np.sin(8 * x_norm)))
        
        # Combined landscape with different curvature characteristics
        return 2.0 * (oscillations + radial_basins + asymmetric_saddles + 
                     cross_dim_interaction + harmonic_modulation + power_law_conditioning)