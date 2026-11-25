import numpy as np

class ChaoticAsymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay base with chaotic modulation
        exp_decay = np.sum(np.exp(-np.abs(x_norm) * (1 + 0.5 * np.sin(10 * x_norm))))
        
        # Trigonometric interference pattern with asymmetric peaks
        trig_interference = np.sum(np.sin(8 * x_norm) * np.cos(6 * x_norm) * 
                                  (1 + 0.3 * np.sin(4 * x_norm)) * 
                                  (1 + 0.2 * np.cos(5 * x_norm)) * 
                                  np.exp(-0.5 * x_norm**2))
        
        # Asymmetric basin structure with varying curvature
        asymmetric_basins = np.sum((np.abs(x_norm)**1.7) * 
                                  (1 + 0.4 * np.sin(3 * x_norm)) * 
                                  (1 + 0.3 * np.cos(7 * x_norm)) * 
                                  np.exp(-0.2 * np.abs(x_norm)))
        
        # Sharp transition regions with piecewise exponential behavior
        sharp_transitions = np.sum(np.exp(-np.abs(x_norm) / (0.1 + 0.1 * np.sin(15 * x_norm))) * 
                                  np.sin(2 * x_norm)**2)
        
        # Cross-dimensional coupling with asymmetric interaction
        cross_dim_coupling = np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                                   (1 + 0.2 * np.sin(5 * x_norm[:-1])) * 
                                   (1 + 0.3 * np.cos(8 * x_norm[1:])))
        
        # Multi-scale chaotic modulation
        chaotic_modulation = np.sum(np.sin(12 * x_norm) * np.cos(9 * x_norm) * 
                                  np.exp(-0.1 * np.abs(x_norm)) * 
                                  (1 + 0.25 * np.sin(6 * x_norm)))
        
        # Combined landscape with chaotic behavior
        return 2.0 * (exp_decay + trig_interference + asymmetric_basins + 
                     sharp_transitions + cross_dim_coupling + chaotic_modulation)