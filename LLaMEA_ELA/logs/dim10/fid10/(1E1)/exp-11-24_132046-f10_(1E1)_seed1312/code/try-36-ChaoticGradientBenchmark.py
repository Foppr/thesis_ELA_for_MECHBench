import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with adaptive curvature
        f1 = np.sum(0.5 * x_norm**2 * (1 + 0.2 * np.sin(3 * x_norm)))
        
        # Exponential decay correlation structure
        f2 = 0.8 * np.sum(np.exp(-np.abs(x_norm)) * np.cos(2 * np.pi * x_norm) * 
                         (1 + 0.3 * np.sin(5 * x_norm)))
        
        # Multi-scale periodic components with varying amplitudes
        f3 = 0.6 * np.sum(np.sin(7 * x_norm) * np.cos(9 * x_norm) * 
                         (1 + 0.4 * np.sin(2 * x_norm)) * 
                         (1 + 0.2 * np.cos(4 * x_norm)))
        
        # Asymmetric hill-climbing attractors with varying steepness
        f4 = 0.4 * np.sum(np.exp(-x_norm**2) * np.sin(6 * np.pi * x_norm) * 
                         (1 + 0.3 * np.cos(8 * np.pi * x_norm)) * 
                         (1 + 0.1 * np.sin(10 * np.pi * x_norm)))
        
        # Chaotic gradient modulation with memory effect
        f5 = 0.3 * np.sum(np.sin(11 * x_norm) * np.cos(13 * x_norm) * 
                         np.exp(-0.5 * np.abs(x_norm)) * 
                         (1 + 0.25 * np.sin(7 * x_norm)))
        
        # Cross-dimensional coupling with directional bias
        f6 = 0.2 * np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                         np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                         (1 + 0.2 * np.cos(3 * np.pi * x_norm[:-1])))
        
        # Fractal-like self-similarity with recursive scaling
        f7 = 0.15 * np.sum(np.sin(17 * x_norm) * np.cos(19 * x_norm) * 
                          (1 + 0.1 * np.sin(13 * x_norm)) * 
                          (1 + 0.15 * np.cos(15 * x_norm)))
        
        # High-frequency oscillatory component with amplitude modulation
        f8 = 0.1 * np.sum(np.sin(23 * x_norm) * np.cos(27 * x_norm) * 
                         (1 + 0.3 * np.sin(19 * x_norm)) * 
                         (1 + 0.2 * np.cos(21 * x_norm)))
        
        # Asymmetric saddle point distribution with variable depth
        f9 = 0.08 * np.sum(np.exp(-x_norm**2) * np.sin(4 * np.pi * x_norm) * 
                         (1 + 0.4 * np.cos(6 * np.pi * x_norm)) * 
                         (1 + 0.1 * np.sin(8 * np.pi * x_norm)))
        
        # Global scaling factor to control difficulty
        return 2.0 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9)