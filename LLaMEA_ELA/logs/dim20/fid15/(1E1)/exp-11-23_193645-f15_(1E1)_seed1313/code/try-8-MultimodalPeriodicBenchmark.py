import numpy as np

class MultimodalPeriodicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for periodic components
        x_norm = x / 5.0
        
        # Enhanced periodic component with multiple frequencies and amplitudes
        periodic_term = np.sum(2.0 * np.sin(3 * np.pi * x_norm) ** 2 + 
                              1.5 * np.sin(7 * np.pi * x_norm) ** 2 + 
                              0.8 * np.sin(11 * np.pi * x_norm) ** 2)
        
        # Quadratic basin with variable coefficients
        quadratic_term = np.sum(0.5 * x_norm ** 2 + 0.3 * x_norm ** 4)
        
        # Complex interaction terms with long-range dependencies
        interaction_term = 0.3 * np.sum((x_norm[:-1] - x_norm[1:]) ** 2) + \
                          0.2 * np.sum((x_norm[:-2] - x_norm[2:]) ** 2) + \
                          0.1 * np.sum((x_norm[:-3] - x_norm[3:]) ** 2)
        
        # Nonlinear cross-terms with higher-order interactions
        cross_term = 0.15 * np.sum(x_norm[:-1] * x_norm[1:] ** 2) + \
                     0.1 * np.sum(x_norm[:-2] * x_norm[2:] ** 3)
        
        # Additional ruggedness through exponential modulation
        modulated_term = np.sum(np.exp(2 * np.abs(x_norm)) * np.sin(5 * np.pi * x_norm) ** 2)
        
        # Combine all terms with different weights
        result = 3.0 * periodic_term + 0.7 * quadratic_term + 0.5 * interaction_term + \
                 0.3 * cross_term + 0.4 * modulated_term
        
        return result