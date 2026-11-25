import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic saddle structure with exponential growth
        chaotic_saddles = np.sum(np.exp(-5.0 * np.abs(x_norm)) * np.sin(10.0 * x_norm) * 
                                np.cos(7.0 * x_norm) * (1.0 + 0.3 * np.sin(15.0 * x_norm)))
        
        # Non-linear correlation with dynamic coupling
        non_linear_corr = np.sum((x_norm[:-1]**2 + x_norm[1:]**2) * 
                                np.exp(-0.5 * (x_norm[:-1] - x_norm[1:])**2) * 
                                (1.0 + 0.2 * np.cos(3.0 * (x_norm[:-1] + x_norm[1:]))))
        
        # Dynamic conditioning with piecewise scaling
        dynamic_conditioning = np.sum((1.0 + 0.5 * np.sin(4.0 * x_norm)) * 
                                    np.exp(-0.2 * np.abs(x_norm)**1.7) * 
                                    (1.0 + 0.3 * np.cos(6.0 * x_norm)))
        
        # Abrupt curvature changes with step functions
        abrupt_curvature = np.sum(np.floor(5.0 * np.abs(x_norm)) * 
                                np.exp(-0.1 * x_norm**2) * 
                                (1.0 + 0.4 * np.sin(8.0 * x_norm)))
        
        # Multi-scale harmonic interference
        harmonic_interference = np.sum(np.sin(2.0 * x_norm) * np.cos(3.0 * x_norm) * 
                                     (1.0 + 0.25 * np.sin(5.0 * x_norm)) * 
                                     (1.0 + 0.2 * np.cos(4.0 * x_norm)))
        
        # Asymmetric valley structure with logarithmic scaling
        asymmetric_valleys = np.sum(np.exp(-np.abs(x_norm) / (0.5 + 0.5 * np.sin(2.0 * x_norm))) * 
                                  (1.0 + 0.3 * np.cos(6.0 * x_norm)) * 
                                  (x_norm**2 + 0.1))
        
        # Combined landscape with mixed smoothness and complexity
        return 2.0 * (chaotic_saddles + non_linear_corr + dynamic_conditioning + 
                     abrupt_curvature + harmonic_interference + asymmetric_valleys)