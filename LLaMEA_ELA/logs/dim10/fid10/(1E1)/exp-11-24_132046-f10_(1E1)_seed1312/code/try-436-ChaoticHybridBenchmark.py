import numpy as np

class ChaoticHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basin structure with chaotic modulation
        radial_basins = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm)) * 
                              np.exp(-0.5 * (x_norm**2)))
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sinusoidal_mod = np.sum(np.sin(2 * np.pi * x_norm) * 
                               np.cos(3 * np.pi * x_norm) * 
                               (1 + 0.3 * np.sin(5 * np.pi * x_norm)))
        
        # Asymmetric saddle points with chaotic perturbations
        saddle_points = np.sum(np.abs(x_norm) * np.sin(4 * x_norm) * 
                              (1 + 0.2 * np.cos(7 * x_norm)) * 
                              np.exp(-0.1 * np.abs(x_norm)))
        
        # Multi-scale chaotic attractor structure
        chaotic_attractor = np.sum(np.sin(8 * x_norm) * 
                                  np.cos(6 * x_norm) * 
                                  np.exp(-0.2 * (x_norm**2 + 0.5 * np.sin(9 * x_norm))))
        
        # Cross-dimensional coupling with exponential interaction
        cross_coupling = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / 
                                     (0.1 + 0.1 * np.cos(3 * x_norm[:-1]))))
        
        # Power-law scaling with logarithmic perturbations
        power_scaling = np.sum((np.abs(x_norm)**1.5) * 
                              (1 + 0.2 * np.log(1 + np.abs(x_norm))))
        
        # Combined landscape with chaotic mixing
        return 2.0 * (radial_basins + sinusoidal_mod + saddle_points + 
                     chaotic_attractor + cross_coupling + power_scaling)