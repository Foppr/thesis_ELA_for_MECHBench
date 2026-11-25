import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with modified exponential decay and additional harmonic
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**3) * (1 + 0.5 * np.sin(7 * r) * np.cos(4 * r) + 0.2 * np.sin(11 * r))
        
        # Trigonometric modulation with altered frequencies and phase shifts
        trig_term = np.sum(np.cos(5 * np.pi * x_norm) * np.sin(6 * np.pi * x_norm) * 
                          (1 + 0.3 * np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm)))
        
        # Chaotic component with logistic map inspired interactions and higher frequency oscillations
        chaotic_term = 0.05 * np.sum(np.sin(8 * np.pi * x_norm) * np.cos(10 * np.pi * x_norm) * 
                                    (np.sin(5 * np.pi * x_norm) + 0.6 * np.cos(7 * np.pi * x_norm) + 
                                     0.3 * np.sin(9 * np.pi * x_norm)))
        
        # Enhanced cross-dimensional interaction with non-linear coupling and varying weights
        cross_term = 0.3 * np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                                np.exp(-0.4 * np.abs(x_norm[:-1] + x_norm[1:])) * 
                                (1 + 0.2 * np.sin(4 * np.pi * (x_norm[:-1] + x_norm[1:])) + 
                                 0.1 * np.cos(5 * np.pi * (x_norm[:-1] - x_norm[1:]))))
        
        # Add a dynamic scaling factor based on multiple harmonic functions
        scale_factor = 1.3 + 0.4 * np.sin(5 * r) * np.cos(3 * r) + 0.2 * np.cos(8 * r)
        
        # Add a global modulation term to increase function complexity
        global_mod = 0.15 * np.sum(np.sin(12 * x_norm) * np.cos(10 * x_norm) + 
                                 0.1 * np.sin(15 * x_norm) * np.cos(13 * x_norm))
        
        # Add a high-frequency chaotic modulation component
        high_freq_mod = 0.08 * np.sum(np.sin(20 * np.pi * x_norm) * np.cos(18 * np.pi * x_norm) * 
                                     (1 + 0.3 * np.sin(16 * np.pi * x_norm)))
        
        # Add a multi-modal peak component with varying amplitudes
        peak_term = 0.2 * np.sum(np.exp(-np.abs(x_norm)) * np.cos(15 * np.pi * x_norm))
        
        return scale_factor * (radial_term + trig_term + chaotic_term + cross_term + global_mod + 
                              high_freq_mod + peak_term)