import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with enhanced exponential decay and radial symmetry
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-2 * r**2) * (1 + 0.3 * np.sin(15 * r) + 0.2 * np.cos(8 * r))
        
        # Modified trigonometric modulation with higher frequency components
        trig_term = np.sum(np.cos(3 * np.pi * x_norm) * np.sin(4 * np.pi * x_norm) + 
                          0.5 * np.sin(5 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))
        
        # Enhanced chaotic component with stronger nonlinear interactions
        chaotic_term = 0.02 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                                    (np.sin(3 * np.pi * x_norm) + 0.4 * np.cos(4 * np.pi * x_norm)))
        
        # Modified cross-dimensional interaction with stronger coupling
        cross_term = 0.15 * np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * np.exp(-0.5 * np.abs(x_norm[:-1] + x_norm[1:])))
        
        # Additional scaling factor with more complex modulation
        scale_factor = 1.2 + 0.4 * np.sin(3 * r) * np.cos(5 * r)
        
        return scale_factor * (radial_term + trig_term + chaotic_term + cross_term)