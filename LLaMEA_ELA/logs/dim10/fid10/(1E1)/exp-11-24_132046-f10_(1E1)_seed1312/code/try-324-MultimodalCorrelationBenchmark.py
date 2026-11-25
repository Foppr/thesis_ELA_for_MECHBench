import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic phase interaction peaks with non-linear coupling
        chaotic_peaks = np.sum(3.0 * np.sin(7 * x_norm) * np.cos(5 * x_norm) * 
                              np.exp(-0.5 * (x_norm**2)) + 
                              2.0 * np.sin(11 * x_norm) * np.cos(9 * x_norm) * 
                              np.exp(-0.3 * (x_norm**2)))
        
        # Fractal-like Gaussian valleys with varying scales
        fractal_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.1 + 0.9 * np.abs(np.sin(3 * x_norm)))))
        
        # Cross-dimensional chaotic correlation with dynamic coupling
        cross_dim_corr = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                               np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                               np.exp(-0.2 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                               (1 + 0.5 * np.sin(8 * x_norm[:-1]) * np.cos(7 * x_norm[1:])))
        
        # Multi-scale harmonic modulation with chaotic frequency
        harmonic_modulation = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm) * 
                                    (1 + 0.3 * np.sin(13 * x_norm)) * 
                                    (1 + 0.25 * np.cos(11 * x_norm)) * 
                                    np.exp(-0.1 * np.abs(x_norm)))
        
        # Power-law conditioned regions with dynamic exponents
        power_law_regions = np.sum(np.abs(x_norm)**1.7 * (1 + 0.6 * np.sin(15 * x_norm)) * 
                                  np.exp(-0.2 * x_norm**2))
        
        # Adaptive conditioning with time-varying local scaling
        adaptive_conditioning = np.sum((1 + 0.8 * np.sin(3 * x_norm)) * 
                                     np.exp(-0.4 * x_norm**2) * 
                                     (1 + 0.4 * np.cos(5 * x_norm)) * 
                                     np.exp(-0.1 * np.abs(x_norm)))
        
        # Phase-locked periodic structures with irregular spacing
        phase_locked = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm) * 
                             (1 + 0.3 * np.sin(4 * np.pi * x_norm)) * 
                             np.exp(-0.3 * (x_norm**2)))
        
        # Combined landscape with extreme conditioning variations
        return 2.0 * (chaotic_peaks + fractal_valleys + cross_dim_corr + 
                     harmonic_modulation + power_law_regions + adaptive_conditioning + 
                     phase_locked)