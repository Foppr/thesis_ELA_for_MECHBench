import numpy as np

class SaddleTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sine-based periodic component with varying frequencies
        periodic_term = np.sum(np.sin(2 * np.pi * x_norm) * 
                              np.cos(3 * np.pi * x_norm) * 
                              np.sin(5 * np.pi * x_norm))
        
        # Hyperbolic tangent based saddle point structure
        saddle_term = np.sum(np.tanh(x_norm)**2 - 0.5 * x_norm**2)
        
        # Adaptive conditioning per dimension with exponential scaling
        condition_term = np.sum(np.exp(0.15 * np.abs(x_norm)) * x_norm**2)
        
        # Cross-dimensional coupling via product of sinusoids with increased strength
        coupling_term = 0.4 * np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * 
                                   np.cos(np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Multi-modal structure with higher-order polynomial for increased complexity
        multimodal_term = 0.3 * np.sum((x_norm**6 - 3 * x_norm**4 + 3 * x_norm**2 - 1)**2)
        
        # Asymmetric quadratic penalty with modified exponent to bias optimization more strongly
        asymmetry_term = 0.15 * np.sum(np.maximum(x_norm, 0)**4 + 
                                     np.minimum(x_norm, 0)**4)
        
        return periodic_term + saddle_term + condition_term + coupling_term + \
               multimodal_term + asymmetry_term