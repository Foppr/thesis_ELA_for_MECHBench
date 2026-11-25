import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basin structure with chaotic modulation
        radial_term = np.sum(x_norm**2 * (1 + 0.3 * np.sin(10 * np.pi * x_norm)))
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_modulation = np.sum(np.sin(5 * np.pi * x_norm) * 
                               np.cos(7 * np.pi * x_norm) * 
                               (1 + 0.2 * np.sin(3 * np.pi * x_norm)))
        
        # Asymmetric gradient components
        asym_gradient = np.sum(np.abs(x_norm)**1.5 * 
                              (1 + 0.4 * np.cos(4 * np.pi * x_norm)) * 
                              np.sign(x_norm))
        
        # Chaotic interaction between dimensions
        chaotic_interaction = np.sum(np.sin(np.pi * x_norm[:-1] * x_norm[1:]) * 
                                   np.cos(np.pi * x_norm[:-1] + x_norm[1:]) * 
                                   (1 + 0.3 * np.sin(2 * np.pi * x_norm[:-1])))
        
        # Multi-scale harmonic interference
        harmonic_interference = np.sum(np.sin(8 * x_norm) * 
                                     np.cos(6 * x_norm) * 
                                     np.exp(-0.5 * x_norm**2))
        
        # Power-law conditioned regions with exponential decay
        power_law_conditioning = np.sum(np.abs(x_norm)**1.7 * 
                                       np.exp(-0.1 * np.abs(x_norm)) * 
                                       (1 + 0.2 * np.sin(5 * x_norm)))
        
        # Combined landscape
        return 2.0 * (radial_term + sin_modulation + asym_gradient + 
                     chaotic_interaction + harmonic_interference + 
                     power_law_conditioning)