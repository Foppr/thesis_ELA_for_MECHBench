import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial term with mixed degrees
        poly_term = np.sum(x_scaled**4 + 0.5 * x_scaled**3 + 0.2 * x_scaled**2)
        
        # Trigonometric term creating oscillations
        trig_term = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled))
        
        # Exponential barrier term to create steep gradients near boundaries
        exp_barrier = np.sum(np.exp(-x_scaled**2 / 0.5) + np.exp(-(x_scaled - 0.5)**2 / 0.3))
        
        # Cross-term interaction creating complex correlations
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(np.pi * x_scaled[:-1]))
        
        # Combine all terms with different weights
        result = 2.0 * poly_term + 0.8 * trig_term - 0.3 * exp_barrier + 0.1 * cross_term
        
        return result