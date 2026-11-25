import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic saddle structure with exponential repulsion
        chaotic_saddle = np.sum(np.exp(-np.abs(x_norm)) * np.sin(10 * x_norm) * 
                               (1 + 0.3 * np.cos(15 * x_norm)))
        
        # Embedded fractal basins with self-similar minima
        fractal_basins = np.sum(np.sin(np.pi * x_norm)**2 * 
                               np.exp(-0.5 * (x_norm**2)) * 
                               (1 + 0.2 * np.sin(8 * np.pi * x_norm)))
        
        # Adaptive conditioning with dynamic curvature
        adaptive_conditioning = np.sum((1 + 0.4 * np.sin(5 * x_norm)) * 
                                     (1 + 0.3 * np.cos(7 * x_norm)) * 
                                     np.exp(-0.2 * x_norm**2))
        
        # Cross-dimensional coupling with nonlinear interaction
        cross_coupling = np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * 
                               np.cos(x_norm[:-1] + x_norm[1:]) * 
                               (1 + 0.25 * np.sin(3 * (x_norm[:-1] - x_norm[1:]))))
        
        # Multi-scale chaotic modulation
        chaotic_modulation = np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm) * 
                                  np.exp(-0.1 * np.abs(x_norm)) * 
                                  (1 + 0.1 * np.sin(25 * x_norm)))
        
        # Stable fixed points with varying basin sizes
        fixed_points = np.sum(np.exp(-0.5 * (x_norm - np.sin(x_norm))**2) * 
                            (1 + 0.3 * np.cos(4 * x_norm)))
        
        # Power-law conditioned regions with varying difficulty
        power_law_regions = np.sum(np.abs(x_norm)**1.7 * (1 + 0.5 * np.sin(12 * x_norm)) * 
                                 np.exp(-0.3 * x_norm**2))
        
        # Combined landscape with chaotic saddle points and multiple local minima
        return 2.0 * (chaotic_saddle + fractal_basins + adaptive_conditioning + 
                     cross_coupling + chaotic_modulation + fixed_points + 
                     power_law_regions)