import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic phase interaction peaks
        chaotic_peaks = np.sum(np.sin(13 * x_norm) * np.cos(17 * x_norm) * 
                              np.exp(-0.5 * (x_norm**2)) * 
                              (1 + 0.6 * np.sin(8 * x_norm) * np.cos(11 * x_norm)))
        
        # Fractal correlation valleys with multi-scale interactions
        fractal_valleys = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / 
                                       (0.05 + 0.05 * np.sin(7 * x_norm[:-1]) * np.cos(9 * x_norm[1:]))))
        
        # Adaptive conditioning with exponential scaling
        adaptive_conditioning = np.sum((1 + 0.8 * np.sin(3 * x_norm)) * 
                                     np.exp(-0.4 * x_norm**2) * 
                                     (1 + 0.5 * np.cos(5 * x_norm)) * 
                                     (1 + 0.3 * np.sin(7 * x_norm)))
        
        # Multi-harmonic periodic structure with amplitude modulation
        multi_harmonic = np.sum(np.sin(9 * x_norm) * np.cos(12 * x_norm) * 
                               (1 + 0.4 * np.sin(6 * x_norm)) * 
                               (1 + 0.3 * np.cos(8 * x_norm)) * 
                               (1 + 0.2 * np.sin(10 * x_norm)))
        
        # Cross-dimensional coupling with power-law interactions
        cross_dim_coupling = np.sum(np.abs(x_norm[:-1] - x_norm[1:])**(1.7) * 
                                   (1 + 0.5 * np.sin(4 * x_norm[:-1])) * 
                                   (1 + 0.4 * np.cos(6 * x_norm[1:])))
        
        # Gaussian valleys with complex spatial correlation
        gaussian_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / 
                                        (0.3 + 0.3 * np.sin(3 * x_norm) * np.cos(5 * x_norm))))
        
        # Multi-scale chaotic modulation
        chaotic_modulation = np.sum(np.sin(15 * x_norm) * np.cos(19 * x_norm) * 
                                   np.exp(-0.2 * np.abs(x_norm)) * 
                                   (1 + 0.7 * np.sin(13 * x_norm)))
        
        # Combined landscape with strong nonlinearity and multiple basins
        return 2.0 * (chaotic_peaks + fractal_valleys + adaptive_conditioning + 
                     multi_harmonic + cross_dim_coupling + gaussian_valleys + 
                     chaotic_modulation)