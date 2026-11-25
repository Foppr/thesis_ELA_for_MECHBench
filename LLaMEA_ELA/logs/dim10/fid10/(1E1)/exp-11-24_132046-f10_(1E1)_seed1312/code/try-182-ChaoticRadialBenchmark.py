import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basins with chaotic modulation
        radial_basins = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm)) * 
                              np.exp(-0.5 * (x_norm**2)))
        
        # Sinusoidal modulations with varying frequencies and amplitudes
        sin_modulation = np.sum(np.sin(5 * x_norm) * np.cos(7 * x_norm) * 
                               (1 + 0.3 * np.sin(3 * x_norm)) * 
                               (1 + 0.2 * np.cos(4 * x_norm)))
        
        # Asymmetric gradient fields with chaotic perturbations
        asym_gradient = np.sum(np.abs(x_norm)**1.5 * np.sin(2 * x_norm) * 
                              (1 + 0.4 * np.sin(8 * x_norm)) * 
                              (1 + 0.3 * np.cos(6 * x_norm)))
        
        # Chaotic attractor-like structure with cross-dimensional interactions
        chaotic_attr = np.sum(np.sin(np.pi * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                             np.cos(np.pi * (x_norm[:-1] - x_norm[1:])) * 
                             (1 + 0.2 * np.sin(5 * x_norm[:-1]) * np.cos(3 * x_norm[1:])))
        
        # Multi-scale harmonic interference
        interference = np.sum(np.sin(4 * x_norm) * np.cos(6 * x_norm) * 
                             (1 + 0.25 * np.sin(9 * x_norm)) * 
                             (1 + 0.3 * np.cos(7 * x_norm)))
        
        # Sharp transition regions with exponential penalties
        sharp_transitions = np.sum(np.exp(5 * np.abs(x_norm - np.mean(x_norm))) * 
                                 (1 + 0.5 * np.sin(12 * x_norm)))
        
        # Combined landscape with varying curvature and conditioning
        return 2.0 * (radial_basins + sin_modulation + asym_gradient + 
                     chaotic_attr + interference + sharp_transitions)