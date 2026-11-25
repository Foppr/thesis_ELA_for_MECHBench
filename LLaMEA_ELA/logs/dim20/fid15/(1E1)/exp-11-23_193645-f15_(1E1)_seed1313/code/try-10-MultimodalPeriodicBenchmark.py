import numpy as np

class MultimodalPeriodicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for periodic components
        x_norm = x / 5.0
        
        # Enhanced periodic component with multiple frequencies
        periodic_term = np.sum(np.sin(3.5 * np.pi * x_norm) ** 2 + 0.6 * np.sin(7.2 * np.pi * x_norm) ** 2)
        
        # Quadratic basin to create a more complex landscape
        quadratic_term = np.sum(x_norm ** 2)
        
        # Enhanced interaction terms between dimensions
        interaction_term = 0.25 * np.sum((x_norm[:-1] - x_norm[1:]) ** 2) + 0.15 * np.sum((x_norm[:-2] - x_norm[2:]) ** 2)
        
        # Additional nonlinear cross-terms
        cross_term = 0.15 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Combine all terms with different weights
        result = 2.7 * periodic_term + 0.65 * quadratic_term + 0.45 * interaction_term + 0.25 * cross_term
        
        return result