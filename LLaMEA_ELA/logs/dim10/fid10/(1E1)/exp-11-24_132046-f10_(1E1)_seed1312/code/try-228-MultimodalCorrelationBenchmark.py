import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic phase interaction peaks with non-linear coupling
        chaotic_peaks = np.sum(3.0 * np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * 
                              np.exp(-0.5 * (x_norm**2)) + 
                              2.0 * np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                              np.exp(-0.3 * (x_norm**2)))
        
        # Fractal-like Gaussian valleys with multi-scale variance
        fractal_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.1 + 0.9 * np.sin(8 * np.pi * x_norm)**2)) + 
                                0.5 * np.exp(-0.3 * (x_norm**2) / (0.2 + 0.8 * np.cos(5 * np.pi * x_norm)**2)))
        
        # Cross-dimensional chaotic correlation with phase wrapping
        cross_dim_chaos = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                                np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                np.exp(-0.2 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                                (1 + 0.4 * np.sin(3 * np.pi * x_norm[:-1]) * np.cos(4 * np.pi * x_norm[1:])))
        
        # Multi-scale harmonic modulation with adaptive frequency
        multi_harmonic = np.sum(np.sin(12 * x_norm) * np.cos(10 * x_norm) * 
                               (1 + 0.3 * np.sin(8 * x_norm)) * 
                               (1 + 0.25 * np.cos(6 * x_norm)) * 
                               np.exp(-0.1 * np.abs(x_norm)))
        
        # Power-law conditioned regions with extreme curvature
        extreme_conditioning = np.sum(np.abs(x_norm)**1.7 * (1 + 0.5 * np.sin(15 * x_norm)) * 
                                    (1 + 0.3 * np.cos(12 * x_norm)))
        
        # Fractal correlation with exponential decay
        fractal_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.05 + 0.95 * np.sin(7 * x_norm[:-1])**2)) * 
                             np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Adaptive conditioning with exponential scaling
        adaptive_scaling = np.sum((1 + 0.8 * np.sin(3 * x_norm)) * 
                                np.exp(-0.5 * x_norm**2) * 
                                (1 + 0.4 * np.cos(5 * x_norm)) * 
                                np.exp(-0.2 * np.abs(x_norm)))
        
        # Combined landscape with extreme curvature variations
        return 2.0 * (chaotic_peaks + fractal_valleys + cross_dim_chaos + 
                     multi_harmonic + extreme_conditioning + fractal_corr + 
                     adaptive_scaling)