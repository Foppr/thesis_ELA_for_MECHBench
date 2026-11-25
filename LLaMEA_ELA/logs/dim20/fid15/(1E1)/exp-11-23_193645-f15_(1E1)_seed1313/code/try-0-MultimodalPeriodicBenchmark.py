import numpy as np

class MultimodalPeriodicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for periodic components
        x_norm = x / 5.0
        
        # Periodic component with multiple global minima
        periodic_term = np.sum(np.sin(5 * np.pi * x_norm) ** 2)
        
        # Quadratic basin to create a more complex landscape
        quadratic_term = np.sum(x_norm ** 2)
        
        # Add interaction terms between dimensions
        interaction_term = 0.1 * np.sum((x_norm[:-1] - x_norm[1:]) ** 2)
        
        # Combine all terms with different weights
        result = 2.0 * periodic_term + 0.5 * quadratic_term + 0.3 * interaction_term
        
        return result