import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay base with chaotic modulation
        exp_decay = np.sum(np.exp(-np.abs(x_norm) * (1 + 0.5 * np.sin(10 * x_norm))))
        
        # Trigonometric interference pattern with varying frequencies
        trig_interference = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * 
                                  np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Adaptive conditioning with exponential scaling
        adaptive_cond = np.sum(np.exp(x_norm**2 / (1 + np.abs(x_norm))) * 
                              (1 + 0.3 * np.sin(8 * x_norm)) * 
                              (1 + 0.2 * np.cos(6 * x_norm)))
        
        # Cross-dimensional chaotic coupling
        cross_coupling = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) * 
                                     (1 + 0.4 * np.sin(4 * np.pi * (x_norm[:-1] + x_norm[1:])))) * 
                               np.cos(np.pi * (x_norm[:-1] + x_norm[1:])))
        
        # Multi-scale oscillatory structure
        oscillatory = np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm) * 
                            (1 + 0.25 * np.sin(9 * x_norm)) * 
                            (1 + 0.3 * np.cos(6 * x_norm)))
        
        # Power-law chaotic regions
        power_law = np.sum(np.abs(x_norm)**1.7 * (1 + 0.4 * np.sin(11 * x_norm)) * 
                          np.exp(-0.5 * x_norm**2))
        
        # Sharp transition zones
        sharp_transitions = np.sum(np.abs(np.sin(20 * x_norm)) * 
                                 np.exp(-0.1 * np.abs(x_norm)))
        
        # Combined chaotic landscape
        return 2.0 * (exp_decay + trig_interference + adaptive_cond + 
                     cross_coupling + oscillatory + power_law + sharp_transitions)