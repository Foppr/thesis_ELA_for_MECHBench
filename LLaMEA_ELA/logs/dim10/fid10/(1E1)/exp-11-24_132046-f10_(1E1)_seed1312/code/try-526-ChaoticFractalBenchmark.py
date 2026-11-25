import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal modulation with chaotic phase shifts
        chaotic_modulation = np.sum(np.sin(10 * x_norm + np.sin(7 * x_norm)) * 
                                   np.cos(8 * x_norm + np.cos(5 * x_norm)))
        
        # Exponential valley structure with fractal scaling
        exp_valleys = np.sum(np.exp(-0.5 * (x_norm**2) / (0.3 + 0.7 * np.sin(3 * x_norm)**2)))
        
        # Multi-scale correlation with recursive interaction
        recursive_corr = np.sum(np.sin(np.pi * x_norm[:-1]) * 
                               np.cos(np.pi * x_norm[1:]) * 
                               (1 + 0.5 * np.sin(2 * np.pi * x_norm[:-1])) * 
                               (1 + 0.3 * np.cos(4 * np.pi * x_norm[1:])) * 
                               np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) / (0.2 + 0.8 * np.sin(6 * x_norm[:-1]))))
        
        # Power-law conditioned with logarithmic scaling
        power_law_scaling = np.sum(np.log(np.abs(x_norm) + 1) * (1 + 0.4 * np.sin(9 * x_norm)))
        
        # Fractal-like self-similarity with varying dimensions
        fractal_self_sim = np.sum(np.sin(2 * np.pi * x_norm) * 
                                 np.cos(3 * np.pi * x_norm) * 
                                 np.exp(-np.abs(x_norm)**0.7))
        
        # Non-linear transformation with cubic and quartic components
        nonlinear_transform = np.sum((x_norm**3 + 0.5 * x_norm**4) * 
                                    (1 + 0.3 * np.sin(6 * x_norm)) * 
                                    (1 + 0.2 * np.cos(8 * x_norm)))
        
        # Combined landscape with chaotic and smooth regions
        return 2.0 * (chaotic_modulation + exp_valleys + recursive_corr + 
                     power_law_scaling + fractal_self_sim + nonlinear_transform)