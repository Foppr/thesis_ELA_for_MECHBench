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
        
        # Exponential interaction terms to create ruggedness
        exp_interaction = np.sum(np.exp(2 * np.abs(x_norm[:-1] - x_norm[1:])) - 1)
        
        # Asymmetric quadratic basin with different weights for positive and negative directions
        asym_quad = np.sum(np.where(x_norm >= 0, 0.8 * x_norm ** 2, 1.2 * x_norm ** 2))
        
        # Cross-terms with exponential weighting
        cross_exp = np.sum(np.exp(0.5 * np.abs(x_norm[:-1] * x_norm[1:])) - 1)
        
        # Additional chaotic cross-term with sine modulation
        chaotic_cross = 0.3 * np.sum(np.sin(4 * np.pi * x_norm[:-1]) * x_norm[1:])
        
        # Combine all terms with different weights
        result = 3.2 * periodic_term + 0.5 * asym_quad + 0.3 * exp_interaction + 0.2 * cross_exp + 0.1 * chaotic_cross
        
        return result