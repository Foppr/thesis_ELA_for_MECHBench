import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic periodic peaks with amplitude modulation
        chaotic_peaks = np.sum(3.0 * np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * 
                              (1 + 0.3 * np.sin(10 * np.pi * x_norm)) * 
                              (1 + 0.2 * np.cos(8 * np.pi * x_norm)))
        
        # Adaptive Gaussian valleys with multi-scale widths
        gaussian_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.7 * np.sin(3 * np.pi * x_norm)**2)))
        
        # Cross-dimensional chaotic correlation with varying coupling strengths
        cross_dim_corr = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               (1 + 0.4 * np.sin(5 * np.pi * x_norm[:-1])) * 
                               (1 + 0.3 * np.cos(7 * np.pi * x_norm[1:])) * 
                               np.exp(-0.1 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Multi-scale harmonic modulation with frequency coupling
        harmonic_modulation = np.sum(np.sin(12 * x_norm) * np.cos(10 * x_norm) * 
                                    (1 + 0.3 * np.sin(9 * x_norm)) * 
                                    (1 + 0.25 * np.cos(7 * x_norm)) * 
                                    (1 + 0.2 * np.sin(5 * x_norm)))
        
        # Power-law conditioned regions with dynamic exponents
        power_law_regions = np.sum(np.abs(x_norm)**1.7 * (1 + 0.5 * np.sin(15 * x_norm)) * 
                                  (1 + 0.3 * np.cos(12 * x_norm)))
        
        # Fractal-like correlation structure with variable dimensionality
        fractal_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.05 + 0.15 * np.sin(4 * np.pi * x_norm[:-1])**2)))
        
        # Adaptive conditioning with dynamic scaling factors
        adaptive_conditioning = np.sum((1 + 0.6 * np.sin(3 * x_norm)) * 
                                     np.exp(-0.4 * x_norm**2) * 
                                     (1 + 0.4 * np.cos(5 * x_norm)) * 
                                     (1 + 0.2 * np.sin(7 * x_norm)))
        
        # Additional chaotic cross-term interactions
        cross_terms = np.sum(np.sin(2 * np.pi * x_norm[:-1]) * np.cos(3 * np.pi * x_norm[1:]) * 
                            np.exp(-0.2 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                            (1 + 0.3 * np.sin(4 * np.pi * x_norm[:-1])))
        
        # Combined landscape with enhanced complexity and varied curvature
        return 2.0 * (chaotic_peaks + gaussian_valleys + cross_dim_corr + 
                     harmonic_modulation + power_law_regions + fractal_corr + 
                     adaptive_conditioning + cross_terms)