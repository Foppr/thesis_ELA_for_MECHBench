import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Multiple sinusoidal modulations with different frequencies
        f2 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) * np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Enhanced exponential barrier terms with different exponents
        barriers = np.sum(np.exp(-0.3 * np.sum(np.abs(x_norm)**4)) + 0.6 * np.exp(-0.4 * np.sum(np.abs(x_norm)**5)))
        
        # Chaotic component using logistic map-like behavior with multiple iterations
        chaotic = np.sum(np.sin(6 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm) * np.sin(12 * np.pi * x_norm))
        
        # Additional ruggedness term with higher frequency oscillations
        rugged = np.sum(np.sin(12 * np.pi * x_norm) * np.exp(-0.15 * np.sum(x_norm**2)))
        
        # High-frequency chaotic modulation with adaptive conditioning
        adaptive_conditioning = np.sum(np.sin(25 * np.pi * x_norm) * np.cos(30 * np.pi * x_norm) * 
                                       np.exp(-0.08 * np.sum(x_norm**2)) * 
                                       (1 + 0.15 * np.sin(60 * np.pi * x_norm)))
        
        # Novel interaction term between dimensions with increased complexity
        interaction = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * 
                            np.exp(-0.15 * np.sum(np.abs(x_norm)**3)) * 
                            np.sin(4 * np.pi * np.sum(x_norm**2)))
        
        # Combine all components with different weights
        return 1.8 * f1 + 2.5 * f2 + 0.9 * barriers + 0.5 * chaotic + 0.7 * rugged + 0.8 * adaptive_conditioning + 0.6 * interaction