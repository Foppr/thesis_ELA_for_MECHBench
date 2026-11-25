import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic periodic peak structure with exponential modulation
        chaotic_peaks = np.sum(3.0 * np.exp(-np.abs(x_norm)) * np.sin(7 * np.pi * x_norm) * 
                              np.cos(5 * np.pi * x_norm) * (1 + 0.3 * np.sin(13 * x_norm)))
        
        # Multi-scale Gaussian valleys with dynamic widths
        gaussian_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.7 * np.cos(3 * np.pi * x_norm))) * 
                                 (1 + 0.2 * np.sin(9 * x_norm)))
        
        # Cross-dimensional chaotic correlation with non-linear coupling
        cross_dim_corr = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               np.exp(-0.5 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                               (1 + 0.4 * np.sin(6 * x_norm[:-1]) * np.cos(4 * x_norm[1:])))
        
        # Multi-harmonic modulation with frequency cascading
        harmonic_modulation = np.sum(np.sin(12 * x_norm) * np.cos(9 * x_norm) * 
                                    (1 + 0.3 * np.sin(8 * x_norm)) * 
                                    (1 + 0.25 * np.cos(7 * x_norm)) * 
                                    np.exp(-0.1 * np.abs(x_norm)))
        
        # Power-law conditioned regions with dynamic exponents
        power_law_regions = np.sum(np.abs(x_norm)**1.7 * (1 + 0.5 * np.sin(15 * x_norm)) * 
                                  np.exp(-0.2 * x_norm**2))
        
        # Fractal-like correlation structure with recursive scaling
        fractal_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.05 + 0.15 * np.cos(7 * x_norm[:-1]))))
        
        # Adaptive conditioning with dynamic local scaling
        adaptive_conditioning = np.sum((1 + 0.6 * np.sin(3 * x_norm)) * 
                                     np.exp(-0.4 * x_norm**2) * 
                                     (1 + 0.4 * np.cos(5 * x_norm)) * 
                                     np.exp(-0.1 * np.abs(x_norm)))
        
        # Additional chaotic saddle point structure
        saddle_points = np.sum(np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * 
                              (1 + 0.3 * np.sin(2 * x_norm)) * 
                              np.exp(-0.5 * np.abs(x_norm)))
        
        # Combined landscape with different curvature regions
        return 2.0 * (chaotic_peaks + gaussian_valleys + cross_dim_corr + 
                     harmonic_modulation + power_law_regions + fractal_corr + 
                     adaptive_conditioning + saddle_points)