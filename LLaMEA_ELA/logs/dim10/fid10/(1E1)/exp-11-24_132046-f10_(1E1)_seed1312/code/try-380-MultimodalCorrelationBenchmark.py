import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Modified periodic peak structure with altered amplitudes and frequencies
        periodic_peaks = np.sum(2.5 * np.cos(3.5 * np.pi * x_norm) * np.sin(5.5 * np.pi * x_norm) + 
                               1.8 * np.cos(7.2 * np.pi * x_norm) * np.sin(9.3 * np.pi * x_norm))
        
        # Adjusted Gaussian valley structure with modified width and scaling
        gaussian_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.4 + 0.6 * np.sin(2.1 * np.pi * x_norm))))
        
        # Modified cross-dimensional correlation with enhanced chaotic interaction
        cross_dim_corr = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               (1 + 0.4 * np.sin(4.2 * np.pi * x_norm[:-1])) * 
                               (1 + 0.25 * np.cos(3.1 * np.pi * x_norm[1:])))
        
        # Modified multi-scale harmonic modulation
        harmonic_modulation = np.sum(np.sin(10.5 * x_norm) * np.cos(8.2 * x_norm) * 
                                    (1 + 0.3 * np.sin(6.1 * x_norm)) * 
                                    (1 + 0.25 * np.cos(4.3 * x_norm)))
        
        # Adjusted power-law conditioned regions
        power_law_regions = np.sum(np.abs(x_norm)**1.4 * (1 + 0.5 * np.sin(12.1 * x_norm)))
        
        # Modified fractal-like correlation structure
        fractal_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.12 + 0.08 * np.cos(5.2 * x_norm[:-1]))))
        
        # Modified adaptive conditioning with local scaling
        adaptive_conditioning = np.sum((1 + 0.6 * np.sin(2.1 * x_norm)) * 
                                     np.exp(-0.35 * x_norm**2) * 
                                     (1 + 0.35 * np.cos(3.2 * x_norm)))
        
        # Combined landscape with different curvature regions
        return 1.6 * (periodic_peaks + gaussian_valleys + cross_dim_corr + 
                     harmonic_modulation + power_law_regions + fractal_corr + 
                     adaptive_conditioning)