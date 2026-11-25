import numpy as np

class CosineRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced periodic cosine wave component with multiple frequencies
        cosine_term = np.sum(np.cos(2 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) * 
                            np.cos(9 * np.pi * x_norm) + 0.3 * np.cos(7 * np.pi * x_norm))
        
        # Modified radial component with quadratic and quartic terms
        radial_term = np.sum(x_norm ** 2 + 0.2 * (x_norm ** 4))
        
        # Improved cross-dimensional coupling with exponential decay
        coupling_term = 0.2 * np.sum(np.exp(-0.3 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
                                   (x_norm[:-1] ** 2 + x_norm[1:] ** 2))
        
        # Enhanced nonlinear interaction terms with sine modulation
        interaction_term = 0.3 * np.sum(np.sin(3 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                      (x_norm[:-1] ** 2 + x_norm[1:] ** 2))
        
        # Additional harmonic component for increased complexity
        harmonic_term = 0.15 * np.sum(np.cos(4 * np.pi * x_norm) * np.sin(6 * np.pi * x_norm))
        
        # Combined function with adjusted weights
        result = 3.0 * cosine_term + 0.7 * radial_term + 0.5 * coupling_term + 0.25 * interaction_term + 0.2 * harmonic_term
        
        return result