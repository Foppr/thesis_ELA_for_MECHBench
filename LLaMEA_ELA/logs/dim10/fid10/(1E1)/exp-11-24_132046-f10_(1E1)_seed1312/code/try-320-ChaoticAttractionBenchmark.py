import numpy as np

class ChaoticAttractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic saddle points with logistic map dynamics
        chaotic_terms = np.sum(4.0 * x_norm * (1.0 - x_norm) + 
                              3.0 * np.sin(np.pi * x_norm) * np.cos(np.pi * x_norm))
        
        # Exponential attraction basins with varying radii
        exp_attraction = np.sum(np.exp(-np.abs(x_norm) / (0.1 + 0.2 * np.abs(x_norm))) * 
                               (1.0 + 0.5 * np.sin(3 * x_norm)))
        
        # Adaptive gradient modulation with local curvature
        adaptive_grad = np.sum((1.0 + 0.3 * np.cos(2 * x_norm)) * 
                              (x_norm**2 + 0.1 * np.sin(5 * x_norm)) * 
                              np.exp(-0.5 * x_norm**2))
        
        # Multi-scale fractal-like correlation with diminishing returns
        fractal_corr = np.sum(np.abs(x_norm)**1.7 * (1.0 + 0.4 * np.cos(7 * x_norm)) * 
                             np.exp(-0.3 * np.abs(x_norm)))
        
        # Power-law conditioned regions with logarithmic scaling
        power_law = np.sum(np.log(np.abs(x_norm) + 1.0) * (1.0 + 0.2 * np.sin(4 * x_norm)))
        
        # Cross-dimensional coupling with asymmetric interaction
        cross_dim = np.sum((x_norm[:-1]**2 + x_norm[1:]**2) * 
                          np.exp(-0.5 * (x_norm[:-1] - x_norm[1:])**2) * 
                          (1.0 + 0.3 * np.sin(2 * np.pi * x_norm[:-1])))
        
        # Rare global optimum with sharp valley
        rare_optimum = np.sum(np.exp(-0.5 * (x_norm - 0.5)**2) * 
                             (1.0 + 0.8 * np.cos(10 * x_norm)))
        
        # Combined landscape with diverse curvature properties
        return 2.0 * (chaotic_terms + exp_attraction + adaptive_grad + 
                     fractal_corr + power_law + cross_dim + rare_optimum)