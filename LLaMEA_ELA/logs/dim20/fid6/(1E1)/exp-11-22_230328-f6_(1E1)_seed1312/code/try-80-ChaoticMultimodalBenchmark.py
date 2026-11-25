import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial component with fractal-like decay and multi-scale oscillations
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**3) * (1 + 0.6 * np.sin(8 * r) * np.cos(4 * r) * np.sin(2 * r))
        
        # Intensified trigonometric modulation with dynamic phase shifts and frequency mixing
        trig_term = np.sum(np.cos(6 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm) * 
                          (1 + 0.3 * np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm)))
        
        # Augmented chaotic component with multi-logistic map interactions and higher frequency harmonics
        chaotic_term = 0.05 * np.sum(np.sin(9 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) * 
                                    (np.sin(5 * np.pi * x_norm) + 0.6 * np.cos(7 * np.pi * x_norm) + 
                                     0.3 * np.sin(8 * np.pi * x_norm)))
        
        # Stronger cross-dimensional interaction with non-linear coupling and adaptive weights
        cross_term = 0.35 * np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                                np.exp(-0.4 * np.abs(x_norm[:-1] + x_norm[1:])) * 
                                (1 + 0.2 * np.sin(4 * np.pi * (x_norm[:-1] + x_norm[1:]))))
        
        # Novel hybrid scaling factor with fractal frequency modulation
        scale_factor = 1.5 + 0.4 * np.sin(5 * r) * np.cos(3 * r) * np.sin(7 * r)
        
        # Complex global modulation with multi-fractal harmonic interactions
        global_mod = 0.15 * np.sum(np.sin(12 * x_norm) * np.cos(10 * x_norm) * 
                                 (1 + 0.25 * np.sin(9 * x_norm) * np.cos(6 * x_norm)))
        
        # Additional chaotic interference term with dynamic amplitude modulation
        interference_term = 0.08 * np.sum(np.sin(13 * np.pi * x_norm) * 
                                         np.cos(14 * np.pi * x_norm) * 
                                         np.exp(-0.5 * r**2))
        
        return scale_factor * (radial_term + trig_term + chaotic_term + cross_term + global_mod + interference_term)