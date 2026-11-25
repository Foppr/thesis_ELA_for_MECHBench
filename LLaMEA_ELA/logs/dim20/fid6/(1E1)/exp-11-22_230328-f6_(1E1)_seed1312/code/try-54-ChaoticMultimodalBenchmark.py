import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with modified exponential decay and additional harmonic
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**2.5) * (1 + 0.4 * np.sin(6 * r) * np.cos(3 * r))
        
        # Trigonometric modulation with altered frequencies and phase shifts
        trig_term = np.sum(np.cos(4 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm) * 
                          (1 + 0.2 * np.sin(2 * np.pi * x_norm)))
        
        # Chaotic component with logistic map inspired interactions and higher frequency oscillations
        chaotic_term = 0.03 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                                    (np.sin(4 * np.pi * x_norm) + 0.5 * np.cos(6 * np.pi * x_norm)))
        
        # Enhanced cross-dimensional interaction with non-linear coupling and varying weights
        cross_term = 0.2 * np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                                np.exp(-0.3 * np.abs(x_norm[:-1] + x_norm[1:])) * 
                                (1 + 0.1 * np.sin(3 * np.pi * (x_norm[:-1] + x_norm[1:]))))
        
        # Add a dynamic scaling factor based on multiple harmonic functions
        scale_factor = 1.2 + 0.3 * np.sin(4 * r) * np.cos(2 * r)
        
        # Add a global modulation term to increase function complexity
        global_mod = 0.1 * np.sum(np.sin(10 * x_norm) * np.cos(8 * x_norm))
        
        return scale_factor * (radial_term + trig_term + chaotic_term + cross_term + global_mod)