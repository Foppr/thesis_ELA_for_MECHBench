import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basin structure with chaotic perturbations
        radial_term = np.sum(x_norm**2 * (1 + 0.3 * np.sin(10 * np.sqrt(np.sum(x_norm**2)))))
        
        # Sinusoidal modulation with chaotic frequency variation
        freq_mod = np.sum(np.sin(2 * np.pi * x_norm * (1 + 0.1 * np.sin(5 * x_norm))) * 
                         np.cos(3 * np.pi * x_norm * (1 + 0.05 * np.cos(7 * x_norm))))
        
        # Asymmetric saddle points with varying curvature
        saddle_term = np.sum((x_norm**2 - 0.5 * np.sin(4 * np.pi * x_norm)) * 
                           (1 + 0.2 * np.cos(6 * np.pi * x_norm)) * 
                           np.exp(-0.1 * np.abs(x_norm)))
        
        # Cross-dimensional chaotic coupling
        cross_coupling = np.sum(np.sin(np.pi * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               (1 + 0.15 * np.sin(3 * np.pi * x_norm[:-1])))
        
        # Multi-scale chaotic oscillation
        chaotic_osc = np.sum(np.exp(-0.5 * (x_norm**2)) * 
                            (1 + 0.4 * np.sin(8 * x_norm) * np.cos(6 * x_norm)) * 
                            (1 + 0.3 * np.sin(12 * x_norm)))
        
        # Fractal-like irregularity
        fractal_irregularity = np.sum(np.abs(x_norm)**1.7 * 
                                    (1 + 0.25 * np.sin(9 * x_norm) * np.cos(5 * x_norm)))
        
        # Asymmetric conditioning with local scaling
        asymmetric_conditioning = np.sum((1 + 0.3 * np.sin(4 * x_norm)) * 
                                       np.exp(-0.2 * x_norm**2) * 
                                       (1 + 0.1 * np.cos(5 * x_norm)))
        
        # Combined chaotic landscape
        return 2.0 * (radial_term + freq_mod + saddle_term + cross_coupling + 
                     chaotic_osc + fractal_irregularity + asymmetric_conditioning)