import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic phase interaction peaks with fractional harmonics
        chaotic_peaks = np.sum(3.0 * np.sin(7 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) * 
                              np.exp(-0.5 * (x_norm**2)) + 
                              2.0 * np.sin(5 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                              np.exp(-0.3 * (x_norm**2)))
        
        # Gaussian valleys with fractional Brownian motion-like correlation
        gaussian_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.7 * np.sin(3 * np.pi * x_norm))) * 
                                 (1 + 0.2 * np.cos(7 * np.pi * x_norm)))
        
        # Cross-dimensional correlation with hyperbolic tangent interactions
        cross_dim_corr = np.sum(np.tanh(2 * (x_norm[:-1] + x_norm[1:])) * 
                               np.tanh(3 * (x_norm[:-1] - x_norm[1:])) * 
                               (1 + 0.4 * np.sin(5 * np.pi * x_norm[:-1])) * 
                               (1 + 0.3 * np.cos(7 * np.pi * x_norm[1:])))
        
        # Multi-scale fractal modulation with power-law scaling
        fractal_modulation = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm) * 
                                   (1 + 0.3 * np.sin(9 * x_norm)) * 
                                   (1 + 0.25 * np.cos(6 * x_norm)) * 
                                   np.exp(-0.1 * np.abs(x_norm)**1.7))
        
        # Power-law conditioned regions with variable exponents
        power_law_regions = np.sum(np.abs(x_norm)**1.8 * (1 + 0.5 * np.sin(15 * x_norm)) * 
                                  (1 + 0.3 * np.cos(10 * x_norm)))
        
        # Hyperbolic fractal correlation structure
        hyperbolic_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / 
                                       (0.05 + 0.2 * np.sin(8 * x_norm[:-1]))))
        
        # Adaptive conditioning with dynamic scaling factors
        adaptive_conditioning = np.sum((1 + 0.7 * np.sin(3 * x_norm)) * 
                                     np.exp(-0.4 * x_norm**2) * 
                                     (1 + 0.4 * np.cos(5 * x_norm)) * 
                                     (1 + 0.2 * np.sin(13 * x_norm)))
        
        # Add extreme conditioning variation through exponential modulation
        extreme_conditioning = np.sum(np.exp(2 * np.abs(x_norm)) * 
                                    (1 + 0.3 * np.cos(17 * x_norm)) * 
                                    (1 + 0.2 * np.sin(14 * x_norm)))
        
        # Combined landscape with extreme curvature variations
        return 2.0 * (chaotic_peaks + gaussian_valleys + cross_dim_corr + 
                     fractal_modulation + power_law_regions + hyperbolic_corr + 
                     adaptive_conditioning + extreme_conditioning)