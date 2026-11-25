import numpy as np

class MultimodalPeriodicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for periodic components
        x_norm = x / 5.0
        
        # Highly chaotic periodic component with multiple frequencies and amplitudes
        periodic_term = np.sum(np.sin(5 * np.pi * x_norm) ** 3 + 0.7 * np.sin(11 * np.pi * x_norm) ** 3 + 
                              0.3 * np.sin(17 * np.pi * x_norm) ** 3 + 0.1 * np.sin(23 * np.pi * x_norm) ** 3)
        
        # Exponential quadratic basin to create rugged landscape
        quadratic_term = np.sum(np.exp(0.5 * x_norm ** 2) - 1.0)
        
        # Complex interaction terms with long-range dependencies
        interaction_term = 0.3 * np.sum((x_norm[:-1] - x_norm[1:]) ** 4) + 0.2 * np.sum((x_norm[:-2] - x_norm[2:]) ** 4) + \
                          0.1 * np.sum((x_norm[:-3] - x_norm[3:]) ** 4)
        
        # Nonlinear cross-terms with exponential coupling
        cross_term = 0.15 * np.sum(np.exp(x_norm[:-1] * x_norm[1:]) - 1.0) + \
                     0.1 * np.sum(np.exp(0.5 * (x_norm[:-1] ** 2 + x_norm[1:] ** 2)) - 1.0)
        
        # Additional chaotic cross-dimensional coupling
        coupling_term = 0.05 * np.sum(np.sin(x_norm[:-1] * x_norm[1:]) ** 2) + \
                        0.03 * np.sum(np.cos(x_norm[:-2] * x_norm[2:]) ** 2)
        
        # Combine all terms with different weights
        result = 3.0 * periodic_term + 0.8 * quadratic_term + 0.5 * interaction_term + 0.3 * cross_term + 0.2 * coupling_term
        
        return result