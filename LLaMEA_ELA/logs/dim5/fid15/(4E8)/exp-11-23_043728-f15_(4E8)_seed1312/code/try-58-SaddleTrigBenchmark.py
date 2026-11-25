import numpy as np

class SaddleTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sinusoidal component with septimic terms
        chaotic_term = np.sum(np.sin(7 * np.pi * x_norm) * 
                             np.cos(5 * np.pi * x_norm) * 
                             np.sin(3 * np.pi * x_norm) * 
                             np.cos(2 * np.pi * x_norm) * 
                             np.sin(4 * np.pi * x_norm) * 
                             np.cos(6 * np.pi * x_norm) * 
                             np.sin(np.pi * x_norm))
        
        # Saddle point structure with hyperbolic tangent and cubic terms
        saddle_term = np.sum(np.tanh(x_norm)**3 - 0.3 * x_norm**3 + 0.1 * x_norm**2)
        
        # Exponentially increasing conditioning with adaptive scaling
        condition_term = np.sum(np.exp(0.2 * np.abs(x_norm)) * 
                               np.exp(0.15 * x_norm**2) * x_norm**2)
        
        # Novel cross-dimensional coupling with chaotic interaction
        coupling_term = 0.5 * np.sum(np.sin(np.pi * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                   np.cos(np.pi * (x_norm[:-1] * x_norm[1:])) * 
                                   np.sin(2 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Highly multimodal structure with multiple local minima and maxima
        multimodal_term = 0.4 * np.sum((x_norm**6 - 3 * x_norm**4 + 3 * x_norm**2 - 1)**2)
        
        # Strong asymmetric penalty with cubic and quartic components
        asymmetry_term = 0.2 * np.sum(np.maximum(x_norm, 0)**4 + 
                                    np.minimum(x_norm, 0)**4 + 
                                    np.maximum(x_norm, 0)**2 + 
                                    np.minimum(x_norm, 0)**2)
        
        # Add chaotic noise component for increased difficulty
        noise_term = 0.1 * np.sum(np.sin(13 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm))
        
        return chaotic_term + saddle_term + condition_term + coupling_term + \
               multimodal_term + asymmetry_term + noise_term