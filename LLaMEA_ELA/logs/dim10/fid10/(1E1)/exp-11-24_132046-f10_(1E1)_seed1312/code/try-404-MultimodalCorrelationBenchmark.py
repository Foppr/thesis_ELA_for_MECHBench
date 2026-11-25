import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic phase interaction peaks with varying frequencies
        chaotic_peaks = np.sum(3.0 * np.sin(7 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) * 
                              np.sin(5 * np.pi * x_norm**2) * np.cos(3 * np.pi * x_norm**3))
        
        # Gaussian valleys with fractal-like width variation
        gaussian_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.7 * np.sin(8 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))))
        
        # Cross-dimensional correlation with chaotic coupling
        cross_dim_corr = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               (1 + 0.5 * np.sin(7 * np.pi * x_norm[:-1])) * 
                               (1 + 0.4 * np.cos(9 * np.pi * x_norm[1:])))
        
        # Multi-scale harmonic modulation with chaotic interference
        harmonic_modulation = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm) * 
                                    (1 + 0.3 * np.sin(14 * x_norm)) * 
                                    (1 + 0.25 * np.cos(16 * x_norm)))
        
        # Power-law conditioned regions with chaotic exponent modulation
        power_law_regions = np.sum(np.abs(x_norm)**1.7 * (1 + 0.5 * np.sin(15 * x_norm) * np.cos(13 * x_norm)))
        
        # Fractal-like correlation structure with chaotic scaling
        fractal_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.2 + 0.3 * np.sin(7 * np.pi * x_norm[:-1]) * np.cos(5 * np.pi * x_norm[1:]))))
        
        # Adaptive conditioning with chaotic local scaling
        adaptive_conditioning = np.sum((1 + 0.7 * np.sin(3 * x_norm)) * 
                                     np.exp(-0.4 * x_norm**2) * 
                                     (1 + 0.4 * np.cos(5 * x_norm)) * 
                                     (1 + 0.3 * np.sin(9 * x_norm)))
        
        # Additional chaotic noise component for increased ruggedness
        chaotic_noise = np.sum(0.5 * np.sin(20 * x_norm) * np.cos(18 * x_norm) * 
                              np.sin(16 * x_norm) * np.cos(14 * x_norm))
        
        # Combined landscape with different curvature regions and extreme variations
        return 2.0 * (chaotic_peaks + gaussian_valleys + cross_dim_corr + 
                     harmonic_modulation + power_law_regions + fractal_corr + 
                     adaptive_conditioning + chaotic_noise)