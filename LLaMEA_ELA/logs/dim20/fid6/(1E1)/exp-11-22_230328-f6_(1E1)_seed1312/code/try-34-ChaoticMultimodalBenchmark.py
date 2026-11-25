import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**2) * (1 + 0.5 * np.sin(10 * r))
        
        # Trigonometric modulation in each dimension
        trig_term = np.sum(np.cos(2 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Chaotic component using sine map-like interactions
        chaotic_term = 0.01 * np.sum(np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * 
                                    (np.sin(2 * np.pi * x_norm) + 0.5))
        
        # Cross-dimensional interaction with varying weights
        cross_term = 0.1 * np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * np.exp(-np.abs(x_norm[:-1] + x_norm[1:])))
        
        # Add a scaling factor to control the overall difficulty
        scale_factor = 1.0 + 0.3 * np.sin(4 * r)
        
        return scale_factor * (radial_term + trig_term + chaotic_term + cross_term)