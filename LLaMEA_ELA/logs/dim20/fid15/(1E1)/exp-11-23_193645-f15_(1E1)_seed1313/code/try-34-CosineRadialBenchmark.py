import numpy as np

class CosineRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced periodic cosine wave component with higher frequencies and more complex interactions
        cosine_term = np.sum(np.cos(5 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                            np.cos(13 * np.pi * x_norm) + 0.6 * np.cos(7 * np.pi * x_norm) * 
                            np.cos(11 * np.pi * x_norm))
        
        # Modified radial component with stronger nonlinear terms
        radial_term = np.sum(x_norm ** 4 + 0.2 * (x_norm ** 6) + 0.05 * (x_norm ** 8))
        
        # Enhanced cross-dimensional coupling with exponential and polynomial decay
        coupling_term = 0.3 * np.sum(np.exp(-0.3 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
                                   (x_norm[:-1] ** 2 + x_norm[1:] ** 2) + 
                                   0.15 * np.abs(x_norm[:-1] - x_norm[1:]) ** 3)
        
        # Stronger nonlinear interaction terms with multiple frequency modulations
        interaction_term = 0.4 * np.sum(np.cos(3 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                      (x_norm[:-1] ** 4 + x_norm[1:] ** 4) + 
                                      0.2 * np.sin(4 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                      (x_norm[:-1] ** 3 + x_norm[1:] ** 3))
        
        # Additional harmonic component with varying amplitudes
        harmonic_term = 0.15 * np.sum(np.sin(2 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Combined function with adjusted weights for increased complexity
        result = 3.0 * cosine_term + 1.2 * radial_term + 0.8 * coupling_term + 0.5 * interaction_term + 0.2 * harmonic_term
        
        return result