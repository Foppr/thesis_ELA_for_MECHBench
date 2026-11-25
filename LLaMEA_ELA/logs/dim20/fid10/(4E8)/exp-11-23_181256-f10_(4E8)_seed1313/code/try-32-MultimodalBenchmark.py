import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for better conditioning
        x_norm = x / 5.0
        
        # Polynomial terms with different degrees to create varying curvature
        poly_term = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.1 * x_norm**2)
        
        # Exponential terms that create steep gradients and narrow valleys
        exp_term = np.sum(np.exp(-2.0 * x_norm**2) - 1.0)
        
        # Trigonometric terms with multiple frequencies to generate many local minima
        trig_term = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # New cross-term interaction that creates complex dependency between dimensions with sine coupling
        cross_term = np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) * x_norm[:-1] * x_norm[1:])
        
        # Combine all terms with different weights to create a challenging landscape
        return 0.5 * poly_term + 0.3 * exp_term + 0.2 * trig_term + 0.1 * cross_term