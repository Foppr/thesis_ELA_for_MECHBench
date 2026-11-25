import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced periodic peak structure with increased amplitude and frequency
        periodic_peaks = np.sum(3.0 * np.cos(4 * np.pi * x_norm) * np.sin(6 * np.pi * x_norm) + 
                               2.0 * np.cos(8 * np.pi * x_norm) * np.sin(10 * np.pi * x_norm))
        
        # Modified Gaussian valley structure with wider spread
        gaussian_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.7 * np.sin(3 * np.pi * x_norm))))
        
        # Altered cross-dimensional correlation with stronger chaotic interaction
        cross_dim_corr = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               (1 + 0.4 * np.sin(5 * np.pi * x_norm[:-1])) * 
                               (1 + 0.3 * np.cos(4 * np.pi * x_norm[1:])))
        
        # Modified multi-scale harmonic modulation
        harmonic_modulation = np.sum(np.sin(12 * x_norm) * np.cos(10 * x_norm) * 
                                    (1 + 0.3 * np.sin(7 * x_norm)) * 
                                    (1 + 0.25 * np.cos(5 * x_norm)))
        
        # Adjusted power-law conditioned regions
        power_law_regions = np.sum(np.abs(x_norm)**1.5 * (1 + 0.5 * np.sin(14 * x_norm)))
        
        # Modified fractal-like correlation structure
        fractal_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.15 + 0.15 * np.cos(6 * x_norm[:-1]))))
        
        # Modified adaptive conditioning with local scaling
        adaptive_conditioning = np.sum((1 + 0.6 * np.sin(3 * x_norm)) * 
                                     np.exp(-0.4 * x_norm**2) * 
                                     (1 + 0.4 * np.cos(4 * x_norm)))
        
        # Combined landscape with modified curvature regions
        return 1.8 * (periodic_peaks + gaussian_valleys + cross_dim_corr + 
                     harmonic_modulation + power_law_regions + fractal_corr + 
                     adaptive_conditioning)