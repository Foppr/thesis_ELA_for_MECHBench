import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic gradient component with sinusoidal modulation
        chaotic_grad = np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm) * 
                             (1 + 0.3 * np.sin(5 * x_norm)) * 
                             (1 + 0.2 * np.cos(3 * x_norm)))
        
        # Exponential decay corridors with asymmetric scaling
        exp_corridors = np.sum(np.exp(-np.abs(x_norm) / (0.5 + 0.5 * np.sin(4 * x_norm))) * 
                              (1 + 0.4 * np.cos(6 * x_norm)) * 
                              (1 + 0.3 * np.sin(8 * x_norm)))
        
        # Saddle point structure with varying stability
        saddle_points = np.sum((x_norm**2 - 1)**2 * (1 + 0.5 * np.sin(3 * x_norm)) * 
                              (1 + 0.3 * np.cos(5 * x_norm)))
        
        # Asymmetric basin structures with directional bias
        asymmetric_basins = np.sum(np.abs(x_norm)**1.7 * (1 + 0.6 * np.sin(9 * x_norm)) * 
                                  (1 + 0.4 * np.cos(4 * x_norm)) * 
                                  np.sign(x_norm))
        
        # Multi-scale curvature variation with local maxima
        multi_curvature = np.sum(np.sin(2 * x_norm) * np.cos(3 * x_norm) * 
                                (1 + 0.5 * np.sin(7 * x_norm)) * 
                                (1 + 0.3 * np.cos(11 * x_norm)))
        
        # Cross-dimensional interaction with chaotic coupling
        cross_interaction = np.sum(np.sin(np.pi * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                  np.cos(np.pi * (x_norm[:-1] * x_norm[1:])) * 
                                  (1 + 0.2 * np.sin(5 * x_norm[:-1])) * 
                                  (1 + 0.3 * np.cos(7 * x_norm[1:])))
        
        # Combined landscape with non-smooth transitions
        return 2.0 * (chaotic_grad + exp_corridors + saddle_points + 
                     asymmetric_basins + multi_curvature + cross_interaction)