import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial terms with varying degrees
        poly_term = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.1 * x_norm**2)
        
        # Trigonometric components creating oscillations
        trig_term = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Exponential barrier terms to create steep gradients
        exp_term = np.sum(np.exp(-x_norm**2) - 1.0)
        
        # Combined function with different weights
        return 2.0 * poly_term + 3.0 * trig_term + 0.5 * exp_term