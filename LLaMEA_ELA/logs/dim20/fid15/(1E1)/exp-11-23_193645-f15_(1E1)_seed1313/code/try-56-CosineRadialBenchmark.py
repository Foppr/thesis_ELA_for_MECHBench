import numpy as np

class CosineRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Modified periodic cosine wave component with higher frequencies and different amplitudes
        cosine_term = np.sum(0.8 * np.cos(4 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                            np.cos(13 * np.pi * x_norm) + 0.3 * np.cos(6 * np.pi * x_norm))
        
        # Altered radial component with stronger quintic and sextic terms
        radial_term = np.sum(x_norm ** 5 + 0.2 * (x_norm ** 6))
        
        # Modified cross-dimensional coupling with exponential decay
        coupling_term = 0.2 * np.sum(np.exp(-0.3 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
                                   (x_norm[:-1] ** 2 + x_norm[1:] ** 2))
        
        # Adjusted nonlinear interaction terms with different modulation
        interaction_term = 0.3 * np.sum(np.cos(3 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                      (x_norm[:-1] ** 4 + x_norm[1:] ** 4))
        
        # Combined function with new weights
        result = 3.0 * cosine_term + 1.2 * radial_term + 0.7 * coupling_term + 0.4 * interaction_term
        
        return result