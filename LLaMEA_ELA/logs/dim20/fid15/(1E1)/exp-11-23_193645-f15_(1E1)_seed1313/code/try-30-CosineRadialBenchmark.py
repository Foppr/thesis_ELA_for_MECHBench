import numpy as np

class CosineRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Modified periodic cosine wave component with different frequencies and amplitudes
        cosine_term = np.sum(0.8 * np.cos(2 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * 
                            np.cos(10 * np.pi * x_norm) + 0.3 * np.cos(4 * np.pi * x_norm))
        
        # Altered radial component with different powers and coefficients
        radial_term = np.sum(0.8 * (x_norm ** 3) + 0.2 * (x_norm ** 5) + 0.1 * (x_norm ** 7))
        
        # Enhanced cross-dimensional coupling with stronger Gaussian decay
        coupling_term = 0.2 * np.sum(np.exp(-0.3 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
                                   (x_norm[:-1] ** 2 + x_norm[1:] ** 2))
        
        # Modified nonlinear interaction terms with different modulation
        interaction_term = 0.3 * np.sum(np.cos(3 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                      (x_norm[:-1] ** 4 + x_norm[1:] ** 4))
        
        # Combined function with updated weights
        result = 2.0 * cosine_term + 1.2 * radial_term + 0.8 * coupling_term + 0.5 * interaction_term
        
        return result