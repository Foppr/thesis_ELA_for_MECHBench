import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basins with varying depths and widths
        radial_basins = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm)) * 
                              np.exp(-0.5 * (x_norm**2) / (0.3 + 0.2 * np.cos(3 * x_norm))))
        
        # Sinusoidal modulations with chaotic phase interactions
        chaotic_modulation = np.sum(np.sin(8 * x_norm + np.sin(5 * x_norm)) * 
                                   np.cos(6 * x_norm + np.cos(4 * x_norm)) * 
                                   (1 + 0.3 * np.sin(2 * x_norm)))
        
        # Asymmetric saddle points with varying steepness
        saddle_points = np.sum(np.tanh(3 * x_norm) * np.exp(-0.5 * x_norm**2) * 
                              (1 + 0.4 * np.sin(7 * x_norm)) * 
                              (1 - 0.2 * np.cos(9 * x_norm)))
        
        # Cross-dimensional coupling with exponential interaction
        cross_coupling = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.2 + 0.1 * np.sin(6 * x_norm[:-1]))))
        
        # Multi-scale chaotic oscillations
        multi_scale_osc = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm) * 
                                (1 + 0.2 * np.sin(10 * x_norm)) * 
                                (1 + 0.15 * np.cos(8 * x_norm)))
        
        # Power-law conditioned regions with varying exponents
        power_law = np.sum(np.abs(x_norm)**1.7 * (1 + 0.3 * np.sin(11 * x_norm)) * 
                          (1 + 0.25 * np.cos(9 * x_norm)))
        
        # Fractal-like structure with recursive scaling
        fractal_structure = np.sum(np.exp(-np.abs(x_norm)**0.7) * 
                                  (1 + 0.3 * np.sin(4 * x_norm)) * 
                                  (1 + 0.2 * np.cos(6 * x_norm)))
        
        # Combined chaotic landscape with multiple competing forces
        return 2.0 * (radial_basins + chaotic_modulation + saddle_points + 
                     cross_coupling + multi_scale_osc + power_law + fractal_structure)