import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-based structure with varying frequencies
        chaotic_term = np.sum(np.sin(10 * np.pi * x_norm) * 
                             np.cos(7 * np.pi * x_norm) * 
                             np.sin(5 * np.pi * x_norm))
        
        # Saddle point structure with hyperbolic tangents
        saddle_term = np.sum(np.tanh(3 * x_norm) * np.tanh(2 * x_norm) * 
                           (1 + 0.3 * np.cos(4 * np.pi * x_norm)))
        
        # Non-convex valley with multiple local minima
        non_convex_valley = np.sum((x_norm**2 + 0.5 * np.sin(8 * np.pi * x_norm)) * 
                                  (1 + 0.2 * np.cos(6 * np.pi * x_norm)))
        
        # Dynamic conditioning based on distance from origin
        dynamic_conditioning = np.sum((1 + 0.5 * np.sin(3 * np.pi * x_norm)) * 
                                    np.exp(-0.1 * np.abs(x_norm)) * 
                                    (1 + 0.3 * np.cos(5 * np.pi * x_norm)))
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / 
                                     (0.2 + 0.1 * np.sin(3 * np.pi * x_norm[:-1]))))
        
        # Multi-scale oscillatory behavior
        oscillatory_term = np.sum(np.sin(15 * x_norm) * 
                                np.cos(12 * x_norm) * 
                                (1 + 0.4 * np.sin(9 * x_norm)))
        
        # Asymmetric basin structure
        asymmetric_basin = np.sum(np.abs(x_norm)**1.7 * 
                                (1 + 0.3 * np.sin(5 * np.pi * x_norm)) * 
                                (1 + 0.2 * np.cos(7 * np.pi * x_norm)))
        
        # Combined chaotic landscape
        return 2.0 * (chaotic_term + saddle_term + non_convex_valley + 
                     dynamic_conditioning + cross_coupling + oscillatory_term + 
                     asymmetric_basin)