import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic periodic peaks with dynamic amplitude modulation
        chaotic_peaks = np.sum(3.0 * np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * 
                              (1 + 0.5 * np.sin(10 * np.pi * x_norm)) * 
                              (1 + 0.3 * np.cos(8 * np.pi * x_norm)))
        
        # Gaussian valleys with fractal-like width variation
        gaussian_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.7 * np.sin(3 * np.pi * x_norm)**2)))
        
        # Cross-dimensional chaotic correlation with non-linear coupling
        cross_dim_corr = np.sum(np.sin(np.pi * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                               np.cos(np.pi * (x_norm[:-1]**3 - x_norm[1:]**3)) * 
                               (1 + 0.4 * np.sin(5 * np.pi * x_norm[:-1])) * 
                               (1 + 0.3 * np.cos(7 * np.pi * x_norm[1:])))
        
        # Multi-scale harmonic modulation with exponential decay
        harmonic_modulation = np.sum(np.sin(12 * x_norm) * np.cos(10 * x_norm) * 
                                    (1 + 0.3 * np.sin(9 * x_norm)) * 
                                    np.exp(-0.1 * np.abs(x_norm)))
        
        # Power-law conditioned regions with log-periodic fluctuations
        power_law_regions = np.sum(np.abs(x_norm)**1.7 * (1 + 0.5 * np.sin(15 * x_norm) * np.cos(13 * x_norm)))
        
        # Fractal-like correlation structure with recursive self-similarity
        fractal_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.2 + 0.3 * np.sin(6 * x_norm[:-1])**2)))
        
        # Adaptive conditioning with exponential scaling and chaotic perturbations
        adaptive_conditioning = np.sum((1 + 0.7 * np.sin(3 * x_norm)) * 
                                     np.exp(-0.5 * x_norm**2) * 
                                     (1 + 0.4 * np.cos(5 * x_norm)) * 
                                     np.sin(2 * np.pi * x_norm)**2)
        
        # Additional deceptive valley structure with irregular topology
        deceptive_valleys = np.sum(0.5 * np.sin(20 * x_norm) * np.exp(-0.2 * (x_norm - 1.0)**2))
        
        # Combined landscape with different curvature regions and sharp transitions
        return 2.0 * (chaotic_peaks + gaussian_valleys + cross_dim_corr + 
                     harmonic_modulation + power_law_regions + fractal_corr + 
                     adaptive_conditioning + deceptive_valleys)