import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basin structure with chaotic modulation
        radial_basins = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm)) * 
                              np.exp(-0.5 * (x_norm**2)))
        
        # Sinusoidal landscape with varying frequencies and amplitudes
        sinusoidal_structure = np.sum(np.sin(2 * np.pi * x_norm) * 
                                    np.cos(3 * np.pi * x_norm) * 
                                    (1 + 0.3 * np.sin(5 * np.pi * x_norm)))
        
        # Asymmetric saddle points with chaotic perturbations
        saddle_points = np.sum(np.tanh(x_norm) * 
                             (x_norm**2 - 1) * 
                             (1 + 0.2 * np.cos(7 * x_norm)) * 
                             np.exp(-0.1 * np.abs(x_norm)))
        
        # Multi-scale chaotic modulation
        chaotic_modulation = np.sum(np.sin(np.pi * x_norm) * 
                                  np.cos(np.pi * x_norm) * 
                                  np.sin(2 * np.pi * x_norm) * 
                                  (1 + 0.15 * np.sin(9 * x_norm)))
        
        # Cross-dimensional coupling with exponential decay
        cross_dim_coupling = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * 
                                  (1 + 0.2 * np.cos(4 * np.pi * x_norm[:-1])) * 
                                  (1 + 0.15 * np.sin(3 * np.pi * x_norm[1:])))
        
        # Power-law scaling with logarithmic perturbations
        power_law_scaling = np.sum(np.abs(x_norm)**1.7 * 
                                 (1 + 0.25 * np.log(1 + np.abs(x_norm))))
        
        # Fractal-like irregularity in the landscape
        fractal_irregularity = np.sum(np.sin(10 * x_norm) * 
                                    np.cos(8 * x_norm) * 
                                    np.exp(-0.5 * (x_norm**2)) * 
                                    (1 + 0.3 * np.sin(6 * x_norm)))
        
        # Combined chaotic landscape
        return 2.0 * (radial_basins + sinusoidal_structure + saddle_points + 
                     chaotic_modulation + cross_dim_coupling + power_law_scaling + 
                     fractal_irregularity)