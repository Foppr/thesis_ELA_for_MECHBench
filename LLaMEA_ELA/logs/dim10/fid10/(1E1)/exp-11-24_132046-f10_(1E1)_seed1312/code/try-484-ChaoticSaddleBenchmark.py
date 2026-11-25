import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic saddle structure with exponential decay
        chaotic_saddle = np.sum(np.exp(-np.abs(x_norm)) * np.sin(10 * x_norm) * 
                               np.cos(7 * x_norm) * (1 + 0.3 * np.sin(5 * x_norm)))
        
        # Asymmetric gradient fields with directional bias
        asym_gradient = np.sum((x_norm**3 + 0.5 * x_norm**2 - 0.3 * x_norm) * 
                              np.exp(-0.5 * x_norm**2) * 
                              (1 + 0.4 * np.cos(3 * x_norm)))
        
        # Exponentially decaying correlations with random phase shifts
        decay_corr = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) * 
                                 (1 + 0.2 * np.sin(4 * x_norm[:-1]))) * 
                           np.cos(2 * np.pi * (x_norm[:-1] + x_norm[1:])))
        
        # Multi-scale chaotic modulation with varying amplitudes
        chaotic_modulation = np.sum(np.sin(8 * x_norm) * np.cos(6 * x_norm) * 
                                  np.exp(-0.1 * np.abs(x_norm)) * 
                                  (1 + 0.25 * np.sin(9 * x_norm)))
        
        # Rugged terrain with sharp directional transitions
        rugged_terrain = np.sum(np.abs(x_norm)**1.7 * np.sin(15 * x_norm) * 
                              (1 + 0.3 * np.cos(12 * x_norm)))
        
        # Adaptive conditioning with exponential scaling
        adaptive_cond = np.sum(np.exp(-0.2 * np.abs(x_norm)) * 
                             (1 + 0.5 * np.sin(4 * x_norm)) * 
                             (x_norm**2 + 0.1))
        
        # Combined chaotic landscape with saddle-point characteristics
        return 2.0 * (chaotic_saddle + asym_gradient + decay_corr + 
                     chaotic_modulation + rugged_terrain + adaptive_cond)