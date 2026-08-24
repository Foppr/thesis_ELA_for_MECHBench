import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Multi-scale sinusoidal modulations with varying frequencies and amplitudes
        f2 = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * 
                   np.sin(5 * np.pi * x_norm) * np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Enhanced exponential barrier terms with higher exponents and additional interaction
        barriers = np.sum(np.exp(-0.3 * np.sum(np.abs(x_norm)**6)) + 
                         0.7 * np.exp(-0.4 * np.sum(np.abs(x_norm)**7)) + 
                         0.3 * np.exp(-0.2 * np.sum(np.abs(x_norm)**8)))
        
        # Chaotic component using a modified logistic map with multiple iterations and feedback
        chaotic = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                        np.sin(13 * np.pi * x_norm) * np.cos(17 * np.pi * x_norm) * 
                        np.exp(-0.1 * np.sum(x_norm**2)))
        
        # Additional ruggedness term with even higher frequency oscillations
        rugged = np.sum(np.sin(15 * np.pi * x_norm) * np.cos(20 * np.pi * x_norm) * 
                       np.exp(-0.05 * np.sum(x_norm**2)))
        
        # High-frequency chaotic modulation with adaptive conditioning and dynamic scaling
        adaptive_conditioning = np.sum(np.sin(30 * np.pi * x_norm) * np.cos(35 * np.pi * x_norm) * 
                                     np.exp(-0.02 * np.sum(x_norm**2)) * 
                                     (1 + 0.2 * np.sin(60 * np.pi * x_norm)) * 
                                     (1 + 0.15 * np.cos(40 * np.pi * x_norm)))
        
        # Novel interaction term between dimensions with higher-order polynomial coupling
        interaction = np.sum(np.sin(np.pi * x_norm) * np.cos(2 * np.pi * x_norm) * 
                            np.exp(-0.15 * np.sum(np.abs(x_norm)**4)) * 
                            np.sin(4 * np.pi * np.sum(x_norm**2)) * 
                            np.cos(6 * np.pi * np.sum(x_norm**3)))
        
        # Multi-scale chaotic modulation with dynamic phase shifts
        multi_scale = np.sum(np.sin(25 * np.pi * x_norm) * np.cos(30 * np.pi * x_norm) * 
                            np.sin(35 * np.pi * x_norm) * np.exp(-0.08 * np.sum(x_norm**2)) * 
                            (1 + 0.1 * np.sin(80 * np.pi * x_norm)) * 
                            (1 + 0.05 * np.cos(100 * np.pi * x_norm)))
        
        # Combine all components with different weights
        return 1.8 * f1 + 3.5 * f2 + 1.0 * barriers + 0.5 * chaotic + 0.7 * rugged + 0.8 * adaptive_conditioning + 0.6 * interaction + 0.9 * multi_scale