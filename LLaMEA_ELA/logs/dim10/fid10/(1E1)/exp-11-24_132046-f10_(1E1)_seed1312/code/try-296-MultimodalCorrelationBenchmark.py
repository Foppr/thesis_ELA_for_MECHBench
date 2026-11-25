import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic periodic structure with multiple frequencies
        chaotic_peaks = np.sum(3.0 * np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) + 
                              2.0 * np.sin(8 * np.pi * x_norm) * np.cos(10 * np.pi * x_norm) + 
                              1.5 * np.sin(12 * np.pi * x_norm) * np.cos(14 * np.pi * x_norm))
        
        # Multi-scale Gaussian valleys with dynamic widths
        gaussian_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.7 * np.sin(3 * np.pi * x_norm)**2)))
        
        # Stronger cross-dimensional correlation with exponential interaction
        cross_dim_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.05 + 0.15 * np.sin(4 * np.pi * x_norm[:-1])**2)) * 
                               np.cos(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               (1 + 0.4 * np.sin(5 * np.pi * x_norm[:-1]) * np.cos(3 * np.pi * x_norm[1:])))
        
        # Complex harmonic modulation with varying amplitudes
        harmonic_modulation = np.sum(np.sin(12 * x_norm) * np.cos(9 * x_norm) * 
                                    (1 + 0.3 * np.sin(7 * x_norm)) * 
                                    (1 + 0.25 * np.cos(5 * x_norm)) * 
                                    (1 + 0.2 * np.sin(3 * x_norm)))
        
        # Power-law conditioned regions with adaptive exponents
        power_law_regions = np.sum(np.abs(x_norm)**1.7 * (1 + 0.5 * np.sin(15 * x_norm)) * 
                                  (1 + 0.3 * np.cos(8 * x_norm)))
        
        # Fractal-like correlation with varying scale factors
        fractal_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.08 + 0.2 * np.sin(6 * np.pi * x_norm[:-1])**3)) * 
                             np.sin(2 * np.pi * (x_norm[:-1] + x_norm[1:])) * 
                             np.cos(2 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Enhanced adaptive conditioning with dynamic scaling
        adaptive_conditioning = np.sum((1 + 0.7 * np.sin(3 * x_norm)) * 
                                     np.exp(-0.4 * x_norm**2) * 
                                     (1 + 0.4 * np.cos(4 * x_norm)) * 
                                     (1 + 0.3 * np.sin(6 * x_norm)))
        
        # Additional interference terms for increased complexity
        interference_terms = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm) * 
                                  (1 + 0.5 * np.sin(4 * np.pi * x_norm)) * 
                                  (1 + 0.4 * np.cos(8 * np.pi * x_norm)))
        
        # Combined landscape with increased curvature and complexity
        return 2.0 * (chaotic_peaks + gaussian_valleys + cross_dim_corr + 
                     harmonic_modulation + power_law_regions + fractal_corr + 
                     adaptive_conditioning + interference_terms)