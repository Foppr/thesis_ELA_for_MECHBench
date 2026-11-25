import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic phase interaction peaks with fractional dimensions
        chaotic_peaks = np.sum(np.sin(13 * np.pi * x_norm) * np.cos(17 * np.pi * x_norm) * 
                              np.exp(-0.5 * (x_norm**2)) * 
                              (1 + 0.6 * np.sin(23 * np.pi * x_norm)))
        
        # Fractional dimensional Gaussian valleys with power-law scaling
        fractional_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.7 * np.abs(x_norm)**0.7)) * 
                                  (1 + 0.4 * np.cos(11 * np.pi * x_norm)))
        
        # Adaptive ridge structures with non-smooth transitions
        adaptive_ridges = np.sum(np.abs(x_norm)**1.7 * np.sin(9 * np.pi * x_norm) * 
                               (1 + 0.5 * np.cos(15 * np.pi * x_norm)) * 
                               (1 + 0.3 * np.sin(7 * np.pi * x_norm)))
        
        # Cross-dimensional fractional correlation with long-range interactions
        cross_dim_frac = np.sum(np.abs(x_norm[:-1] - x_norm[1:])**(0.3) * 
                               np.exp(-np.abs(x_norm[:-1] + x_norm[1:])**2) * 
                               (1 + 0.2 * np.sin(5 * np.pi * x_norm[:-1])) * 
                               (1 + 0.2 * np.cos(8 * np.pi * x_norm[1:])))
        
        # Multi-scale fractal modulation with discontinuous derivatives
        fractal_modulation = np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm) * 
                                  (1 + 0.3 * np.sin(25 * x_norm)) * 
                                  (1 + 0.4 * np.cos(18 * x_norm)) * 
                                  np.exp(-np.abs(x_norm)**0.8))
        
        # Power-law conditioned regions with sharp curvature changes
        power_law_curvature = np.sum(np.abs(x_norm)**2.1 * (1 + 0.5 * np.sin(30 * x_norm)) * 
                                   (1 + 0.3 * np.cos(22 * x_norm)))
        
        # Non-smooth chaotic correlation structure
        chaotic_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])**1.5) * 
                            (1 + 0.4 * np.sin(19 * np.pi * x_norm[:-1])) * 
                            (1 + 0.3 * np.cos(16 * np.pi * x_norm[1:])))
        
        # Adaptive conditioning with discontinuous scaling
        adaptive_conditioning = np.sum((1 + 0.7 * np.sin(3 * x_norm)) * 
                                     np.exp(-0.4 * np.abs(x_norm)**1.8) * 
                                     (1 + 0.4 * np.cos(5 * x_norm)) * 
                                     (1 + 0.2 * np.sin(13 * x_norm)))
        
        # Combined landscape with sharp transitions and non-smooth regions
        return 2.0 * (chaotic_peaks + fractional_valleys + adaptive_ridges + 
                     cross_dim_frac + fractal_modulation + power_law_curvature + 
                     chaotic_corr + adaptive_conditioning)