import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Highly chaotic periodic structure with irregular peaks
        chaotic_peaks = np.sum(3.0 * np.sin(7 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) + 
                              2.0 * np.sin(13 * np.pi * x_norm) * np.cos(17 * np.pi * x_norm) + 
                              1.5 * np.sin(19 * np.pi * x_norm) * np.cos(23 * np.pi * x_norm))
        
        # Multi-scale Gaussian valleys with varying widths and heights
        gaussian_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.2 + 0.8 * np.sin(4 * np.pi * x_norm)**2)) + 
                                 0.5 * np.exp(-0.3 * (x_norm**2) / (0.1 + 0.9 * np.cos(6 * np.pi * x_norm)**2)))
        
        # Complex cross-dimensional correlation with non-linear interactions
        cross_dim_corr = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               (1 + 0.5 * np.sin(8 * np.pi * x_norm[:-1])) * 
                               (1 + 0.4 * np.cos(7 * np.pi * x_norm[1:])) * 
                               np.exp(-0.1 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Multi-harmonic modulation with fractal-like frequency variations
        harmonic_modulation = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm) * 
                                    (1 + 0.3 * np.sin(9 * x_norm)) * 
                                    (1 + 0.25 * np.cos(7 * x_norm)) * 
                                    (1 + 0.2 * np.sin(5 * x_norm)))
        
        # Power-law conditioned regions with irregular scaling
        power_law_regions = np.sum(np.abs(x_norm)**1.7 * (1 + 0.5 * np.sin(15 * x_norm)) * 
                                  (1 + 0.3 * np.cos(13 * x_norm)))
        
        # Fractal-like correlation structure with irregular spacing
        fractal_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.05 + 0.2 * np.sin(8 * np.pi * x_norm[:-1])**2)))
        
        # Adaptive conditioning with extreme local scaling variations
        adaptive_conditioning = np.sum((1 + 0.8 * np.sin(3 * x_norm)) * 
                                     np.exp(-0.5 * x_norm**2) * 
                                     (1 + 0.4 * np.cos(5 * x_norm)) * 
                                     (1 + 0.6 * np.sin(9 * x_norm)**2))
        
        # Additional chaotic interference terms
        chaos_interference = np.sum(0.7 * np.sin(25 * x_norm) * np.cos(22 * x_norm) * 
                                  np.exp(-0.2 * np.abs(x_norm)))
        
        # Combined landscape with extreme conditioning variations
        return 2.0 * (chaotic_peaks + gaussian_valleys + cross_dim_corr + 
                     harmonic_modulation + power_law_regions + fractal_corr + 
                     adaptive_conditioning + chaos_interference)