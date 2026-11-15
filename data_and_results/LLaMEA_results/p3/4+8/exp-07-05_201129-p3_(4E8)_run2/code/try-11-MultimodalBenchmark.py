import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial term with mixed degrees
        poly_term = np.sum(x_scaled**4 + 0.5 * x_scaled**3 + 0.1 * x_scaled**2)
        
        # Trigonometric term creating multiple oscillations
        trig_term = np.sum(np.sin(3.0 * np.pi * x_scaled) * np.cos(2.0 * np.pi * x_scaled))
        
        # Exponential barrier term to create steep gradients
        exp_term = np.sum(np.exp(-x_scaled**2) * (1.0 + 0.5 * np.sin(5.0 * x_scaled)))
        
        # Cross-term interaction
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(np.pi * x_scaled[:-1]))
        
        # Combine all terms with different weights
        result = 0.3 * poly_term + 0.4 * trig_term + 0.2 * exp_term + 0.1 * cross_term
        
        # Add a small penalty for distance from origin to encourage convergence
        penalty = 0.05 * np.sum(x_scaled**2)
        
        return result + penalty