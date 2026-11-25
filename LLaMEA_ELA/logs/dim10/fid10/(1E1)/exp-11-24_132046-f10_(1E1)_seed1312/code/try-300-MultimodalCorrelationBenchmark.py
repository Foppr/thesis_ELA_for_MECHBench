import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced periodic peak structure with chaotic amplitude modulation
        periodic_peaks = np.sum(3.0 * np.cos(4 * np.pi * x_norm) * np.sin(6 * np.pi * x_norm) * 
                               (1 + 0.5 * np.sin(10 * np.pi * x_norm)) + 
                               2.0 * np.cos(8 * np.pi * x_norm) * np.sin(12 * np.pi * x_norm) * 
                               (1 + 0.3 * np.cos(15 * np.pi * x_norm)))
        
        # Complex Gaussian valley structure with multi-scale width variation
        gaussian_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.7 * np.sin(3 * np.pi * x_norm)**2)) + 
                                0.5 * np.exp(-0.5 * (x_norm**2) / (0.8 + 0.2 * np.cos(5 * np.pi * x_norm)**2)))
        
        # Enhanced cross-dimensional correlation with chaotic interaction
        cross_dim_corr = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               (1 + 0.4 * np.sin(5 * np.pi * x_norm[:-1])) * 
                               (1 + 0.3 * np.cos(4 * np.pi * x_norm[1:])) * 
                               np.exp(-0.1 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Multi-scale harmonic modulation with chaotic frequency variation
        harmonic_modulation = np.sum(np.sin(12 * x_norm) * np.cos(10 * x_norm) * 
                                    (1 + 0.3 * np.sin(8 * x_norm)) * 
                                    (1 + 0.25 * np.cos(6 * x_norm)) * 
                                    (1 + 0.2 * np.sin(14 * x_norm)))
        
        # Power-law conditioned regions with chaotic exponent variation
        power_law_regions = np.sum(np.abs(x_norm)**1.7 * (1 + 0.5 * np.sin(15 * x_norm)) * 
                                 (1 + 0.3 * np.cos(12 * x_norm)))
        
        # Fractal-like correlation structure with varying fractal dimension
        fractal_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.05 + 0.15 * np.cos(7 * x_norm[:-1])**2)))
        
        # Adaptive conditioning with dynamic scaling and chaotic modulation
        adaptive_conditioning = np.sum((1 + 0.7 * np.sin(3 * x_norm)) * 
                                     np.exp(-0.4 * x_norm**2) * 
                                     (1 + 0.4 * np.cos(5 * x_norm)) * 
                                     (1 + 0.2 * np.sin(8 * x_norm)))
        
        # Additional chaotic basin structure with irregular boundaries
        basin_structure = np.sum(np.sin(20 * x_norm) * np.cos(18 * x_norm) * 
                                (1 + 0.3 * np.sin(25 * x_norm)) * 
                                np.exp(-0.2 * np.abs(x_norm)))
        
        # Combined landscape with extreme conditioning variations
        return 2.0 * (periodic_peaks + gaussian_valleys + cross_dim_corr + 
                     harmonic_modulation + power_law_regions + fractal_corr + 
                     adaptive_conditioning + basin_structure)