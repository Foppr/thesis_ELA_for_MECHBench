import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic periodic peaks with exponential modulation
        chaotic_peaks = np.sum(np.exp(3 * np.abs(np.sin(7 * np.pi * x_norm))) * 
                              np.cos(5 * np.pi * x_norm) * 
                              np.sin(9 * np.pi * x_norm))
        
        # Gaussian valleys with logarithmic scaling
        gaussian_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.1 + 0.9 * np.abs(np.sin(3 * np.pi * x_norm)))) * 
                                 np.log(1 + 0.5 * np.abs(x_norm)))
        
        # Cross-dimensional chaotic correlation with non-linear coupling
        cross_dim_corr = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               np.exp(-0.5 * np.abs(x_norm[:-1] - x_norm[1:]) / (0.01 + 0.99 * np.sin(4 * np.pi * x_norm[:-1]))))
        
        # Multi-scale fractal-like structure with power-law scaling
        fractal_structure = np.sum(np.exp(-np.abs(x_norm)**1.7) * 
                                  np.sin(15 * x_norm) * 
                                  (1 + 0.3 * np.cos(12 * x_norm)))
        
        # Adaptive conditioning with exponential curvature
        adaptive_conditioning = np.sum((1 + 0.8 * np.sin(3 * x_norm)) * 
                                     np.exp(-0.5 * x_norm**2) * 
                                     np.exp(0.3 * np.abs(x_norm)) * 
                                     (1 + 0.2 * np.cos(7 * x_norm)))
        
        # Sharp fitness transitions with step-like behavior
        sharp_transitions = np.sum(np.abs(np.sin(10 * np.pi * x_norm)) * 
                                 np.exp(-0.1 * np.abs(x_norm)) * 
                                 (1 + 0.5 * np.sin(8 * np.pi * x_norm)))
        
        # Power-law conditioned regions with chaotic exponent
        power_law_regions = np.sum(np.abs(x_norm)**(1.2 + 0.8 * np.sin(13 * x_norm)) * 
                                 (1 + 0.6 * np.cos(9 * x_norm)))
        
        # Combined landscape with extreme conditioning variations
        return 2.0 * (chaotic_peaks + gaussian_valleys + cross_dim_corr + 
                     fractal_structure + adaptive_conditioning + sharp_transitions + 
                     power_law_regions)