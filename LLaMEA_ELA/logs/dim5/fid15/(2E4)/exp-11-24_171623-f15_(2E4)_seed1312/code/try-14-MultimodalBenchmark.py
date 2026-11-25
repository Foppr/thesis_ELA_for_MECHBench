import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial term with varying degrees
        poly_term = np.sum((x_norm ** 4) + 0.3 * (x_norm ** 3) + 0.1 * (x_norm ** 2))
        
        # Trigonometric term creating multiple oscillations
        trig_term = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Radial component with multiple peaks
        radial_term = np.sum(1.0 / (1.0 + 0.5 * np.sum(x_norm**2, axis=0)))
        
        # Interaction term between dimensions
        interaction_term = np.sum(np.sin(np.sqrt(np.sum(x_norm**2, axis=0))) * 
                                np.cos(np.sum(x_norm, axis=0)))
        
        # Combine all terms with different weights
        result = 0.4 * poly_term + 0.3 * trig_term + 0.2 * radial_term + 0.1 * interaction_term
        
        return result