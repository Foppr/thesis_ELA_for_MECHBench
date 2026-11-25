import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Coupled harmonic oscillators with phase-locked interactions
        oscillator_term = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm) * 
                                (1 + 0.2 * np.sin(3 * np.pi * x_norm)) * 
                                np.exp(-0.1 * np.abs(x_norm)))
        
        # Saddle point structure via asymmetric cubic interactions
        saddle_term = np.sum((x_norm**3 - 0.5 * x_norm) * 
                            np.cos(2 * x_norm) * 
                            np.exp(-0.05 * x_norm**2))
        
        # Spatially varying frequency modulation with periodicity
        freq_mod = np.sum(np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * 
                         (1 + 0.1 * np.cos(2 * x_norm)) * 
                         np.exp(-0.15 * np.abs(x_norm)))
        
        # Gradient flow complexity through non-linear coupling
        gradient_flow = np.sum((x_norm**4 + 0.3 * x_norm**2 - 0.1) * 
                              np.sin(3 * x_norm) * 
                              np.exp(-0.1 * x_norm**2))
        
        # Embedded saddle points with directional bias
        saddle_bias = 0.3 * np.sum((x_norm[:-1] - x_norm[1:])**2 * 
                                 np.exp(-0.1 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                 np.sin(0.5 * (x_norm[:-1] + x_norm[1:])))
        
        # Global conditioning term with polynomial scaling
        conditioning = 0.05 * np.sum(x_norm**5)
        
        # Combine all terms
        return oscillator_term + saddle_term - freq_mod + gradient_flow + saddle_bias + conditioning