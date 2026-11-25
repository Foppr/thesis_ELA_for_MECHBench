import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-wave structure with varying frequencies
        chaotic_sine = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * 
                             (1 + 0.3 * np.sin(5 * np.pi * x_norm)) * 
                             (1 + 0.2 * np.cos(3 * np.pi * x_norm)))
        
        # Hyperbolic tangent valleys with adaptive scaling
        hyperbolic_valleys = np.sum(np.tanh(2 * x_norm) * np.exp(-0.5 * x_norm**2) * 
                                  (1 + 0.4 * np.sin(8 * x_norm)))
        
        # Saddle point structure with cross-dimensional interaction
        saddle_structure = np.sum((x_norm[:-1]**2 - x_norm[1:]**2) * 
                                (1 + 0.3 * np.cos(4 * np.pi * x_norm[:-1])) * 
                                (1 + 0.2 * np.sin(6 * np.pi * x_norm[1:])))
        
        # Multi-scale Gaussian-like peaks with varying amplitudes
        gaussian_peaks = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.7 * np.cos(3 * x_norm))) * 
                              (1 + 0.5 * np.sin(9 * x_norm)))
        
        # Non-linear coupling with polynomial interaction
        poly_coupling = np.sum((x_norm[:-1]**3 + x_norm[1:]**3) * 
                             (1 + 0.2 * np.sin(2 * np.pi * x_norm[:-1])) * 
                             (1 + 0.3 * np.cos(5 * np.pi * x_norm[1:])))
        
        # Gradient variation with directional dependence
        gradient_variation = np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                                  (1 + 0.4 * np.sin(7 * np.pi * x_norm[:-1])) * 
                                  (1 + 0.3 * np.cos(4 * np.pi * x_norm[1:])))
        
        # Power-law conditioned with exponential modulation
        power_exp_modulation = np.sum(np.abs(x_norm)**1.7 * np.exp(-0.2 * x_norm**2) * 
                                    (1 + 0.3 * np.sin(11 * x_norm)))
        
        # Combined chaotic landscape
        return 2.0 * (chaotic_sine + hyperbolic_valleys + saddle_structure + 
                     gaussian_peaks + poly_coupling + gradient_variation + 
                     power_exp_modulation)