import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic phase interference peaks with non-linear coupling
        chaotic_peaks = np.sum(3.0 * np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * 
                              np.exp(-0.5 * (x_norm**2)) + 
                              2.0 * np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                              np.exp(-0.3 * (x_norm**2)))
        
        # Fractal Gaussian valleys with dimensionally dependent variance
        fractal_gauss = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.7 * np.sin(3 * np.pi * x_norm)**2)))
        
        # Enhanced cross-dimensional correlation with exponential decay
        enhanced_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.2 + 0.3 * np.sin(4 * np.pi * x_norm[:-1]))))
        
        # Multi-scale harmonic interference with adaptive frequency
        harmonic_interference = np.sum(np.sin(12 * x_norm) * np.cos(10 * x_norm) * 
                                     (1 + 0.5 * np.sin(8 * x_norm)) * 
                                     (1 + 0.4 * np.cos(6 * x_norm)) * 
                                     np.exp(-0.2 * x_norm**2))
        
        # Power-law conditioned regions with logarithmic scaling
        power_law_scaled = np.sum(np.abs(x_norm)**1.7 * (1 + 0.5 * np.sin(15 * x_norm)) * 
                                np.log(1 + np.abs(x_norm)))
        
        # Adaptive conditioning with dynamic curvature
        dynamic_conditioning = np.sum((1 + 0.8 * np.sin(3 * x_norm)) * 
                                    np.exp(-0.4 * x_norm**2) * 
                                    (1 + 0.5 * np.cos(5 * x_norm)) * 
                                    np.tanh(x_norm))
        
        # Combined landscape with chaotic basin structure
        return 2.0 * (chaotic_peaks + fractal_gauss + enhanced_corr + 
                     harmonic_interference + power_law_scaled + dynamic_conditioning)