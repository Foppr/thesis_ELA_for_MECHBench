import numpy as np

class ChaoticRadialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with chaotic modulation
        radial = np.sum(x_norm**2 * (1 + 0.3 * np.sin(10 * np.sum(x_norm**2))))
        
        # Sinusoidal modulation in each dimension with varying frequencies
        sin_modulation = np.sum(np.sin(5 * x_norm) * np.cos(7 * x_norm) * 
                               (1 + 0.2 * np.sin(3 * x_norm)))
        
        # Asymmetric saddle points with varying steepness
        saddle = np.sum((x_norm**2 - 1)**2 * (1 + 0.4 * np.cos(4 * x_norm)) * 
                       np.exp(-0.5 * (x_norm**2)))
        
        # Multi-scale chaotic interaction between dimensions
        chaotic_interaction = np.sum(np.sin(np.pi * x_norm[:-1]) * 
                                   np.cos(np.pi * x_norm[1:]) * 
                                   (1 + 0.3 * np.sin(2 * np.pi * x_norm[:-1])) * 
                                   (1 + 0.2 * np.cos(3 * np.pi * x_norm[1:])))
        
        # Fractal-like structure with power-law scaling
        fractal = np.sum(np.abs(x_norm)**1.7 * (1 + 0.25 * np.sin(8 * x_norm)) * 
                        np.exp(-0.1 * np.abs(x_norm)))
        
        # Directional bias with local conditioning
        directional_bias = np.sum((x_norm + 0.5)**3 * (1 + 0.3 * np.cos(6 * x_norm)) * 
                                 np.exp(-0.2 * x_norm**2))
        
        # Combined landscape
        return 2.0 * (radial + sin_modulation + saddle + chaotic_interaction + 
                     fractal + directional_bias)