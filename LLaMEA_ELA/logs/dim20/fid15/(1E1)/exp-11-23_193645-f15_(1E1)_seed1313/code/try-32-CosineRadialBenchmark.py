import numpy as np

class CosineRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced periodic cosine wave component with higher frequencies and more complex interactions
        cosine_term = np.sum(np.cos(4 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm) * 
                            np.cos(12 * np.pi * x_norm) + 0.3 * np.cos(6 * np.pi * x_norm))
        
        # Modified radial component with stronger nonlinearity
        radial_term = np.sum(x_norm ** 4 + 0.2 * (x_norm ** 6))
        
        # Enhanced cross-dimensional coupling with exponential decay and additional interaction
        coupling_term = 0.2 * np.sum(np.exp(-0.3 * (x_norm[:-1] - x_norm[1:]) ** 2) * 
                                   (x_norm[:-1] ** 2 + x_norm[1:] ** 2) + 
                                   0.1 * np.abs(x_norm[:-1] - x_norm[1:]))
        
        # Strengthened nonlinear interaction terms with additional trigonometric modulation
        interaction_term = 0.3 * np.sum(np.cos(3 * np.pi * (x_norm[:-1] - x_norm[1:])) * 
                                      (x_norm[:-1] ** 4 + x_norm[1:] ** 4) + 
                                      0.15 * np.sin(2 * np.pi * (x_norm[:-1] + x_norm[1:])))
        
        # Combined function with adjusted weights for better balance
        result = 3.0 * cosine_term + 1.0 * radial_term + 0.7 * coupling_term + 0.4 * interaction_term
        
        return result