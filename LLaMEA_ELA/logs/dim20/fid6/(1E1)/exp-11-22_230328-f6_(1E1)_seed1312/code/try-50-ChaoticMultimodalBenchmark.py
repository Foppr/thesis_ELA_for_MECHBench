import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with modified exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**3) * (1 + 0.3 * np.sin(8 * r))
        
        # Trigonometric modulation with altered frequencies
        trig_term = np.sum(np.cos(3 * np.pi * x_norm) * np.sin(4 * np.pi * x_norm))
        
        # Chaotic component with modified sine map interactions and phase shift
        chaotic_term = 0.02 * np.sum(np.sin(6 * np.pi * x_norm + 0.5) * np.cos(8 * np.pi * x_norm + 0.3) * 
                                    (np.sin(3 * np.pi * x_norm) + 0.4))
        
        # Enhanced cross-dimensional interaction with different weights
        cross_term = 0.15 * np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * np.exp(-0.5 * np.abs(x_norm[:-1] + x_norm[1:])))
        
        # Additional sinusoidal modulation to increase complexity
        mod_term = 0.08 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Add a scaling factor to control the overall difficulty
        scale_factor = 1.0 + 0.4 * np.sin(5 * r)
        
        return scale_factor * (radial_term + trig_term + chaotic_term + cross_term + mod_term)