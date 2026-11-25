import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic_term = np.sum(x_norm**2)
        
        # Chaotic sinusoidal component with multiple frequencies
        sin_term = np.sum(np.sin(5 * np.pi * x_norm) * np.sin(13 * np.pi * x_norm))
        
        # Enhanced polynomial terms with higher degrees for increased complexity
        poly_term = np.sum(x_norm**4) + 0.2 * np.sum(x_norm**6) + 0.05 * np.sum(x_norm**8)
        
        # Interaction terms between dimensions with varying coupling strengths
        interaction_term = 0.1 * np.sum((x_norm[:-1] - x_norm[1:])**2) + \
                          0.05 * np.sum((x_norm[:-2] + x_norm[2:])**2)
        
        # Additional cross-term interactions to create more complex landscape
        cross_term = 0.03 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Combine all terms with different weights to create a challenging landscape
        return quadratic_term + 0.8 * sin_term + 0.02 * poly_term + interaction_term + cross_term