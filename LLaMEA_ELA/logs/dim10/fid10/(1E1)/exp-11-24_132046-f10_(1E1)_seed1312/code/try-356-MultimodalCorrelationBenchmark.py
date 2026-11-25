import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic periodic peaks with fractional scaling
        chaotic_peaks = np.sum(3.0 * np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) + 
                              2.0 * np.sin(8 * np.pi * x_norm) * np.cos(10 * np.pi * x_norm) +
                              1.5 * np.sin(12 * np.pi * x_norm) * np.cos(14 * np.pi * x_norm))
        
        # Fractional Brownian motion inspired valleys
        fbm_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.7 * np.sin(3 * np.pi * x_norm)**2)))
        
        # Cross-dimensional chaotic correlation with memory effects
        cross_dim_corr = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               (1 + 0.4 * np.sin(5 * np.pi * x_norm[:-1])) * 
                               (1 + 0.3 * np.cos(7 * np.pi * x_norm[1:])) *
                               np.exp(-0.1 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Multi-scale fractal modulation with power-law exponents
        fractal_modulation = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm) * 
                                   (1 + 0.3 * np.sin(9 * x_norm)) * 
                                   (1 + 0.25 * np.cos(6 * x_norm)) *
                                   np.exp(-0.2 * np.abs(x_norm)**1.7))
        
        # Power-law conditioned regions with adaptive scaling
        power_law_regions = np.sum(np.abs(x_norm)**1.8 * (1 + 0.5 * np.sin(15 * x_norm)) *
                                  (1 + 0.3 * np.cos(10 * x_norm)))
        
        # Memory-dependent chaotic interaction terms
        memory_interaction = np.sum((1 + 0.6 * np.sin(4 * x_norm)) * 
                                   np.exp(-0.4 * x_norm**2) * 
                                   (1 + 0.4 * np.cos(5 * x_norm)) *
                                   np.sin(2 * np.pi * x_norm[:-1]) * 
                                   np.cos(2 * np.pi * x_norm[1:]))
        
        # Adaptive conditioning with dynamic curvature
        adaptive_conditioning = np.sum((1 + 0.7 * np.sin(3 * x_norm)) * 
                                     np.exp(-0.2 * x_norm**2) * 
                                     (1 + 0.5 * np.cos(4 * x_norm)) *
                                     np.exp(-0.1 * np.abs(x_norm)**1.5))
        
        # Combined landscape with enhanced complexity
        return 2.0 * (chaotic_peaks + fbm_valleys + cross_dim_corr + 
                     fractal_modulation + power_law_regions + memory_interaction + 
                     adaptive_conditioning)