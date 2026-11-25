import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic phase interaction peaks with exponential modulation
        chaotic_peaks = np.sum(np.exp(3 * np.sin(7 * x_norm) * np.cos(5 * x_norm)) * 
                              np.sin(9 * x_norm) * np.cos(4 * x_norm))
        
        # Gaussian valleys with fractal-like width variation
        gaussian_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.1 + 0.9 * np.abs(np.sin(3 * x_norm)))))
        
        # Cross-dimensional correlation with chaotic coupling
        cross_dim_corr = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.05 + 0.05 * np.sin(8 * x_norm[:-1]))))
        
        # Multi-scale harmonic modulation with chaotic frequency
        harmonic_modulation = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm) * 
                                    (1 + 0.3 * np.sin(10 * x_norm)) * 
                                    (1 + 0.25 * np.cos(7 * x_norm)) * 
                                    np.exp(-0.1 * np.abs(x_norm)))
        
        # Power-law conditioned regions with chaotic exponent variation
        power_law_regions = np.sum(np.abs(x_norm)**(1.5 + 0.5 * np.sin(15 * x_norm)) * 
                                  (1 + 0.3 * np.cos(12 * x_norm)))
        
        # Fractal-like correlation structure with varying dimensionality
        fractal_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.2 + 0.2 * np.sin(6 * x_norm[:-1]))))
        
        # Adaptive conditioning with dynamic scaling factor
        adaptive_conditioning = np.sum((1 + 0.8 * np.sin(3 * x_norm)) * 
                                     np.exp(-0.5 * x_norm**2) * 
                                     (1 + 0.4 * np.cos(5 * x_norm)) * 
                                     np.exp(-0.2 * np.abs(x_norm)))
        
        # Sharp fitness gradient regions with chaotic curvature
        sharp_gradients = np.sum(np.abs(x_norm)**3 * (1 + 0.6 * np.sin(18 * x_norm)) * 
                                np.exp(-0.4 * x_norm**2))
        
        # Combined landscape with extreme conditioning variations
        return 2.0 * (chaotic_peaks + gaussian_valleys + cross_dim_corr + 
                     harmonic_modulation + power_law_regions + fractal_corr + 
                     adaptive_conditioning + sharp_gradients)