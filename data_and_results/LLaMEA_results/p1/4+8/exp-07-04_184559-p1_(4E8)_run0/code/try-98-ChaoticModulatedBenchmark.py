import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Enhanced sinusoidal modulations with adaptive frequencies
        f2 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) * 
                   np.exp(-0.3 * np.sum(x_norm**2)) * 
                   (1 + 0.2 * np.sin(10 * np.pi * x_norm)))
        
        # Enhanced exponential barrier terms with variable exponents
        barriers = np.sum(0.8 * np.exp(-0.1 * np.sum(np.abs(x_norm)**3)) + 
                         0.6 * np.exp(-0.2 * np.sum(np.abs(x_norm)**4)) + 
                         0.4 * np.exp(-0.05 * np.sum(np.abs(x_norm)**6)))
        
        # Chaotic component with enhanced logistic map behavior
        chaotic = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                        np.sin(13 * np.pi * x_norm) * 
                        np.exp(-0.15 * np.sum(x_norm**2)))
        
        # Enhanced ruggedness term with multiple high-frequency components
        rugged = np.sum(np.sin(15 * np.pi * x_norm) * np.cos(20 * np.pi * x_norm) * 
                       np.exp(-0.08 * np.sum(x_norm**2)) * 
                       (1 + 0.15 * np.sin(40 * np.pi * x_norm)))
        
        # Adaptive conditioning with dynamic scaling
        adaptive_conditioning = np.sum(np.sin(25 * np.pi * x_norm) * 
                                     np.cos(30 * np.pi * x_norm) * 
                                     np.exp(-0.03 * np.sum(x_norm**2)) * 
                                     (1 + 0.2 * np.sin(60 * np.pi * x_norm)) * 
                                     (1 + 0.1 * np.cos(80 * np.pi * x_norm)))
        
        # Novel cross-dimension interaction term with enhanced complexity
        interaction = np.sum(np.sin(np.pi * x_norm) * np.cos(2 * np.pi * x_norm) * 
                            np.exp(-0.2 * np.sum(np.abs(x_norm)**3)) * 
                            np.sin(3 * np.pi * np.sum(x_norm**2)) * 
                            np.cos(5 * np.pi * np.sum(x_norm**3)))
        
        # Additional coupling term between dimensions
        coupling = np.sum(np.sin(np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * 
                         np.exp(-0.1 * np.sum(np.abs(x_norm)**2)) * 
                         np.sin(2 * np.pi * np.sum(x_norm**2)) * 
                         np.cos(4 * np.pi * np.sum(x_norm**3)))
        
        # Combine all components with optimized weights
        return 1.2 * f1 + 2.5 * f2 + 0.9 * barriers + 0.5 * chaotic + 0.7 * rugged + 0.8 * adaptive_conditioning + 0.6 * interaction + 0.4 * coupling