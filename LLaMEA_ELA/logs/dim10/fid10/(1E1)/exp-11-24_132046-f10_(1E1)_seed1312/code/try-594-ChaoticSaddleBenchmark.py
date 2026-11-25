import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic saddle structure with exponential growth
        chaotic_saddles = np.sum(np.exp(-5.0 * np.abs(x_norm)) * 
                                np.sin(10.0 * x_norm) * 
                                np.cos(7.0 * x_norm))
        
        # Non-convex regions with dynamic curvature
        non_convex_curvature = np.sum((x_norm**2 - 2.0 * x_norm + 1.0) * 
                                     (1.0 + 0.5 * np.sin(3.0 * x_norm)) * 
                                     np.exp(-0.5 * x_norm**2))
        
        # Sharp valley structure with multiple local minima
        sharp_valleys = np.sum(np.abs(x_norm)**1.7 * 
                              (1.0 + 0.3 * np.cos(8.0 * x_norm)) * 
                              np.exp(-0.2 * np.abs(x_norm)))
        
        # Flat regions with high condition number
        flat_regions = np.sum((x_norm**4 + 0.5 * x_norm**2) * 
                             (1.0 + 0.4 * np.sin(5.0 * x_norm)) * 
                             np.exp(-0.1 * x_norm**2))
        
        # Dynamic interaction terms with time-like scaling
        dynamic_interaction = np.sum(np.sin(np.pi * x_norm[:-1]) * 
                                   np.cos(np.pi * x_norm[1:]) * 
                                   (1.0 + 0.3 * np.sin(2.0 * np.pi * x_norm[:-1])) * 
                                   (1.0 + 0.2 * np.cos(3.0 * np.pi * x_norm[1:])))
        
        # Multi-scale oscillatory pattern
        oscillatory_pattern = np.sum(np.sin(15.0 * x_norm) * 
                                   np.cos(12.0 * x_norm) * 
                                   (1.0 + 0.2 * np.sin(9.0 * x_norm)) * 
                                   (1.0 + 0.15 * np.cos(6.0 * x_norm)))
        
        # Combined landscape with varying conditioning
        return 2.0 * (chaotic_saddles + non_convex_curvature + sharp_valleys + 
                     flat_regions + dynamic_interaction + oscillatory_pattern)