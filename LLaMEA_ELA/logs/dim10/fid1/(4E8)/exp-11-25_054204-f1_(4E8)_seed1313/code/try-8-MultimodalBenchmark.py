import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial term with mixed degrees to create varied curvature
        poly_term = np.sum(x_scaled**4 + 0.5 * x_scaled**2)
        
        # Trigonometric terms creating oscillations in multiple directions
        trig_term = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled))
        
        # Exponential barrier term to create steep regions near boundaries
        exp_barrier = np.sum(np.exp(-x_scaled**2 / 0.5))
        
        # Cross-term creating interaction between dimensions
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(np.pi * x_scaled[:-1]))
        
        # Combine all terms with different weights
        return 0.3 * poly_term + 0.4 * trig_term - 0.2 * exp_barrier + 0.1 * cross_term + 2.0