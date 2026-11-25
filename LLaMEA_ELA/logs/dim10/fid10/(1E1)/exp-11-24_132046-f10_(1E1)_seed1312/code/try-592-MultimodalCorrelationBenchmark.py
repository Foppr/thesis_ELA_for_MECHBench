import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic periodic peaks with varying frequencies and amplitudes
        chaotic_peaks = np.sum(3.0 * np.sin(7 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) + 
                              2.0 * np.sin(5 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) + 
                              1.5 * np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Gaussian valleys with fractal-like width variations
        gaussian_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.7 * np.sin(4 * np.pi * x_norm)**2)))
        
        # Cross-dimensional chaotic correlation with non-linear interaction
        cross_dim_corr = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               (1 + 0.5 * np.sin(6 * np.pi * x_norm[:-1]) * np.cos(4 * np.pi * x_norm[1:])))
        
        # Multi-scale harmonic modulation with irregular frequencies
        harmonic_modulation = np.sum(np.sin(12 * x_norm) * np.cos(10 * x_norm) * 
                                    (1 + 0.3 * np.sin(8 * x_norm)) * 
                                    (1 + 0.25 * np.cos(6 * x_norm)))
        
        # Power-law conditioned regions with variable exponents
        power_law_regions = np.sum(np.abs(x_norm)**1.7 * (1 + 0.5 * np.sin(15 * x_norm)) * 
                                  (1 + 0.3 * np.cos(10 * x_norm)))
        
        # Fractal-like correlation structure with varying scaling
        fractal_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.2 + 0.3 * np.sin(7 * x_norm[:-1])**2)))
        
        # Adaptive conditioning with chaotic local scaling
        adaptive_conditioning = np.sum((1 + 0.7 * np.sin(3 * x_norm)) * 
                                     np.exp(-0.5 * x_norm**2) * 
                                     (1 + 0.4 * np.cos(5 * x_norm)) * 
                                     (1 + 0.3 * np.sin(8 * x_norm)))
        
        # Additional irregular basin structure
        basin_structure = np.sum(np.abs(x_norm)**2.5 * np.sin(13 * x_norm) * 
                                (1 + 0.2 * np.cos(9 * x_norm)) * 
                                (1 + 0.15 * np.sin(11 * x_norm)))
        
        # Combined landscape with extreme curvature variations
        return 2.0 * (chaotic_peaks + gaussian_valleys + cross_dim_corr + 
                     harmonic_modulation + power_law_regions + fractal_corr + 
                     adaptive_conditioning + basin_structure)